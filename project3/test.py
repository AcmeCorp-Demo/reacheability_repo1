"""
Project3 test module - Data processing and validation tests.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import validate_email, chunk_list, safe_divide
from data_analysis import generate_sample_data, DataAnalyzer
import pandas as pd


def test_email_validation():
    """Test email validation functionality."""
    print("\n=== Testing Email Validation ===")
    test_emails = [
        ('user@example.com', True),
        ('invalid.email', False),
        ('test@domain.co.uk', True),
        ('@nodomain.com', False),
    ]
    
    for email, expected in test_emails:
        result = validate_email(email)
        status = "✓" if result == expected else "✗"
        print(f"{status} {email}: {result}")


def test_data_analysis():
    """Test data analysis functionality."""
    print("\n=== Testing Data Analysis ===")
    
    # Generate sample data
    df = generate_sample_data(30)
    print(f"Generated {len(df)} rows")
    print(f"Columns: {list(df.columns)}")
    
    # Initialize analyzer
    analyzer = DataAnalyzer()
    analyzer.load_data_from_dict(df.to_dict('records'))
    
    # Get statistics
    stats = analyzer.get_statistics()
    print(f"Total rows: {stats['count']}")
    print(f"Null counts: {stats['null_counts']}")
    
    # Filter data
    filtered = analyzer.filter_data('category', 'A')
    print(f"Rows with category 'A': {len(filtered)}")
    
    # Aggregate data
    agg = analyzer.aggregate_by_column('category', 'value', 'mean')
    print("\nMean values by category:")
    print(agg.to_string(index=False))


def test_utility_functions():
    """Test utility functions."""
    print("\n=== Testing Utility Functions ===")
    
    # Test chunking
    items = list(range(1, 26))
    chunks = chunk_list(items, 5)
    print(f"Split {len(items)} items into {len(chunks)} chunks of 5")
    
    # Test safe division
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)} (with zero handling)")
    print(f"15 / 3 = {safe_divide(15, 3)}")


def main():
    """Run all tests."""
    print("=" * 50)
    print("Project3 Test Suite")
    print("=" * 50)
    
    test_email_validation()
    test_data_analysis()
    test_utility_functions()
    
    print("\n" + "=" * 50)
    print("All tests completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
