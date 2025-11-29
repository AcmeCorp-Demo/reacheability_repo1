# PowerShell build script for Windows
# Run with: .\build.ps1 [command]

param(
    [Parameter(Position=0)]
    [string]$Command = "help"
)

function Show-Help {
    Write-Host "Python Test Repository - Available Commands" -ForegroundColor Cyan
    Write-Host "===========================================" -ForegroundColor Cyan
    Write-Host "install      - Install dependencies"
    Write-Host "test         - Run tests with pytest"
    Write-Host "test-cov     - Run tests with coverage"
    Write-Host "lint         - Run flake8 linter"
    Write-Host "format       - Format code with black"
    Write-Host "clean        - Clean up generated files"
    Write-Host "run          - Run main application"
    Write-Host "run-django   - Run Django development server"
    Write-Host "run-flask    - Run Flask application"
    Write-Host "run-cli      - Show CLI help"
    Write-Host "setup        - Initial setup (venv + install)"
}

function Install-Dependencies {
    Write-Host "Installing dependencies..." -ForegroundColor Green
    pip install -r requirements.txt
}

function Run-Tests {
    Write-Host "Running tests..." -ForegroundColor Green
    pytest -v
}

function Run-TestsWithCoverage {
    Write-Host "Running tests with coverage..." -ForegroundColor Green
    pytest --cov=. --cov-report=html --cov-report=term-missing
}

function Run-Lint {
    Write-Host "Running linter..." -ForegroundColor Green
    flake8 . --exclude=venv,env,.venv,build,dist
}

function Run-Format {
    Write-Host "Formatting code..." -ForegroundColor Green
    black . --exclude='/(venv|env|\.venv|build|dist)/'
}

function Clean-Files {
    Write-Host "Cleaning generated files..." -ForegroundColor Green
    Get-ChildItem -Path . -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
    Get-ChildItem -Path . -Recurse -File -Filter *.pyc | Remove-Item -Force -ErrorAction SilentlyContinue
    Get-ChildItem -Path . -Recurse -File -Filter *.pyo | Remove-Item -Force -ErrorAction SilentlyContinue
    Remove-Item -Path .pytest_cache, .coverage, htmlcov, *.egg-info, build, dist -Recurse -Force -ErrorAction SilentlyContinue
}

function Run-App {
    Write-Host "Running main application..." -ForegroundColor Green
    python python.py
}

function Run-Django {
    Write-Host "Running Django server..." -ForegroundColor Green
    Set-Location myproject
    python manage.py runserver
}

function Run-Flask {
    Write-Host "Running Flask application..." -ForegroundColor Green
    python sast.py
}

function Run-CLI {
    Write-Host "CLI Help:" -ForegroundColor Green
    python cli.py --help
}

function Setup-Environment {
    Write-Host "Creating virtual environment..." -ForegroundColor Green
    python -m venv venv
    Write-Host "Virtual environment created!" -ForegroundColor Green
    Write-Host "Activate with: venv\Scripts\activate" -ForegroundColor Yellow
    Write-Host "Then run: .\build.ps1 install" -ForegroundColor Yellow
}

# Command dispatcher
switch ($Command) {
    "help" { Show-Help }
    "install" { Install-Dependencies }
    "test" { Run-Tests }
    "test-cov" { Run-TestsWithCoverage }
    "lint" { Run-Lint }
    "format" { Run-Format }
    "clean" { Clean-Files }
    "run" { Run-App }
    "run-django" { Run-Django }
    "run-flask" { Run-Flask }
    "run-cli" { Run-CLI }
    "setup" { Setup-Environment }
    default { 
        Write-Host "Unknown command: $Command" -ForegroundColor Red
        Show-Help 
    }
}
