# app.py — updated secure version with safe ping endpoint integrated
import os
import re
import sqlite3
import subprocess
from shlex import split
from flask import Flask, render_template, request, redirect, url_for, session, abort, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

# Configuration
app = Flask(__name__)
# Load secret from environment, fallback to a random secret (rotate in production)
app.secret_key = os.environ.get('FLASK_SECRET_KEY') or os.urandom(32)
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'txt'}  # adjust to your needs
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Harden session cookies
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    SESSION_COOKIE_SECURE=bool(os.environ.get('SESSION_COOKIE_SECURE', False))  # set True in prod with HTTPS
)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# --- Database helpers ---
DB_PATH = os.environ.get('DB_PATH', 'database.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password TEXT
                    )''')
    conn.execute('''CREATE TABLE IF NOT EXISTS posts (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        title TEXT,
                        content TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(id)
                    )''')
    conn.commit()
    conn.close()

# --- Utility functions ---
def allowed_file(filename: str) -> bool:
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    return ext in ALLOWED_EXTENSIONS

def is_valid_hostname(h: str) -> bool:
    # Simple validation: allow only alphanumeric, dots, hyphens
    return bool(re.fullmatch(r"[A-Za-z0-9.-]+", h))

# --- Routes (secured / improved) ---

@app.route('/')
def home():
    return render_template('index.html')

# Simple registration added to create hashed passwords
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        if not username or not password:
            return "Username and password required", 400

        pw_hash = generate_password_hash(password)
        conn = get_db_connection()
        try:
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, pw_hash))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return "Username already exists", 400
        conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')

# Secure login: parameterized query and hashed password check
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        if not username or not password:
            return "Invalid credentials", 401

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        conn.close()
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# Dashboard: parameterized query and ownership enforced
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    conn = get_db_connection()
    posts = conn.execute("SELECT * FROM posts WHERE user_id = ?", (user_id,)).fetchall()
    conn.close()
    return render_template('dashboard.html', posts=posts)

# Create post — uses parameterized insert and basic escaping is left to templates
@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        if not title:
            return "Title required", 400
        user_id = session['user_id']
        conn = get_db_connection()
        conn.execute("INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)", (user_id, title, content))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    return render_template('create_post.html')

# Secure file upload: use secure_filename, allowed extensions, store safely
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        file = request.files.get('file')
        if not file or file.filename == '':
            return "No file provided", 400
        filename = secure_filename(file.filename)
        if not allowed_file(filename):
            return "File type not allowed", 400
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # NOTE: Consider scanning the file (antivirus) before making available
        file.save(save_path)
        return f"File uploaded: {filename}"
    return render_template('upload.html')

# Safe view_post: ensure authorized access and parameterized query
@app.route('/view_post/<int:post_id>')
def view_post(post_id):
    conn = get_db_connection()
    post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    conn.close()
    if post:
        # If you want to enforce that only owners can view: check session user_id
        if 'user_id' not in session or session['user_id'] != post['user_id']:
            # If posts are public, change this; otherwise restrict
            return "Forbidden", 403
        return render_template('view_post.html', post=post)
    return "Post not found", 404

# Integrated safe ping endpoint (no shell=True, validated input)
@app.route('/ping')
def ping():
    host = request.args.get('host', '').strip()
    if not host or not is_valid_hostname(host):
        abort(400, "Invalid host")
    cmd = ["ping", "-c", "1", host]
    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, timeout=5)
        return f"<pre>{result}</pre>"
    except subprocess.CalledProcessError as e:
        return f"Ping failed: {e.output}", 500
    except subprocess.TimeoutExpired:
        return "Ping timed out", 504
    except Exception as e:
        # Generic catch: log in real app
        return f"Error running ping: {str(e)}", 500

# Serve uploaded files (optional). Restrict to authenticated users and safe path
@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    # secure filename again (avoid path traversal)
    filename = secure_filename(filename)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=False)

# App entry
if __name__ == '__main__':
    init_db()
    # Use environment variable FLASK_DEBUG=true for development only
    debug_mode = bool(os.environ.get('FLASK_DEBUG', False))
    app.run(debug=debug_mode, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))










