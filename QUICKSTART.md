# Quick Start Guide

## Introduction

This Python test repository provides a comprehensive testing environment with multiple frameworks, libraries, and utilities.

## Quick Setup (5 minutes)

### 1. Prerequisites
- Python 3.8+ installed
- pip package manager
- Git (for cloning)

### 2. Installation

```bash
# Clone repository
git clone https://github.com/AcmeCorp-Demo/reacheability_repo1.git
cd reacheability_repo1

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows PowerShell:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. First Run

```bash
# Run main application
python python.py
```

You should see output showing data processing, email validation, and data analysis.

## What's Included

### 🌐 Web Applications
- **Flask App** (`sast.py`) - Security testing application with SQL injection examples
- **Django App** (`myproject/`) - Full Django project with REST framework

### 📊 Data Processing
- **Data Analysis** (`data_analysis.py`) - Pandas/NumPy operations
- **Utils** (`utils.py`) - Common utility functions
- **Async Operations** (`async_operations.py`) - Asyncio examples

### 🔌 API & Database
- **API Client** (`api_client.py`) - HTTP request handling
- **Database** (`database.py`) - MongoDB and SQLAlchemy operations
- **Config** (`config.py`) - Configuration management

### 🧪 Testing
- **Test Suite** (`tests/`) - Comprehensive pytest tests
- **Test Runner** - Run with `pytest`

### 🛠️ CLI Tool
- **Command Line Interface** (`cli.py`) - Rich CLI with multiple commands

## Common Tasks

### Run Tests
```bash
# All tests
pytest

# With coverage
pytest --cov=. --cov-report=html

# Specific test file
pytest tests/test_utils.py

# Verbose output
pytest -v
```

### Use CLI Tools
```bash
# Show help
python cli.py --help

# Generate sample data
python cli.py generate --rows 20

# Validate email
python cli.py validate test@example.com

# Show application info
python cli.py info

# Process data
python cli.py process --count 10
```

### Run Web Applications
```bash
# Flask application
python sast.py
# Visit: http://localhost:5000

# Django application
cd myproject
python manage.py migrate
python manage.py runserver
# Visit: http://localhost:8000
```

### Code Quality
```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
mypy .
```

## Project Components

### 1. Main Application (`python.py`)
Entry point demonstrating various features:
- Configuration loading
- Data processing
- Email validation
- Sample data generation
- Metrics calculation

### 2. Flask Security Testing (`sast.py`)
Intentionally vulnerable Flask app for security testing:
- SQL injection examples
- XSS vulnerabilities
- IDOR vulnerabilities
- File upload issues

### 3. Django Project (`myproject/`)
Full Django setup with:
- REST framework integration
- Database models
- Admin interface
- URL routing
- Settings configuration

### 4. Data Analysis (`data_analysis.py`)
Pandas and NumPy functionality:
- Sample data generation
- Statistics calculation
- Data filtering
- Aggregation operations

### 5. Utilities (`utils.py`)
Common functions:
- Date formatting
- Email validation
- List chunking
- Safe division
- Data processor class

### 6. API Client (`api_client.py`)
HTTP request handling:
- Synchronous requests (requests)
- Asynchronous requests (httpx)
- Session management
- Authentication

### 7. Database Operations (`database.py`)
Database connectivity:
- MongoDB operations
- SQLAlchemy ORM
- User management
- Document operations

### 8. Configuration (`config.py`)
Environment-based configuration:
- Development settings
- Production settings
- Testing settings
- Environment variables

### 9. Async Operations (`async_operations.py`)
Asynchronous programming:
- Async HTTP requests
- Concurrent task execution
- Queue-based processing
- Worker patterns

### 10. CLI Tool (`cli.py`)
Command-line interface:
- Data generation
- Email validation
- App information
- Data processing

## Testing Guide

### Test Structure
```
tests/
├── __init__.py
├── conftest.py          # Pytest configuration and fixtures
├── test_utils.py        # Utils module tests
├── test_config.py       # Configuration tests
└── test_api_client.py   # API client tests
```

### Running Specific Tests
```bash
# Run by file
pytest tests/test_utils.py

# Run by class
pytest tests/test_utils.py::TestUtilityFunctions

# Run by method
pytest tests/test_utils.py::TestUtilityFunctions::test_validate_email_valid

# Run with markers
pytest -m "not slow"
```

### Coverage Reports
```bash
# Generate HTML coverage report
pytest --cov=. --cov-report=html
# Open htmlcov/index.html in browser

# Terminal coverage report
pytest --cov=. --cov-report=term-missing
```

## Configuration

### Environment Variables
Copy `.env.example` to `.env` and customize:

```bash
# Application
APP_NAME=Python Test Repo
DEBUG=True

# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=testdb

# MongoDB
MONGO_URI=mongodb://localhost:27017/

# API
API_KEY=your-api-key-here
```

### Django Settings
Located in `myproject/myproject/settings.py`:
- Database configuration
- Installed apps
- Middleware
- Static files
- REST framework settings

## Examples

### Example 1: Email Validation
```python
from utils import validate_email

emails = ['valid@test.com', 'invalid', 'user@domain.co.uk']
for email in emails:
    if validate_email(email):
        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")
```

### Example 2: Data Analysis
```python
from data_analysis import generate_sample_data, calculate_metrics

# Generate data
df = generate_sample_data(100)
print(f"Generated {len(df)} rows")

# Calculate metrics
metrics = calculate_metrics(df, 'value')
print(f"Mean: {metrics['mean']:.2f}")
print(f"Median: {metrics['median']:.2f}")
```

### Example 3: Database Operations
```python
from database import DatabaseManager

db = DatabaseManager()
db.connect_mongo()

# Insert document
doc_id = db.insert_mongo_document('users', {
    'name': 'John Doe',
    'email': 'john@example.com'
})

# Find documents
users = db.find_mongo_documents('users', {'name': 'John Doe'})
print(f"Found {len(users)} users")
```

### Example 4: Async Operations
```python
import asyncio
from async_operations import async_task_runner

# Run async tasks
results = asyncio.run(async_task_runner(5))
for result in results:
    print(result)
```

## Troubleshooting

### Import Errors
If you get import errors, ensure:
1. Virtual environment is activated
2. Dependencies are installed: `pip install -r requirements.txt`
3. You're in the correct directory

### Database Connection Errors
1. Check if MongoDB/PostgreSQL is running
2. Verify connection strings in `.env`
3. Ensure database credentials are correct

### Test Failures
1. Run with verbose output: `pytest -v`
2. Check individual test: `pytest tests/test_utils.py -v`
3. Review test output for specific errors

### Django Issues
```bash
# Run migrations
cd myproject
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Check for issues
python manage.py check
```

## Next Steps

1. **Explore the Code**: Review each module to understand functionality
2. **Run Tests**: Execute the test suite to see coverage
3. **Try CLI**: Use the CLI tool for various operations
4. **Modify & Experiment**: Add your own features and tests
5. **Read Documentation**: Check docstrings in each module

## Additional Resources

- Python Documentation: https://docs.python.org/
- Django Documentation: https://docs.djangoproject.com/
- Flask Documentation: https://flask.palletsprojects.com/
- Pytest Documentation: https://docs.pytest.org/
- Pandas Documentation: https://pandas.pydata.org/docs/

## Support

For issues or questions:
1. Check this guide first
2. Review module docstrings
3. Check test files for usage examples
4. Open an issue on GitHub

---

**Happy Testing! 🎉**
