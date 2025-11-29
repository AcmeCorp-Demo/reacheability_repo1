# Makefile for Python Test Repository

.PHONY: help install test lint format clean run-django run-flask run-cli

help:
	@echo "Python Test Repository - Available Commands"
	@echo "==========================================="
	@echo "install      - Install dependencies"
	@echo "test         - Run tests with pytest"
	@echo "test-cov     - Run tests with coverage"
	@echo "lint         - Run flake8 linter"
	@echo "format       - Format code with black"
	@echo "type-check   - Run mypy type checking"
	@echo "clean        - Clean up generated files"
	@echo "run          - Run main application"
	@echo "run-django   - Run Django development server"
	@echo "run-flask    - Run Flask application"
	@echo "run-cli      - Show CLI help"
	@echo "setup        - Initial setup (venv + install)"

install:
	pip install -r requirements.txt

test:
	pytest -v

test-cov:
	pytest --cov=. --cov-report=html --cov-report=term-missing

lint:
	flake8 . --exclude=venv,env,.venv,build,dist

format:
	black . --exclude='/(venv|env|\.venv|build|dist)/'

type-check:
	mypy . --exclude 'venv|env|\.venv|build|dist'

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete 2>/dev/null || true
	find . -type f -name '*.pyo' -delete 2>/dev/null || true
	rm -rf .pytest_cache .coverage htmlcov *.egg-info build dist 2>/dev/null || true

run:
	python python.py

run-django:
	cd myproject && python manage.py runserver

run-flask:
	python sast.py

run-cli:
	python cli.py --help

setup:
	python -m venv venv
	@echo "Virtual environment created. Activate with:"
	@echo "  Windows: venv\\Scripts\\activate"
	@echo "  Linux/Mac: source venv/bin/activate"
	@echo "Then run: make install"
