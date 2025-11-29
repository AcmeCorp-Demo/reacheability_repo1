"""
Main application entry point.
"""

import logging
from config import get_config
from utils import DataProcessor, validate_email
from data_analysis import generate_sample_data, calculate_metrics

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Main application function."""
    logger.info("Starting Python Test Repository Application")
    
    # Get configuration
    config = get_config()
    logger.info(f"Running in {config.__name__} mode")
    logger.info(f"Application: {config.APP_NAME} v{config.APP_VERSION}")
    
    # Test data processor
    processor = DataProcessor()
    test_data = [
        {'id': 1, 'name': 'Item 1', 'value': 100},
        {'id': 2, 'name': 'Item 2', 'value': 200},
        {'id': 3, 'name': 'Item 3', 'value': 300},
    ]
    processed = processor.process_data(test_data)
    logger.info(f"Processed {len(processed)} items")
    
    # Test email validation
    test_emails = [
        'valid@example.com',
        'invalid.email',
        'user@domain.co.uk'
    ]
    for email in test_emails:
        is_valid = validate_email(email)
        logger.info(f"Email '{email}' is {'valid' if is_valid else 'invalid'}")
    
    # Generate and analyze sample data
    logger.info("Generating sample data...")
    df = generate_sample_data(50)
    logger.info(f"Generated {len(df)} rows with columns: {list(df.columns)}")
    
    # Calculate metrics
    metrics = calculate_metrics(df, 'value')
    logger.info(f"Value metrics: mean={metrics.get('mean', 0):.2f}, median={metrics.get('median', 0):.2f}")
    
    logger.info("Application completed successfully")


if __name__ == "__main__":
    main()
