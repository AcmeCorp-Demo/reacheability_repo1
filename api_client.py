"""
API client for making HTTP requests.
"""

import requests
import httpx
from typing import Dict, Any, Optional
import logging
from config import Config

logger = logging.getLogger(__name__)


class APIClient:
    """HTTP API client with requests and httpx support."""
    
    def __init__(self, base_url: str = "", api_key: Optional[str] = None):
        """
        Initialize API client.
        
        Args:
            base_url: Base URL for API requests
            api_key: API key for authentication
        """
        self.base_url = base_url
        self.api_key = api_key or Config.API_KEY
        self.timeout = Config.API_TIMEOUT
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': f'{Config.APP_NAME}/{Config.APP_VERSION}',
            'Authorization': f'Bearer {self.api_key}'
        })
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """
        Make a GET request.
        
        Args:
            endpoint: API endpoint
            params: Query parameters
            
        Returns:
            JSON response or None
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            logger.info(f"GET {url} - Status: {response.status_code}")
            return response.json()
        except requests.RequestException as e:
            logger.error(f"GET request failed: {e}")
            return None
    
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """
        Make a POST request.
        
        Args:
            endpoint: API endpoint
            data: JSON data to send
            
        Returns:
            JSON response or None
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.post(url, json=data, timeout=self.timeout)
            response.raise_for_status()
            logger.info(f"POST {url} - Status: {response.status_code}")
            return response.json()
        except requests.RequestException as e:
            logger.error(f"POST request failed: {e}")
            return None
    
    async def async_get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """
        Make an async GET request using httpx.
        
        Args:
            endpoint: API endpoint
            params: Query parameters
            
        Returns:
            JSON response or None
        """
        url = f"{self.base_url}{endpoint}"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    url,
                    params=params,
                    headers=self.session.headers,
                    timeout=self.timeout
                )
                response.raise_for_status()
                logger.info(f"Async GET {url} - Status: {response.status_code}")
                return response.json()
            except httpx.HTTPError as e:
                logger.error(f"Async GET request failed: {e}")
                return None
    
    def close(self):
        """Close the session."""
        self.session.close()
        logger.info("API client session closed")
