"""Test core functionality for {{ cookiecutter.project_name }}."""

import pytest
{% if cookiecutter.include_async %}import asyncio{% endif %}
from {{ cookiecutter.__package_name }}.core import (
    hello_world,
    {% if cookiecutter.include_async %}async_hello_world,{% endif %}
    {{ cookiecutter.__package_name.title().replace('_', '') }}Base,
    {{ cookiecutter.__package_name.title().replace('_', '') }}Error,
    ValidationError,
    ConfigurationError,
)


class Test{{ cookiecutter.__package_name.title().replace('_', '') }}Base:
    """Test the base class functionality."""
    
    def test_initialization_without_config(self):
        """Test initialization without configuration."""
        base = {{ cookiecutter.__package_name.title().replace('_', '') }}Base()
        assert base.config == {}
    
    def test_initialization_with_config(self):
        """Test initialization with configuration."""
        config = {"key": "value", "debug": True}
        base = {{ cookiecutter.__package_name.title().replace('_', '') }}Base(config)
        assert base.config == config
    
    def test_repr(self):
        """Test string representation."""
        config = {"test": True}
        base = {{ cookiecutter.__package_name.title().replace('_', '') }}Base(config)
        repr_str = repr(base)
        assert "{{ cookiecutter.__package_name.title().replace('_', '') }}Base" in repr_str
        assert "config=" in repr_str


class TestHelloWorld:
    """Test hello world functionality."""
    
    def test_hello_world_default(self):
        """Test hello world with default parameter."""
        result = hello_world()
        assert result == "Hello, World!"
    
    def test_hello_world_custom_name(self):
        """Test hello world with custom name."""
        result = hello_world("Alice")
        assert result == "Hello, Alice!"
    
    def test_hello_world_empty_string(self):
        """Test hello world with empty string."""
        result = hello_world("")
        assert result == "Hello, !"
    
    def test_hello_world_special_characters(self):
        """Test hello world with special characters."""
        result = hello_world("Test-User_123")
        assert result == "Hello, Test-User_123!"
    
    @pytest.mark.parametrize("name,expected", [
        ("Alice", "Hello, Alice!"),
        ("Bob", "Hello, Bob!"),
        ("Charlie", "Hello, Charlie!"),
        ("123", "Hello, 123!"),
        ("Test User", "Hello, Test User!"),
    ])
    def test_hello_world_parametrized(self, name, expected):
        """Test hello world with various names."""
        assert hello_world(name) == expected


{% if cookiecutter.include_async %}
class TestAsyncHelloWorld:
    """Test async hello world functionality."""
    
    @pytest.mark.asyncio
    async def test_async_hello_world_default(self):
        """Test async hello world with default parameter."""
        result = await async_hello_world()
        assert result == "Hello async, World!"
    
    @pytest.mark.asyncio
    async def test_async_hello_world_custom_name(self):
        """Test async hello world with custom name."""
        result = await async_hello_world("Alice")
        assert result == "Hello async, Alice!"
    
    @pytest.mark.asyncio
    async def test_async_hello_world_timing(self):
        """Test async hello world execution time."""
        import time
        start_time = time.time()
        result = await async_hello_world("Performance")
        end_time = time.time()
        
        assert result == "Hello async, Performance!"
        # Should take at least 0.1 seconds due to asyncio.sleep(0.1)
        assert (end_time - start_time) >= 0.1
    
    @pytest.mark.asyncio
    @pytest.mark.parametrize("name,expected", [
        ("Alice", "Hello async, Alice!"),
        ("Bob", "Hello async, Bob!"),
        ("Charlie", "Hello async, Charlie!"),
    ])
    async def test_async_hello_world_parametrized(self, name, expected):
        """Test async hello world with various names."""
        result = await async_hello_world(name)
        assert result == expected


def test_async_sync_consistency():
    """Test that async and sync versions produce consistent results."""
    name = "Consistency Test"
    sync_result = hello_world(name)
    
    async def get_async_result():
        return await async_hello_world(name)
    
    async_result = asyncio.run(get_async_result())
    
    # Results should be similar but async version has "async" in the message
    assert "Hello," in sync_result
    assert "Hello async," in async_result
    assert name in both sync_result and async_result
{% endif %}


class TestExceptions:
    """Test custom exception classes."""
    
    def test_base_error(self):
        """Test base error class."""
        error = {{ cookiecutter.__package_name.title().replace('_', '') }}Error("Test error")
        assert str(error) == "Test error"
        assert isinstance(error, Exception)
    
    def test_validation_error(self):
        """Test validation error inheritance."""
        error = ValidationError("Validation failed")
        assert str(error) == "Validation failed"
        assert isinstance(error, {{ cookiecutter.__package_name.title().replace('_', '') }}Error)
        assert isinstance(error, Exception)
    
    def test_configuration_error(self):
        """Test configuration error inheritance."""
        error = ConfigurationError("Config error")
        assert str(error) == "Config error"
        assert isinstance(error, {{ cookiecutter.__package_name.title().replace('_', '') }}Error)
        assert isinstance(error, Exception)
    
    def test_exception_with_empty_message(self):
        """Test exceptions with empty messages."""
        error = {{ cookiecutter.__package_name.title().replace('_', '') }}Error("")
        assert str(error) == ""
    
    def test_exception_raising(self):
        """Test that exceptions can be raised and caught."""
        with pytest.raises({{ cookiecutter.__package_name.title().replace('_', '') }}Error):
            raise {{ cookiecutter.__package_name.title().replace('_', '') }}Error("Test")
        
        with pytest.raises(ValidationError):
            raise ValidationError("Validation test")
        
        with pytest.raises(ConfigurationError):
            raise ConfigurationError("Config test")


class TestIntegration:
    """Integration tests for core functionality."""
    
    def test_base_class_with_hello_world(self):
        """Test base class integration with hello world function."""
        config = {"greeting_target": "Integration Test"}
        base = {{ cookiecutter.__package_name.title().replace('_', '') }}Base(config)
        
        target = base.config.get("greeting_target", "World")
        result = hello_world(target)
        
        assert result == "Hello, Integration Test!"
    
    {% if cookiecutter.include_async %}
    @pytest.mark.asyncio
    async def test_async_integration(self):
        """Test async integration."""
        config = {"async_target": "Async Integration"}
        base = {{ cookiecutter.__package_name.title().replace('_', '') }}Base(config)
        
        target = base.config.get("async_target", "World")
        result = await async_hello_world(target)
        
        assert result == "Hello async, Async Integration!"
    {% endif %}
    
    def test_error_handling_integration(self):
        """Test error handling in integration scenarios."""
        def risky_operation():
            # Simulate some operation that might fail
            raise ValidationError("Something went wrong")
        
        with pytest.raises(ValidationError) as exc_info:
            risky_operation()
        
        assert "Something went wrong" in str(exc_info.value)
        assert isinstance(exc_info.value, {{ cookiecutter.__package_name.title().replace('_', '') }}Error)


@pytest.mark.slow
class TestPerformance:
    """Performance tests for core functionality."""
    
    def test_hello_world_performance(self, benchmark):
        """Benchmark hello world function."""
        result = benchmark(hello_world, "Performance Test")
        assert result == "Hello, Performance Test!"
    
    {% if cookiecutter.include_async %}
    @pytest.mark.asyncio
    async def test_async_hello_world_performance(self):
        """Test async hello world performance."""
        import time
        
        # Test multiple async calls
        start_time = time.time()
        tasks = [async_hello_world(f"User{i}") for i in range(10)]
        results = await asyncio.gather(*tasks)
        end_time = time.time()
        
        assert len(results) == 10
        assert all("Hello async, User" in result for result in results)
        
        # All calls should complete in roughly the same time as one call
        # since they run concurrently
        assert (end_time - start_time) < 1.0  # Should be much less than 1 second
    {% endif %}
    
    def test_base_class_instantiation_performance(self, benchmark):
        """Benchmark base class instantiation."""
        config = {"test": True, "value": 42}
        
        def create_base():
            return {{ cookiecutter.__package_name.title().replace('_', '') }}Base(config)
        
        result = benchmark(create_base)
        assert result.config == config


class TestEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_hello_world_with_none(self):
        """Test hello world with None input."""
        # This should handle None gracefully
        try:
            result = hello_world(None)
            assert "None" in result
        except TypeError:
            # If it raises TypeError, that's also acceptable
            pass
    
    def test_base_class_with_none_config(self):
        """Test base class with None config."""
        base = {{ cookiecutter.__package_name.title().replace('_', '') }}Base(None)
        assert base.config == {}
    
    def test_large_string_input(self):
        """Test with very large string input."""
        large_name = "A" * 10000
        result = hello_world(large_name)
        assert result.startswith("Hello, ")
        assert result.endswith("!")
        assert large_name in result
    
    def test_unicode_input(self):
        """Test with unicode characters."""
        unicode_name = "Ñoño 测试 🚀"
        result = hello_world(unicode_name)
        assert result == f"Hello, {unicode_name}!"
    
    {% if cookiecutter.include_async %}
    @pytest.mark.asyncio
    async def test_async_exception_handling(self):
        """Test async function exception handling."""
        # Test that async function handles exceptions properly
        result = await async_hello_world("Exception Test")
        assert "Exception Test" in result
    {% endif %}