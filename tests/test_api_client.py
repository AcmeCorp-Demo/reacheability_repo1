"""
Integration tests for API client.
"""

import pytest
from api_client import APIClient


@pytest.fixture
def api_client():
    """Fixture for API client."""
    client = APIClient(base_url="https://api.example.com")
    yield client
    client.close()


class TestAPIClient:
    """Test suite for API client."""
    
    def test_client_initialization(self, api_client):
        """Test API client initialization."""
        assert api_client.base_url == "https://api.example.com"
        assert api_client.api_key is not None
        assert api_client.timeout > 0
    
    def test_session_headers(self, api_client):
        """Test that session headers are set correctly."""
        headers = api_client.session.headers
        assert 'User-Agent' in headers
        assert 'Authorization' in headers
    
    @pytest.mark.skip(reason="Requires live API endpoint")
    def test_get_request(self, api_client):
        """Test GET request (skipped - requires live endpoint)."""
        response = api_client.get("/test")
        assert response is not None
    
    @pytest.mark.skip(reason="Requires live API endpoint")
    def test_post_request(self, api_client):
        """Test POST request (skipped - requires live endpoint)."""
        data = {'key': 'value'}
        response = api_client.post("/test", data=data)
        assert response is not None
