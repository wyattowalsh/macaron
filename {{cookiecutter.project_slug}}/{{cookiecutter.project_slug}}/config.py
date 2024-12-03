"""Configuration management for {{cookiecutter.project_slug}}.

This module provides a centralized configuration management system using Pydantic.
It supports:
- YAML-based configuration files
- Environment variable overrides
- Type validation and coercion
- Nested configuration structures
- Runtime configuration reloading
- Singleton configuration pattern

Example:
    >>> from {{cookiecutter.project_slug}}.config import config
    >>> print(config.settings.app_name)
    >>> config.reload()  # Reload configuration at runtime
"""
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Final, Optional, TypeVar, cast

import yaml
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

from .logging import BatchConfig, ConsoleConfig, FileConfig, LogLevel, ProgressConfig

T = TypeVar('T')


class FrozenModel(BaseModel):
    """Base model that's immutable after creation."""

    class Config:
        frozen = True
        validate_assignment = True
        extra = "forbid"
        validate_all = True


class LoggingSettings(FrozenModel):
    """Logging-specific configuration settings.
    
    Attributes:
        app_name (str): Application name used in log files
        level (LogLevel): Minimum logging level
        log_dir (Path): Directory for log file storage
        format_string (str): Log message format template
        console (ConsoleConfig): Console output settings
        file (FileConfig): File output settings
        json (FileConfig): JSON output settings
        batch (BatchConfig): Batch processing settings
        progress (ProgressConfig): Progress bar settings
        parallel (Dict[str, Any]): Parallel processing settings
    """
    app_name: str = "{{cookiecutter.project_slug}}"
    level: LogLevel = LogLevel.INFO
    log_dir: Path = Path("logs")
    format_string: str
    console: ConsoleConfig = ConsoleConfig()
    file: FileConfig = FileConfig()
    json: FileConfig = FileConfig()
    batch: BatchConfig = BatchConfig()
    progress: ProgressConfig
    parallel: Dict[str, Any] = {"max_workers": 4}

    @classmethod
    @lru_cache(maxsize=1)
    def from_dict(cls, data: Dict[str, Any]) -> "LoggingSettings":
        """Create cached settings instance."""
        return cls(**data)


class AppSettings(FrozenModel):
    """Central application settings container.
    
    This class serves as the root configuration object, containing all
    application settings in a hierarchical structure.
    
    Attributes:
        app_name (str): Application name
        version (str): Application version
        debug (bool): Debug mode flag
        logging (LoggingSettings): Logging configuration
    """
    # Application metadata
    app_name: str = "{{cookiecutter.project_slug}}"
    version: str = "0.1.0"
    debug: bool = False

    # Logging configuration
    logging: LoggingSettings

    # Add other configuration sections as needed
    # database: DatabaseSettings
    # api: APISettings
    # cache: CacheSettings
    # etc.

    class Config:
        env_prefix = "APP_"
        case_sensitive = False

    @classmethod
    @lru_cache(maxsize=1)
    def from_dict(cls, data: Dict[str, Any]) -> "AppSettings":
        """Create cached settings instance."""
        return cls(**data)


class Config:
    """Configuration management singleton.
    
    This class implements the singleton pattern for configuration management,
    ensuring a single source of truth for application settings.
    
    Methods:
        load_config: Load configuration from YAML file
        reload: Reload configuration at runtime
        settings: Access current settings
    """
    _instance: Final[Optional["Config"]] = None
    _settings: Optional[AppSettings] = None
    _config_path: Path
    _last_modified: float = 0

    def __new__(cls) -> "Config":
        """Ensure singleton instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize with default config path."""
        self._config_path = Path("config.yaml")
        if self._settings is None:
            self.load_config()

    @lru_cache(maxsize=32)
    def get_setting(self, path: str, default: T = None) -> T:
        """Get nested setting value with caching.
        
        Args:
            path: Dot-separated path to setting
            default: Default value if path not found
            
        Returns:
            Setting value or default
        """
        parts = path.split('.')
        value = self._settings
        for part in parts:
            try:
                value = getattr(value, part)
            except AttributeError:
                return default
        return cast(T, value)

    def _needs_reload(self) -> bool:
        """Check if config file has been modified."""
        try:
            mtime = self._config_path.stat().st_mtime
            return mtime > self._last_modified
        except FileNotFoundError:
            return True

    def load_config(self, config_path: Optional[Path] = None) -> None:
        """Load configuration from YAML file with validation."""
        if config_path:
            self._config_path = config_path

        if not self._needs_reload():
            return

        if not self._config_path.exists():
            raise FileNotFoundError(
                f"Config file not found: {self._config_path}")

        with open(self._config_path) as f:
            config_dict = yaml.safe_load(f)

        self._settings = AppSettings.from_dict(config_dict)
        self._last_modified = self._config_path.stat().st_mtime
        self.get_setting.cache_clear()  # Clear setting cache

    @property
    def settings(self) -> AppSettings:
        """Get current application settings.
        
        Returns:
            AppSettings: Validated configuration object
        """
        if self._settings is None:
            self.load_config()
        return self._settings

    def reload(self) -> None:
        """Reload configuration."""
        self.load_config()


# Initialize singleton configuration
config = Config()
