"""
Utility functions for the project.
"""

import logging
from typing import List, Dict, Any
from datetime import datetime
import json


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def format_date(date_obj: datetime, format_string: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Format a datetime object to a string.
    
    Args:
        date_obj: The datetime object to format
        format_string: The format string to use
        
    Returns:
        Formatted date string
    """
    return date_obj.strftime(format_string)


def parse_json_file(file_path: str) -> Dict[str, Any]:
    """
    Parse a JSON file and return the contents.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        Dictionary containing the JSON data
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return {}
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in file {file_path}: {e}")
        return {}


def validate_email(email: str) -> bool:
    """
    Basic email validation.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid, False otherwise
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def chunk_list(items: List[Any], chunk_size: int) -> List[List[Any]]:
    """
    Split a list into chunks of specified size.
    
    Args:
        items: List to split
        chunk_size: Size of each chunk
        
    Returns:
        List of chunked lists
    """
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """
    Safely divide two numbers, returning a default value if denominator is zero.
    
    Args:
        numerator: The numerator
        denominator: The denominator
        default: Default value to return if division by zero
        
    Returns:
        Result of division or default value
    """
    try:
        return numerator / denominator
    except ZeroDivisionError:
        logger.warning(f"Division by zero attempted: {numerator}/{denominator}")
        return default


class DataProcessor:
    """Class for processing various data types."""
    
    def __init__(self):
        self.processed_count = 0
    
    def process_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Process a list of data dictionaries.
        
        Args:
            data: List of dictionaries to process
            
        Returns:
            Processed list of dictionaries
        """
        processed = []
        for item in data:
            processed_item = {
                'id': item.get('id'),
                'timestamp': datetime.now().isoformat(),
                'data': item
            }
            processed.append(processed_item)
            self.processed_count += 1
        
        logger.info(f"Processed {len(data)} items. Total: {self.processed_count}")
        return processed
    
    def reset_counter(self):
        """Reset the processed count."""
        self.processed_count = 0
        logger.info("Counter reset")
