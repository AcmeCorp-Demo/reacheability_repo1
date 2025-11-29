"""
Unit tests for utility functions.
"""

import pytest
from datetime import datetime
from utils import (
    format_date,
    validate_email,
    chunk_list,
    safe_divide,
    DataProcessor
)


class TestUtilityFunctions:
    """Test suite for utility functions."""
    
    def test_format_date(self):
        """Test date formatting."""
        test_date = datetime(2023, 11, 29, 15, 30, 0)
        result = format_date(test_date)
        assert result == "2023-11-29 15:30:00"
    
    def test_validate_email_valid(self):
        """Test email validation with valid emails."""
        assert validate_email("test@example.com") is True
        assert validate_email("user.name+tag@example.co.uk") is True
    
    def test_validate_email_invalid(self):
        """Test email validation with invalid emails."""
        assert validate_email("invalid.email") is False
        assert validate_email("@example.com") is False
        assert validate_email("test@") is False
    
    def test_chunk_list(self):
        """Test list chunking."""
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        chunks = chunk_list(items, 3)
        assert len(chunks) == 4
        assert chunks[0] == [1, 2, 3]
        assert chunks[-1] == [10]
    
    def test_safe_divide(self):
        """Test safe division."""
        assert safe_divide(10, 2) == 5.0
        assert safe_divide(10, 0) == 0.0
        assert safe_divide(10, 0, default=1.0) == 1.0


class TestDataProcessor:
    """Test suite for DataProcessor class."""
    
    def test_process_data(self):
        """Test data processing."""
        processor = DataProcessor()
        data = [
            {'id': 1, 'name': 'Item 1'},
            {'id': 2, 'name': 'Item 2'}
        ]
        result = processor.process_data(data)
        assert len(result) == 2
        assert processor.processed_count == 2
        assert 'timestamp' in result[0]
    
    def test_reset_counter(self):
        """Test counter reset."""
        processor = DataProcessor()
        processor.process_data([{'id': 1}])
        assert processor.processed_count == 1
        processor.reset_counter()
        assert processor.processed_count == 0


@pytest.fixture
def sample_data():
    """Fixture providing sample test data."""
    return {
        'users': [
            {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
            {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
        ]
    }


def test_sample_data_fixture(sample_data):
    """Test that fixture works correctly."""
    assert len(sample_data['users']) == 2
    assert sample_data['users'][0]['name'] == 'Alice'
