"""
Pytest configuration file.
"""

import pytest
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture(scope="session")
def test_data_dir():
    """Fixture providing test data directory path."""
    return Path(__file__).parent / "test_data"


@pytest.fixture
def mock_api_response():
    """Fixture providing mock API response."""
    return {
        'status': 'success',
        'data': {
            'id': 1,
            'name': 'Test Item',
            'created_at': '2023-11-29T00:00:00Z'
        }
    }


def pytest_configure(config):
    """Pytest configuration hook."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
