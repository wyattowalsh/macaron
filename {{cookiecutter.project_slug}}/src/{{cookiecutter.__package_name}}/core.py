"""Core functionality for {{ cookiecutter.project_name }}."""

from typing import Any, Dict, List, Optional, Union
import logging

logger = logging.getLogger(__name__)


class {{ cookiecutter.__package_name.title().replace('_', '') }}Base:
    """Base class for {{ cookiecutter.project_name }}."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None) -> None:
        """Initialize with optional configuration."""
        self.config = config or {}
        logger.info("Initialized {{ cookiecutter.__package_name.title().replace('_', '') }}Base")
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(config={self.config})>"


def hello_world(name: str = "World") -> str:
    """Simple hello world function for testing.
    
    Args:
        name: Name to greet
        
    Returns:
        Greeting message
    """
    message = f"Hello, {name}!"
    logger.debug(f"Generated greeting: {message}")
    return message


{% if cookiecutter.include_async %}
import asyncio


async def async_hello_world(name: str = "World") -> str:
    """Async version of hello world function.
    
    Args:
        name: Name to greet
        
    Returns:
        Greeting message
    """
    await asyncio.sleep(0.1)  # Simulate async work
    message = f"Hello async, {name}!"
    logger.debug(f"Generated async greeting: {message}")
    return message
{% endif %}


class {{ cookiecutter.__package_name.title().replace('_', '') }}Error(Exception):
    """Base exception for {{ cookiecutter.project_name }}."""
    pass


class ValidationError({{ cookiecutter.__package_name.title().replace('_', '') }}Error):
    """Raised when validation fails."""
    pass


class ConfigurationError({{ cookiecutter.__package_name.title().replace('_', '') }}Error):
    """Raised when configuration is invalid."""
    pass