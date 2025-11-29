# Python Test Repository

A comprehensive pure Python repository for testing, featuring web frameworks, data analysis, API clients, and database operations.

## Features

- 🌐 **Web Frameworks**: Flask and Django applications
- 📊 **Data Analysis**: Pandas and NumPy data processing
- 🔌 **API Client**: HTTP request handling with requests and httpx
- 💾 **Database Support**: MongoDB and SQLAlchemy integration
- 🧪 **Testing**: Comprehensive pytest test suite
- 🛠️ **Utilities**: Email validation, data processing, configuration management
- 📝 **CLI**: Rich command-line interface

## Project Structure

```
reacheability_repo1/
├── myproject/          # Django web application
│   └── myproject/      # Django settings and configuration
├── project3/           # Additional test project
├── tests/              # Pytest test suite
├── python.py           # Main application entry point
├── sast.py             # Flask security testing application
├── utils.py            # Utility functions
├── config.py           # Configuration management
├── database.py         # Database operations
├── api_client.py       # HTTP API client
├── data_analysis.py    # Data analysis with pandas/numpy
├── cli.py              # Command-line interface
└── requirements.txt    # Python dependencies
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/AcmeCorp-Demo/reacheability_repo1.git
cd reacheability_repo1
```

2. Create a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Usage

### Run the main application
```bash
python python.py
```

### Run the Flask SAST demo
```bash
python sast.py
```

### Use the CLI
```bash
# Generate sample data
python cli.py generate --rows 20

# Validate email
python cli.py validate user@example.com

# Show app info
python cli.py info

# Process test data
python cli.py process --count 10
```

### Django Project
```bash
cd myproject
python manage.py migrate
python manage.py runserver
```

### Run Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_utils.py

# Run with verbose output
pytest -v
```

## Dependencies

### Core Frameworks
- Django 4.1.3 - Web framework
- Django REST Framework 3.12.4 - API framework
- Flask 2.3.3 - Lightweight web framework

### Data Science
- NumPy 1.24.3 - Numerical computing
- Pandas 2.0.3 - Data manipulation
- Matplotlib 3.7.2 - Data visualization
- SciPy 1.11.2 - Scientific computing

### Database
- PyMongo 4.6.2 - MongoDB driver
- SQLAlchemy 2.0.21 - SQL toolkit
- psycopg2-binary 2.9.7 - PostgreSQL adapter

### HTTP & API
- Requests 2.27.0 - HTTP library
- httpx 0.24.1 - Async HTTP client
- aiohttp 3.8.5 - Async HTTP framework

### Testing & Quality
- pytest 7.4.2 - Testing framework
- pytest-cov 4.1.0 - Coverage plugin
- black 23.7.0 - Code formatter
- flake8 6.1.0 - Linter
- mypy 1.5.1 - Type checker

### Utilities
- python-dotenv 1.0.0 - Environment variables
- PyYAML 6.0.1 - YAML parser
- pydantic 2.3.0 - Data validation
- click 8.1.7 - CLI creation
- rich 13.5.2 - Terminal formatting

## Development

### Code Quality

Run linter:
```bash
flake8 .
```

Format code:
```bash
black .
```

Type checking:
```bash
mypy .
```

### Running in Development Mode
```bash
# Set environment
export FLASK_ENV=development  # Linux/Mac
$env:FLASK_ENV="development"  # Windows PowerShell

# Run with auto-reload
python python.py
```

## Examples

### Data Analysis
```python
from data_analysis import generate_sample_data, calculate_metrics

# Generate data
df = generate_sample_data(100)

# Calculate metrics
metrics = calculate_metrics(df, 'value')
print(f"Mean: {metrics['mean']}")
```

### Email Validation
```python
from utils import validate_email

if validate_email('user@example.com'):
    print("Valid email!")
```

### API Client
```python
from api_client import APIClient

client = APIClient(base_url="https://api.example.com")
data = client.get("/endpoint")
```

### Database Operations
```python
from database import DatabaseManager

db = DatabaseManager()
db.connect_mongo()
db.insert_mongo_document('users', {'name': 'John', 'email': 'john@example.com'})
```

## Testing

The repository includes comprehensive tests:

- `tests/test_utils.py` - Utility function tests
- `tests/test_config.py` - Configuration tests
- `tests/test_api_client.py` - API client tests
- `tests/conftest.py` - Pytest configuration

## License

This project is for testing purposes.

## Contributing

This is a test repository. Feel free to experiment and test various features.

## Contact

For issues or questions, please open an issue on GitHub.


