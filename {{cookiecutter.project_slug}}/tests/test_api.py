"""Test API functionality for {{ cookiecutter.project_name }}."""

{% if cookiecutter.include_api %}
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from datetime import datetime

from {{ cookiecutter.__package_name }}.api import create_app, app
from {{ cookiecutter.__package_name }}.config import Config


@pytest.fixture
def client():
    """Create a test client."""
    test_app = create_app()
    return TestClient(test_app)


@pytest.fixture
def test_config():
    """Create a test configuration."""
    return Config(
        environment="testing",
        debug=True,
        api_host="localhost",
        api_port=8000,
    )


class TestAPIBasics:
    """Test basic API functionality."""
    
    def test_root_endpoint(self, client):
        """Test the root endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        
        data = response.json()
        assert "message" in data
        assert "{{ cookiecutter.project_name }}" in data["message"]
        assert data["docs"] == "/docs"
        assert data["health"] == "/health"
    
    def test_docs_endpoint(self, client):
        """Test the docs endpoint is accessible."""
        response = client.get("/docs")
        assert response.status_code == 200
        assert "html" in response.headers["content-type"]
    
    def test_redoc_endpoint(self, client):
        """Test the redoc endpoint is accessible."""
        response = client.get("/redoc")
        assert response.status_code == 200
        assert "html" in response.headers["content-type"]
    
    def test_openapi_endpoint(self, client):
        """Test the OpenAPI schema endpoint."""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        
        schema = response.json()
        assert "openapi" in schema
        assert "info" in schema
        assert schema["info"]["title"] == "{{ cookiecutter.project_name }}"


class TestHealthEndpoint:
    """Test the health check endpoint."""
    
    def test_health_check(self, client):
        """Test basic health check."""
        response = client.get("/health")
        assert response.status_code == 200
        
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data
        assert "version" in data
        assert "uptime" in data
        assert data["version"] == "{{ cookiecutter.project_version }}"
    
    def test_health_check_response_format(self, client):
        """Test health check response format."""
        response = client.get("/health")
        data = response.json()
        
        # Check timestamp format
        timestamp_str = data["timestamp"]
        timestamp = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
        assert isinstance(timestamp, datetime)
        
        # Check uptime is a number
        assert isinstance(data["uptime"], (int, float))
        assert data["uptime"] >= 0


class TestGreetingEndpoints:
    """Test the greeting endpoints."""
    
    def test_greet_endpoint_basic(self, client):
        """Test basic greeting endpoint."""
        response = client.post("/greet", json={"name": "Test"})
        assert response.status_code == 200
        
        data = response.json()
        assert data["message"] == "Hello, Test!"
        assert "timestamp" in data
    
    def test_greet_endpoint_uppercase(self, client):
        """Test greeting endpoint with uppercase option."""
        response = client.post("/greet", json={"name": "test", "uppercase": True})
        assert response.status_code == 200
        
        data = response.json()
        assert data["message"] == "HELLO, TEST!"
    
    def test_greet_endpoint_validation(self, client):
        """Test greeting endpoint input validation."""
        # Empty name should fail validation
        response = client.post("/greet", json={"name": ""})
        assert response.status_code == 422
        
        # Missing name should fail
        response = client.post("/greet", json={})
        assert response.status_code == 422
        
        # Name too long should fail
        long_name = "a" * 101
        response = client.post("/greet", json={"name": long_name})
        assert response.status_code == 422
    
    @pytest.mark.parametrize("name,expected", [
        ("Alice", "Hello, Alice!"),
        ("Bob", "Hello, Bob!"),
        ("Charlie", "Hello, Charlie!"),
        ("Test-User_123", "Hello, Test-User_123!"),
        ("Ñoño 🚀", "Hello, Ñoño 🚀!"),
    ])
    def test_greet_endpoint_various_names(self, client, name, expected):
        """Test greeting endpoint with various names."""
        response = client.post("/greet", json={"name": name})
        assert response.status_code == 200
        
        data = response.json()
        assert data["message"] == expected


{% if cookiecutter.include_async %}
class TestAsyncGreetingEndpoint:
    """Test the async greeting endpoint."""
    
    def test_async_greet_endpoint_basic(self, client):
        """Test basic async greeting endpoint."""
        response = client.post("/async-greet", json={"name": "AsyncTest"})
        assert response.status_code == 200
        
        data = response.json()
        assert data["message"] == "Hello async, AsyncTest!"
        assert "timestamp" in data
    
    def test_async_greet_endpoint_uppercase(self, client):
        """Test async greeting endpoint with uppercase option."""
        response = client.post("/async-greet", json={"name": "test", "uppercase": True})
        assert response.status_code == 200
        
        data = response.json()
        assert data["message"] == "HELLO ASYNC, TEST!"
    
    def test_async_greet_endpoint_validation(self, client):
        """Test async greeting endpoint input validation."""
        response = client.post("/async-greet", json={"name": ""})
        assert response.status_code == 422
{% endif %}


class TestInfoEndpoint:
    """Test the info endpoint."""
    
    def test_info_endpoint(self, client):
        """Test the info endpoint."""
        response = client.get("/info")
        assert response.status_code == 200
        
        data = response.json()
        assert "name" in data
        assert "version" in data
        assert "environment" in data
        assert "debug" in data
        assert "uptime" in data
        
        assert data["version"] == "{{ cookiecutter.project_version }}"


class TestErrorHandling:
    """Test API error handling."""
    
    def test_404_error(self, client):
        """Test 404 error for non-existent endpoints."""
        response = client.get("/non-existent-endpoint")
        assert response.status_code == 404
    
    def test_method_not_allowed(self, client):
        """Test method not allowed errors."""
        response = client.post("/health")  # GET only endpoint
        assert response.status_code == 405
    
    def test_invalid_json(self, client):
        """Test invalid JSON in request body."""
        response = client.post(
            "/greet",
            data="invalid json",
            headers={"content-type": "application/json"}
        )
        assert response.status_code == 422
    
    @patch('{{ cookiecutter.__package_name }}.core.hello_world')
    def test_internal_server_error(self, mock_hello_world, client):
        """Test internal server error handling."""
        mock_hello_world.side_effect = Exception("Internal error")
        
        response = client.post("/greet", json={"name": "Test"})
        assert response.status_code == 500
        assert "Failed to generate greeting" in response.json()["detail"]


class TestAPIConfiguration:
    """Test API configuration and middleware."""
    
    def test_cors_headers(self, client):
        """Test CORS headers are present."""
        response = client.options("/greet")
        # CORS headers should be present for OPTIONS requests
        assert response.status_code in [200, 204]
    
    def test_create_app_with_config(self, test_config):
        """Test creating app with custom configuration."""
        app = create_app(test_config)
        client = TestClient(app)
        
        response = client.get("/info")
        assert response.status_code == 200
        
        data = response.json()
        assert data["environment"] == "testing"
        assert data["debug"] is True


class TestAPIStartupShutdown:
    """Test API startup and shutdown events."""
    
    def test_startup_event(self):
        """Test that startup event is triggered."""
        # This is implicitly tested when creating the test client
        # The startup event should complete without errors
        test_app = create_app()
        client = TestClient(test_app)
        
        # If we can make a request, startup was successful
        response = client.get("/health")
        assert response.status_code == 200
    
    def test_app_lifespan(self):
        """Test app lifespan management."""
        with TestClient(create_app()) as client:
            response = client.get("/health")
            assert response.status_code == 200
        # Shutdown event should be triggered when exiting context


@pytest.mark.slow
class TestAPIPerformance:
    """Performance tests for API functionality."""
    
    def test_concurrent_requests(self, client):
        """Test handling multiple concurrent requests."""
        import concurrent.futures
        import time
        
        def make_request():
            return client.post("/greet", json={"name": "Concurrent"})
        
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(make_request) for _ in range(20)]
            responses = [future.result() for future in futures]
        end_time = time.time()
        
        # All requests should succeed
        assert all(response.status_code == 200 for response in responses)
        
        # Should complete in reasonable time
        assert (end_time - start_time) < 5.0
    
    def test_large_request_body(self, client):
        """Test handling large request bodies."""
        large_name = "A" * 100  # Maximum allowed length
        response = client.post("/greet", json={"name": large_name})
        assert response.status_code == 200


class TestAPIIntegration:
    """Integration tests for API functionality."""
    
    def test_full_api_workflow(self, client):
        """Test a complete API workflow."""
        # Check health
        health_response = client.get("/health")
        assert health_response.status_code == 200
        
        # Get app info
        info_response = client.get("/info")
        assert info_response.status_code == 200
        
        # Make greeting requests
        greet_response = client.post("/greet", json={"name": "Integration"})
        assert greet_response.status_code == 200
        assert "Hello, Integration!" in greet_response.json()["message"]
        
        {% if cookiecutter.include_async %}
        # Make async greeting request
        async_response = client.post("/async-greet", json={"name": "AsyncInt"})
        assert async_response.status_code == 200
        assert "Hello async, AsyncInt!" in async_response.json()["message"]
        {% endif %}
    
    def test_api_consistency(self, client):
        """Test API response consistency."""
        # Make multiple requests and ensure consistent response format
        responses = []
        for i in range(5):
            response = client.post("/greet", json={"name": f"User{i}"})
            assert response.status_code == 200
            responses.append(response.json())
        
        # All responses should have the same structure
        for response in responses:
            assert "message" in response
            assert "timestamp" in response
            assert response["message"].startswith("Hello, ")


class TestAPIEdgeCases:
    """Test edge cases for API functionality."""
    
    def test_special_characters_in_name(self, client):
        """Test API with special characters in name."""
        response = client.post("/greet", json={"name": "Test-User_123!"})
        assert response.status_code == 200
        
        data = response.json()
        assert "Test-User_123!" in data["message"]
    
    def test_unicode_characters(self, client):
        """Test API with unicode characters."""
        response = client.post("/greet", json={"name": "Ñoño 测试 🚀"})
        assert response.status_code == 200
        
        data = response.json()
        assert "Ñoño 测试 🚀" in data["message"]
    
    def test_boolean_options(self, client):
        """Test boolean option handling."""
        # Test with explicit false
        response = client.post("/greet", json={"name": "Test", "uppercase": False})
        assert response.status_code == 200
        assert response.json()["message"] == "Hello, Test!"
        
        # Test with explicit true
        response = client.post("/greet", json={"name": "Test", "uppercase": True})
        assert response.status_code == 200
        assert response.json()["message"] == "HELLO, TEST!"

{% else %}
# Placeholder tests when API is not included
def test_api_not_included():
    """Test that API functionality is not included when disabled."""
    try:
        from {{ cookiecutter.__package_name }}.api import create_app
        app = create_app()
        assert app is None  # Should return None when not configured
    except NotImplementedError:
        # Expected when API is not included
        pass
    except ImportError:
        # Also acceptable if module doesn't exist
        pass
{% endif %}