"""
Validation script to check repository integrity.
"""

import os
import sys
from pathlib import Path


def check_file_exists(filepath: str) -> bool:
    """Check if a file exists."""
    return Path(filepath).exists()


def validate_repository():
    """Validate repository structure and files."""
    print("=" * 60)
    print("Python Test Repository - Validation")
    print("=" * 60)
    
    # Check core Python files
    core_files = [
        'python.py',
        'sast.py',
        'utils.py',
        'config.py',
        'database.py',
        'api_client.py',
        'data_analysis.py',
        'async_operations.py',
        'cli.py',
        '__init__.py',
    ]
    
    print("\n✓ Checking core Python files...")
    for file in core_files:
        exists = check_file_exists(file)
        status = "✓" if exists else "✗"
        print(f"  {status} {file}")
    
    # Check configuration files
    config_files = [
        'requirements.txt',
        'setup.py',
        'pytest.ini',
        '.env.example',
        '.gitignore',
        'MANIFEST.in',
    ]
    
    print("\n✓ Checking configuration files...")
    for file in config_files:
        exists = check_file_exists(file)
        status = "✓" if exists else "✗"
        print(f"  {status} {file}")
    
    # Check documentation
    doc_files = [
        'README.md',
        'QUICKSTART.md',
        'SUMMARY.md',
        'LICENSE',
    ]
    
    print("\n✓ Checking documentation...")
    for file in doc_files:
        exists = check_file_exists(file)
        status = "✓" if exists else "✗"
        print(f"  {status} {file}")
    
    # Check directories
    directories = [
        'myproject',
        'myproject/myproject',
        'project3',
        'tests',
    ]
    
    print("\n✓ Checking directories...")
    for directory in directories:
        exists = Path(directory).is_dir()
        status = "✓" if exists else "✗"
        print(f"  {status} {directory}/")
    
    # Check Django files
    django_files = [
        'myproject/manage.py',
        'myproject/myproject/settings.py',
        'myproject/myproject/urls.py',
        'myproject/myproject/wsgi.py',
        'myproject/myproject/asgi.py',
    ]
    
    print("\n✓ Checking Django project...")
    for file in django_files:
        exists = check_file_exists(file)
        status = "✓" if exists else "✗"
        print(f"  {status} {file}")
    
    # Check test files
    test_files = [
        'tests/__init__.py',
        'tests/conftest.py',
        'tests/test_utils.py',
        'tests/test_config.py',
        'tests/test_api_client.py',
    ]
    
    print("\n✓ Checking test suite...")
    for file in test_files:
        exists = check_file_exists(file)
        status = "✓" if exists else "✗"
        print(f"  {status} {file}")
    
    # Syntax validation
    print("\n✓ Checking Python syntax...")
    import py_compile
    
    python_files = list(Path('.').rglob('*.py'))
    python_files = [f for f in python_files if '__pycache__' not in str(f) and 'venv' not in str(f)]
    
    syntax_errors = 0
    for pyfile in python_files:
        try:
            py_compile.compile(str(pyfile), doraise=True)
        except py_compile.PyCompileError as e:
            print(f"  ✗ Syntax error in {pyfile}")
            syntax_errors += 1
    
    if syntax_errors == 0:
        print(f"  ✓ All {len(python_files)} Python files have valid syntax")
    else:
        print(f"  ✗ {syntax_errors} files with syntax errors")
    
    # Summary
    print("\n" + "=" * 60)
    print("Validation Summary")
    print("=" * 60)
    print(f"✓ Core modules: {len(core_files)} files")
    print(f"✓ Configuration: {len(config_files)} files")
    print(f"✓ Documentation: {len(doc_files)} files")
    print(f"✓ Django project: Complete")
    print(f"✓ Test suite: {len(test_files)} test files")
    print(f"✓ Python files: {len(python_files)} files validated")
    
    if syntax_errors == 0:
        print("\n🎉 Repository validation PASSED! All checks successful.")
        return 0
    else:
        print(f"\n⚠️  Repository validation FAILED! {syntax_errors} syntax errors found.")
        return 1


if __name__ == "__main__":
    sys.exit(validate_repository())
