"""Test configuration module for {{ cookiecutter.project_name }}."""

import pytest
from {{ cookiecutter.__package_name }}.config import Config, get_config, load_config_from_file
import tempfile
import os
from pathlib import Path


def test_config_defaults():
    """Test default configuration values."""
    config = Config()
    
    assert config.app_name == "{{ cookiecutter.project_name }}"
    assert config.version == "{{ cookiecutter.project_version }}"
    assert config.debug is False
    assert config.environment == "development"
    assert config.log_level == "INFO"
    assert config.max_workers == 4
    assert config.timeout == 30.0


def test_config_validation():
    """Test configuration validation."""
    # Test valid environment
    config = Config(environment="production")
    assert config.environment == "production"
    
    # Test invalid environment
    with pytest.raises(ValueError, match="Environment must be one of"):
        Config(environment="invalid")


def test_config_log_level_validation():
    """Test log level validation."""
    # Test valid log level
    config = Config(log_level="DEBUG")
    assert config.log_level == "DEBUG"
    
    # Test invalid log level
    with pytest.raises(ValueError, match="Log level must be one of"):
        Config(log_level="INVALID")


{% if cookiecutter.include_api %}
def test_api_config():
    """Test API-specific configuration."""
    config = Config(api_host="0.0.0.0", api_port=8080)
    
    assert config.api_host == "0.0.0.0"
    assert config.api_port == 8080
    assert config.api_workers == 1
    assert config.api_reload is False


def test_api_port_validation():
    """Test API port validation."""
    # Test valid port
    config = Config(api_port=8080)
    assert config.api_port == 8080
    
    # Test invalid port
    with pytest.raises(ValueError, match="API port must be between"):
        Config(api_port=0)
    
    with pytest.raises(ValueError, match="API port must be between"):
        Config(api_port=70000)
{% endif %}


def test_environment_checks():
    """Test environment check methods."""
    dev_config = Config(environment="development")
    prod_config = Config(environment="production")
    test_config = Config(environment="testing")
    
    assert dev_config.is_development() is True
    assert dev_config.is_production() is False
    assert dev_config.is_testing() is False
    
    assert prod_config.is_development() is False
    assert prod_config.is_production() is True
    assert prod_config.is_testing() is False
    
    assert test_config.is_development() is False
    assert test_config.is_production() is False
    assert test_config.is_testing() is True


def test_load_config_from_yaml_file():
    """Test loading configuration from YAML file."""
    config_data = {
        "app_name": "Test App",
        "debug": True,
        "log_level": "DEBUG"
    }
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        import yaml
        yaml.dump(config_data, f)
        temp_path = f.name
    
    try:
        loaded_data = load_config_from_file(temp_path)
        assert loaded_data == config_data
    finally:
        os.unlink(temp_path)


def test_load_config_from_json_file():
    """Test loading configuration from JSON file."""
    config_data = {
        "app_name": "Test App",
        "debug": True,
        "log_level": "DEBUG"
    }
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        import json
        json.dump(config_data, f)
        temp_path = f.name
    
    try:
        loaded_data = load_config_from_file(temp_path)
        assert loaded_data == config_data
    finally:
        os.unlink(temp_path)


def test_load_config_nonexistent_file():
    """Test loading configuration from non-existent file."""
    with pytest.raises(FileNotFoundError):
        load_config_from_file("nonexistent.yaml")


def test_load_config_unsupported_format():
    """Test loading configuration from unsupported file format."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("some content")
        temp_path = f.name
    
    try:
        with pytest.raises(ValueError, match="Unsupported configuration file format"):
            load_config_from_file(temp_path)
    finally:
        os.unlink(temp_path)


def test_get_config_with_overrides():
    """Test get_config function with overrides."""
    config = get_config(debug=True, log_level="DEBUG")
    
    assert config.debug is True
    assert config.log_level == "DEBUG"


def test_get_config_with_file():
    """Test get_config function with configuration file."""
    config_data = {
        "app_name": "File Test App",
        "environment": "testing"
    }
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        import yaml
        yaml.dump(config_data, f)
        temp_path = f.name
    
    try:
        config = get_config(config_file=temp_path)
        assert config.app_name == "File Test App"
        assert config.environment == "testing"
    finally:
        os.unlink(temp_path)


@pytest.mark.parametrize("env_value,expected", [
    ("development", "development"),
    ("staging", "staging"),
    ("production", "production"),
    ("testing", "testing"),
])
def test_environment_values(env_value, expected):
    """Test various environment values."""
    config = Config(environment=env_value)
    assert config.environment == expected


@pytest.mark.parametrize("log_level,expected", [
    ("DEBUG", "DEBUG"),
    ("info", "INFO"),
    ("Warning", "WARNING"),
    ("ERROR", "ERROR"),
    ("critical", "CRITICAL"),
])
def test_log_level_normalization(log_level, expected):
    """Test log level case normalization."""
    config = Config(log_level=log_level)
    assert config.log_level == expected
