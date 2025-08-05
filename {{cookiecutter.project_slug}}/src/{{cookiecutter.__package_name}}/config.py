"""Configuration management for {{ cookiecutter.project_name }}.

This module handles configuration loading from multiple sources:
- Environment variables
- Configuration files (YAML, JSON, TOML)
- Command line arguments
- Defaults
"""

import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

{% if cookiecutter.include_async %}
import yaml
{% endif %}
from pydantic import BaseSettings, Field, validator
from pydantic_settings import SettingsConfigDict


class Config(BaseSettings):
    """Application configuration with validation."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="{{ cookiecutter.__package_name.upper() }}_",
        case_sensitive=False,
        extra="allow"
    )
    
    # Application settings
    app_name: str = Field(default="{{ cookiecutter.project_name }}", description="Application name")
    version: str = Field(default="{{ cookiecutter.project_version }}", description="Application version")
    debug: bool = Field(default=False, description="Enable debug mode")
    environment: str = Field(default="development", description="Environment (development, staging, production)")
    
    # Logging settings
    log_level: str = Field(default="INFO", description="Logging level")
    log_format: str = Field(default="%(asctime)s - %(name)s - %(levelname)s - %(message)s", description="Log format")
    log_file: Optional[str] = Field(default=None, description="Log file path")
    
    {% if cookiecutter.include_api %}
    # API settings
    api_host: str = Field(default="localhost", description="API host")
    api_port: int = Field(default=8000, description="API port")
    api_workers: int = Field(default=1, description="Number of API workers")
    api_reload: bool = Field(default=False, description="Enable API auto-reload")
    {% endif %}
    
    {% if cookiecutter.include_database %}
    # Database settings
    database_url: str = Field(default="sqlite:///./{{ cookiecutter.project_slug }}.db", description="Database URL")
    database_echo: bool = Field(default=False, description="Enable SQL query logging")
    {% endif %}
    
    # Performance settings
    max_workers: int = Field(default=4, description="Maximum number of worker threads")
    timeout: float = Field(default=30.0, description="Default timeout in seconds")
    
    @validator("environment")
    def validate_environment(cls, v: str) -> str:
        """Validate environment value."""
        allowed = ["development", "staging", "production", "testing"]
        if v.lower() not in allowed:
            raise ValueError(f"Environment must be one of: {allowed}")
        return v.lower()
    
    @validator("log_level")
    def validate_log_level(cls, v: str) -> str:
        """Validate log level."""
        allowed = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if v.upper() not in allowed:
            raise ValueError(f"Log level must be one of: {allowed}")
        return v.upper()
    
    {% if cookiecutter.include_api %}
    @validator("api_port")
    def validate_api_port(cls, v: int) -> int:
        """Validate API port."""
        if not (1 <= v <= 65535):
            raise ValueError("API port must be between 1 and 65535")
        return v
    {% endif %}
    
    def is_development(self) -> bool:
        """Check if running in development mode."""
        return self.environment == "development"
    
    def is_production(self) -> bool:
        """Check if running in production mode."""
        return self.environment == "production"
    
    def is_testing(self) -> bool:
        """Check if running in testing mode."""
        return self.environment == "testing"


def load_config_from_file(config_path: Union[str, Path]) -> Dict[str, Any]:
    """Load configuration from a file.
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Configuration dictionary
        
    Raises:
        FileNotFoundError: If config file doesn't exist
        ValueError: If config file format is unsupported
    """
    config_path = Path(config_path)
    
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    suffix = config_path.suffix.lower()
    
    with open(config_path, "r", encoding="utf-8") as f:
        if suffix in [".yml", ".yaml"]:
            import yaml
            return yaml.safe_load(f)
        elif suffix == ".json":
            import json
            return json.load(f)
        elif suffix == ".toml":
            import tomllib if sys.version_info >= (3, 11) else tomli
            return tomllib.load(f.buffer) if sys.version_info >= (3, 11) else tomli.load(f)
        else:
            raise ValueError(f"Unsupported configuration file format: {suffix}")


def get_config(config_file: Optional[Union[str, Path]] = None, **overrides: Any) -> Config:
    """Get application configuration.
    
    Args:
        config_file: Optional path to configuration file
        **overrides: Configuration overrides
        
    Returns:
        Configured Config instance
    """
    config_data = {}
    
    # Load from file if provided
    if config_file:
        config_data.update(load_config_from_file(config_file))
    
    # Apply overrides
    config_data.update(overrides)
    
    # Create config instance (will also load from environment and .env file)
    return Config(**config_data)


# Default configuration instance
_config: Optional[Config] = None


def get_default_config() -> Config:
    """Get the default configuration instance."""
    global _config
    if _config is None:
        _config = get_config()
    return _config


def set_default_config(config: Config) -> None:
    """Set the default configuration instance."""
    global _config
    _config = config