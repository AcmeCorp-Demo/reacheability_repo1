"""
Unit tests for configuration module.
"""

import pytest
from config import Config, DevelopmentConfig, ProductionConfig, TestingConfig, get_config


class TestConfig:
    """Test suite for configuration classes."""
    
    def test_base_config(self):
        """Test base configuration values."""
        assert Config.APP_NAME is not None
        assert Config.APP_VERSION == '1.0.0'
        assert Config.DB_HOST is not None
    
    def test_get_database_url(self):
        """Test database URL generation."""
        url = Config.get_database_url()
        assert url.startswith('postgresql://')
        assert Config.DB_HOST in url
    
    def test_get_redis_url(self):
        """Test Redis URL generation."""
        url = Config.get_redis_url()
        assert url.startswith('redis://')
        assert str(Config.REDIS_PORT) in url


class TestEnvironmentConfigs:
    """Test suite for environment-specific configurations."""
    
    def test_development_config(self):
        """Test development configuration."""
        assert DevelopmentConfig.DEBUG is True
        assert DevelopmentConfig.TESTING is False
    
    def test_production_config(self):
        """Test production configuration."""
        assert ProductionConfig.DEBUG is False
        assert ProductionConfig.TESTING is False
    
    def test_testing_config(self):
        """Test testing configuration."""
        assert TestingConfig.DEBUG is True
        assert TestingConfig.TESTING is True
        assert TestingConfig.DB_NAME == 'test_db'


def test_get_config():
    """Test getting configuration by environment."""
    dev_config = get_config('development')
    assert dev_config == DevelopmentConfig
    
    prod_config = get_config('production')
    assert prod_config == ProductionConfig
    
    default_config = get_config('unknown')
    assert default_config == DevelopmentConfig
