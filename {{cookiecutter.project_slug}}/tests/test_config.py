import os
from pathlib import Path
import pytest
import yaml
from typing import Dict, Any

from {{cookiecutter.project_slug}}.config import (
    Config, 
    AppSettings,
    LoggingSettings,
    FrozenModel,
    config
)
from {{cookiecutter.project_slug}}.logging import LogLevel

# Fixtures

@pytest.fixture
def temp_config_file(tmp_path) -> Path:
    """Create a temporary valid config file."""
    config_data = {
        "app_name": "test_app",
        "version": "0.1.0",
        "debug": False,
        "logging": {
            "app_name": "test_app",
            "level": "INFO",
            "log_dir": str(tmp_path / "logs"),
            "format_string": "<green>{time}</green> | {message}",
            "console": {"enabled": True},
            "file": {"enabled": True},
            "json": {"enabled": True},
            "batch": {"initial_size": 100},
            "progress": {
                "theme": "NEON",
                "themes": {
                    "neon": {
                        "bar_color": "cyan",
                        "complete_style": {"color": "green", "bold": True},
                        "progress_style": {"color": "white"},
                        "spinner_style": {"color": "magenta"},
                        "description_style": {"color": "yellow"}
                    }
                }
            },
            "parallel": {"max_workers": 2}
        }
    }
    config_path = tmp_path / "config.yaml"
    with open(config_path, "w") as f:
        yaml.dump(config_data, f)
    return config_path

@pytest.fixture
def config_instance(temp_config_file: Path) -> Config:
    """Get a fresh config instance with temporary file."""
    Config._instance = None
    instance = Config()
    instance._config_path = temp_config_file
    instance.load_config()
    return instance

# Test Cases

def test_singleton_pattern():
    """Test Config class implements singleton pattern correctly."""
    Config._instance = None
    first = Config()
    second = Config()
    assert first is second
    assert id(first) == id(second)

def test_config_initialization(config_instance: Config):
    """Test basic configuration initialization."""
    assert config_instance._settings is not None
    assert isinstance(config_instance._settings, AppSettings)
    assert config_instance._settings.app_name == "test_app"
    assert config_instance._settings.version == "0.1.0"
    assert config_instance._settings.debug is False

def test_yaml_loading(config_instance: Config, temp_config_file: Path):
    """Test YAML configuration loading."""
    config_instance.load_config(temp_config_file)
    assert config_instance._settings is not None
    assert config_instance._settings.logging.level == LogLevel.INFO
    assert Path(config_instance._settings.logging.log_dir).name == "logs"

def test_env_var_override(config_instance: Config):
    """Test environment variable overrides."""
    os.environ["APP_DEBUG"] = "true"
    os.environ["APP_LOGGING__LEVEL"] = "DEBUG"
    
    config_instance.reload()
    
    assert config_instance.settings.debug is True
    assert config_instance.settings.logging.level == LogLevel.DEBUG
    
    # Cleanup
    del os.environ["APP_DEBUG"]
    del os.environ["APP_LOGGING__LEVEL"]

def test_settings_cache(config_instance: Config):
    """Test settings caching behavior."""
    # First access caches the value
    value1 = config_instance.get_setting("logging.level")
    value2 = config_instance.get_setting("logging.level")
    assert value1 == value2
    
    # Cache should be cleared on reload
    config_instance.reload()
    assert not hasattr(config_instance.get_setting, "cache_info") or \
           config_instance.get_setting.cache_info().hits == 0

@pytest.mark.parametrize("invalid_path", [
    "nonexistent.path",
    "logging.invalid",
    "",
    None
])
def test_invalid_setting_paths(config_instance: Config, invalid_path):
    """Test handling of invalid setting paths."""
    assert config_instance.get_setting(invalid_path, default="default") == "default"

def test_config_reload(config_instance: Config, temp_config_file: Path):
    """Test configuration reloading."""
    original_level = config_instance.settings.logging.level
    
    # Modify config file
    with open(temp_config_file) as f:
        config_data = yaml.safe_load(f)
    config_data["logging"]["level"] = "DEBUG"
    with open(temp_config_file, "w") as f:
        yaml.dump(config_data, f)
    
    config_instance.reload()
    assert config_instance.settings.logging.level == LogLevel.DEBUG
    assert config_instance.settings.logging.level != original_level

def test_missing_config_file():
    """Test handling of missing config file."""
    config = Config()
    config._config_path = Path("nonexistent.yaml")
    
    with pytest.raises(FileNotFoundError):
        config.load_config()

def test_invalid_yaml_format(tmp_path):
    """Test handling of invalid YAML format."""
    config_path = tmp_path / "invalid.yaml"
    with open(config_path, "w") as f:
        f.write("invalid: yaml: content: {")
    
    config = Config()
    config._config_path = config_path
    
    with pytest.raises(yaml.YAMLError):
        config.load_config()

def test_frozen_model_immutability():
    """Test FrozenModel immutability."""
    class TestModel(FrozenModel):
        value: str = "test"
    
    model = TestModel()
    with pytest.raises(Exception):  # Pydantic raises TypeError or ValidationError
        model.value = "changed"

def test_nested_settings_access(config_instance: Config):
    """Test accessing nested settings."""
    # Valid nested access
    assert config_instance.get_setting("logging.console.enabled") is True
    
    # Deep nesting
    assert config_instance.get_setting("logging.progress.themes.neon.bar_color") == "cyan"
    
    # Invalid nesting with default
    assert config_instance.get_setting("logging.invalid.nested.path", "default") == "default"

@pytest.mark.parametrize("setting_path,expected_type", [
    ("app_name", str),
    ("version", str),
    ("debug", bool),
    ("logging.level", LogLevel),
    ("logging.parallel.max_workers", int)
])
def test_setting_types(config_instance: Config, setting_path: str, expected_type: type):
    """Test setting value types are correct."""
    value = config_instance.get_setting(setting_path)
    assert isinstance(value, expected_type)

def test_multiple_reloads(config_instance: Config):
    """Test multiple consecutive reloads."""
    for _ in range(5):
        config_instance.reload()
        assert config_instance._settings is not None
        assert isinstance(config_instance._settings, AppSettings)

def test_concurrent_access(config_instance: Config):
    """Test concurrent access to settings."""
    import threading
    import queue
    
    results = queue.Queue()
    def worker():
        try:
            value = config_instance.get_setting("logging.level")
            results.put(("success", value))
        except Exception as e:
            results.put(("error", str(e)))
    
    threads = [threading.Thread(target=worker) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    while not results.empty():
        status, value = results.get()
        assert status == "success"
        assert value == LogLevel.INFO

def test_large_config(tmp_path):
    """Test handling of large configuration files."""
    large_config = {
        "app_name": "test_app",
        "version": "0.1.0",
        "logging": {
            "level": "INFO",
            "large_data": ["item" + str(i) for i in range(10000)]
        }
    }
    
    config_path = tmp_path / "large_config.yaml"
    with open(config_path, "w") as f:
        yaml.dump(large_config, f)
    
    config = Config()
    config._config_path = config_path
    config.load_config()
    
    assert len(config.get_setting("logging.large_data")) == 10000

def test_config_performance(config_instance: Config, benchmark):
    """Test configuration access performance."""
    def access_settings():
        return config_instance.get_setting("logging.level")
    
    result = benchmark(access_settings)
    assert result == LogLevel.INFO
