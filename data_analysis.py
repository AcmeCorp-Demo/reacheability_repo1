"""
Data analysis module using pandas and numpy.
"""

import numpy as np
import pandas as pd
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class DataAnalyzer:
    """Class for data analysis operations."""
    
    def __init__(self):
        """Initialize the data analyzer."""
        self.data = None
    
    def load_data_from_dict(self, data: List[Dict[str, Any]]) -> pd.DataFrame:
        """
        Load data from a list of dictionaries into a DataFrame.
        
        Args:
            data: List of dictionaries
            
        Returns:
            Pandas DataFrame
        """
        self.data = pd.DataFrame(data)
        logger.info(f"Loaded {len(self.data)} rows")
        return self.data
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get basic statistics for the dataset.
        
        Returns:
            Dictionary with statistics
        """
        if self.data is None or self.data.empty:
            logger.warning("No data loaded")
            return {}
        
        stats = {
            'count': len(self.data),
            'columns': list(self.data.columns),
            'numeric_summary': self.data.describe().to_dict() if not self.data.select_dtypes(include=[np.number]).empty else {},
            'null_counts': self.data.isnull().sum().to_dict(),
        }
        
        return stats
    
    def filter_data(self, column: str, value: Any) -> pd.DataFrame:
        """
        Filter data by column value.
        
        Args:
            column: Column name to filter
            value: Value to filter by
            
        Returns:
            Filtered DataFrame
        """
        if self.data is None:
            logger.error("No data loaded")
            return pd.DataFrame()
        
        filtered = self.data[self.data[column] == value]
        logger.info(f"Filtered to {len(filtered)} rows")
        return filtered
    
    def aggregate_by_column(self, group_column: str, agg_column: str, agg_func: str = 'sum') -> pd.DataFrame:
        """
        Aggregate data by a column.
        
        Args:
            group_column: Column to group by
            agg_column: Column to aggregate
            agg_func: Aggregation function ('sum', 'mean', 'count', etc.)
            
        Returns:
            Aggregated DataFrame
        """
        if self.data is None:
            logger.error("No data loaded")
            return pd.DataFrame()
        
        try:
            result = self.data.groupby(group_column)[agg_column].agg(agg_func).reset_index()
            logger.info(f"Aggregated data by {group_column}")
            return result
        except Exception as e:
            logger.error(f"Aggregation failed: {e}")
            return pd.DataFrame()


def generate_sample_data(num_rows: int = 100) -> pd.DataFrame:
    """
    Generate sample data for testing.
    
    Args:
        num_rows: Number of rows to generate
        
    Returns:
        DataFrame with sample data
    """
    np.random.seed(42)
    
    data = {
        'id': range(1, num_rows + 1),
        'category': np.random.choice(['A', 'B', 'C', 'D'], num_rows),
        'value': np.random.randint(1, 100, num_rows),
        'score': np.random.uniform(0, 1, num_rows).round(2),
        'status': np.random.choice(['active', 'inactive'], num_rows)
    }
    
    return pd.DataFrame(data)


def calculate_metrics(data: pd.DataFrame, value_column: str) -> Dict[str, float]:
    """
    Calculate various metrics for a numeric column.
    
    Args:
        data: Input DataFrame
        value_column: Column name to calculate metrics for
        
    Returns:
        Dictionary of metrics
    """
    if value_column not in data.columns:
        logger.error(f"Column {value_column} not found")
        return {}
    
    values = data[value_column].dropna()
    
    metrics = {
        'mean': float(values.mean()),
        'median': float(values.median()),
        'std': float(values.std()),
        'min': float(values.min()),
        'max': float(values.max()),
        'q25': float(values.quantile(0.25)),
        'q75': float(values.quantile(0.75)),
    }
    
    logger.info(f"Calculated metrics for {value_column}")
    return metrics
