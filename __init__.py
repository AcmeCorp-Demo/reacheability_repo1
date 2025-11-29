"""
Python Test Repository - A comprehensive Python testing repository.
"""

__version__ = '1.0.0'
__author__ = 'Test Author'
__email__ = 'test@example.com'

from .utils import DataProcessor, validate_email
from .config import get_config
from .data_analysis import DataAnalyzer, generate_sample_data

__all__ = [
    'DataProcessor',
    'validate_email',
    'get_config',
    'DataAnalyzer',
    'generate_sample_data',
]
