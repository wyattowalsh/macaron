# test_logging.py

import importlib
from unittest import mock

import pytest
from loguru import logger

from {{cookiecutter.project_slug}}.logging import LoggingConfig

import asyncio
import json
import os
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
import yaml
from rich.progress import Progress

from {{cookiecutter.project_slug}}.logging import (LogLevel, LogStats, LoggingConfig,
                                                 ProgressBarStyle, ProgressTheme)

"""Test suite for logging configuration and functionality.

This module tests all aspects of the logging system:
- Configuration loading and validation
- Log output formats and sinks
- Progress bar functionality
- Performance tracking
- Batch logging
- Thread safety
- Resource cleanup
"""

# Fixtures
@pytest.fixture
def mock_config_path(tmp_path):
    """Create a temporary config file for testing.
    
    Creates a minimal valid configuration file with all required
    logging settings for testing purposes.
    
    Args:
        tmp_path: Pytest fixture providing temporary directory
    
    Returns:
        Path: Path to temporary config file
    """
    config = {
        "logging": {
            "app_name": "test_app",
            "level": "INFO",
            "log_dir": str(tmp_path),
            "console": {"enabled": True},
            "file": {"enabled": True},
            "json": {"enabled": True},
            "batch": {"initial_size": 100},
            "progress": {
                "theme": "NEON",
                "themes": {
                    "neon": ProgressTheme.NEON,
                    "minimal": ProgressTheme.MINIMAL
                }
            },
            "parallel": {"max_workers": 2}
        }
    }
    config_path = tmp_path / "config.yaml"
    with open(config_path, "w") as f:
        yaml.dump(config, f)
    return config_path

@pytest.fixture
def logging_config(mock_config_path, tmp_path):
    """Create a LoggingConfig instance for testing."""
    with patch("rich.console.Console"), patch("rich.progress.Progress"), patch("loguru.logger"):
        config = LoggingConfig.from_yaml(mock_config_path)
        config.log_dir = tmp_path
        return config

# Basic Configuration Tests
def test_logging_config_initialization(logging_config):
    """Test basic initialization of LoggingConfig."""
    assert logging_config.app_name == "test_app"
    assert logging_config.log_level == LogLevel.INFO
    assert isinstance(logging_config.progress, Progress)

def test_logging_config_from_yaml(mock_config_path):
    """Test configuration loading from YAML."""
    config = LoggingConfig.from_yaml(mock_config_path)
    assert config.app_name == "test_app"
    assert config.log_level == LogLevel.INFO

# Logging Functionality Tests
@pytest.mark.asyncio
async def test_async_logging(logging_config):
    """Test async logging capabilities."""
    with patch("loguru.logger") as mock_logger:
        mock_logger.complete = AsyncMock()
        await logging_config.alog("INFO", "test message")
        mock_logger.complete.assert_awaited_once()
        mock_logger.log.assert_called_once_with("INFO", "test message")

def test_batch_logging(logging_config):
    """Test batch logging functionality."""
    with patch("loguru.logger") as mock_logger:
        # Test batch accumulation
        for i in range(50):
            logging_config.batch_log("INFO", f"msg {i}")
        assert len(logging_config._log_batch) == 50
        mock_logger.log.assert_not_called()

        # Test batch flush
        for i in range(51):
            logging_config.batch_log("INFO", f"msg {i}")
        assert len(logging_config._log_batch) == 0
        assert mock_logger.log.call_count > 0

# Progress Bar Tests
def test_progress_bar_features(logging_config):
    """Test progress bar creation and updates."""
    with patch("rich.progress.Progress") as MockProgress:
        # Test creation
        task_id = logging_config.create_progress_bar(100, "test")
        MockProgress.return_value.add_task.assert_called_once()

        # Test update
        logging_config.update_progress(task_id, 5)
        MockProgress.return_value.update.assert_called_once()

        # Test themed progress
        progress = logging_config.create_themed_progress(ProgressTheme.NEON)
        assert isinstance(progress, Progress)

# Performance and Resource Tests
def test_performance_tracking(logging_config):
    """Test performance tracking functionality."""
    with patch("time.perf_counter") as mock_time, \
         patch("psutil.Process") as mock_process, \
         patch("loguru.logger") as mock_logger:
        
        mock_time.side_effect = [0, 1]
        mock_process.return_value.memory_info.return_value.rss = 1024 * 1024
        
        with logging_config.performance_tracking("test_op"):
            pass
        
        mock_logger.info.assert_called_once()

# Error Handling and Edge Cases
@pytest.mark.parametrize("invalid_config", [
    {},
    {"logging": {}},
    {"logging": {"invalid": "config"}},
])
def test_invalid_config_handling(tmp_path, invalid_config):
    """Test handling of invalid configurations."""
    config_path = tmp_path / "invalid_config.yaml"
    with open(config_path, "w") as f:
        yaml.dump(invalid_config, f)
    
    with pytest.raises((KeyError, ValueError)):
        LoggingConfig.from_yaml(config_path)

def test_log_interpolation_edge_cases(logging_config):
    """Test log message interpolation with edge cases."""
    # Valid interpolation
    assert logging_config.interpolate("Hello {name}", name="World") == "Hello World"
    
    # Missing parameter
    result = logging_config.interpolate("Hello {name}")
    assert "Failed to interpolate" in result

    # Empty message
    assert logging_config.interpolate("") == ""

# Statistics and Metrics Tests
def test_logging_statistics(logging_config):
    """Test logging statistics collection and accuracy.
    
    Verifies that:
    - Message counts are accurate
    - Error counts are tracked correctly
    - Performance metrics are calculated
    
    Approach:
    1. Generate known number of logs
    2. Include specific error logs
    3. Verify all metrics match expectations
    """
    logging_config.stats.update("INFO")
    logging_config.stats.update("ERROR", is_error=True)
    
    stats = logging_config.get_stats()
    assert stats["total_messages"] == 2
    assert stats["errors_count"] == 1
    assert "messages_per_second" in stats

# Thread Safety Tests
def test_thread_safety(logging_config):
    """Test thread-safe operations."""
    import threading
    
    def log_messages():
        for _ in range(100):
            logging_config.batch_log("INFO", "test")
    
    threads = [threading.Thread(target=log_messages) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    logging_config.flush_logs()
    assert logging_config.stats.total_messages > 0

# Cleanup and Resource Management
def test_resource_cleanup(logging_config):
    """Test proper resource cleanup."""
    with patch("loguru.logger") as mock_logger:
        logging_config.flush_logs()
        del logging_config
        mock_logger.remove.assert_called()

# Integration Tests
def test_full_logging_workflow(logging_config, tmp_path):
    """Test complete logging workflow."""
    log_file = tmp_path / "test.log"
    json_file = tmp_path / "test.json"
    
    # Test different logging methods
    with patch("loguru.logger") as mock_logger:
        # Regular logging
        logging_config.batch_log("INFO", "test message")
        
        # Async logging
        asyncio.run(logging_config.alog("DEBUG", "async message"))
        
        # Progress tracking
        with logging_config.progress_context(10, "test") as task_id:
            for _ in range(10):
                logging_config.update_progress(task_id)
        
        # Performance tracking
        with logging_config.performance_tracking("test"):
            pass
        
        # Check final stats
        stats = logging_config.get_stats()
        assert stats["total_messages"] > 0

def test_logger_configuration():
    with mock.patch('rich.logging.RichHandler') as MockRichHandler, \
         mock.patch('rich.console.Console') as MockConsole, \
         mock.patch('loguru.logger.add') as MockLoggerAdd, \
         mock.patch('loguru.logger.remove') as MockLoggerRemove:

        # Re-import the logger module to trigger the configuration
        importlib.reload(
            importlib.import_module('{{cookiecutter.project_slug}}.logging'))

        # Check if logger.remove was called
        MockLoggerRemove.assert_called_once()

        # Check if logger.add was called three times (console, file, structured file)
        assert MockLoggerAdd.call_count == 3

        # Check the arguments for each call to logger.add
        console_call_args = MockLoggerAdd.call_args_list[0]
        file_call_args = MockLoggerAdd.call_args_list[1]
        structured_file_call_args = MockLoggerAdd.call_args_list[2]

        # Verify console logger configuration
        assert console_call_args[1]['sink'] == MockRichHandler.return_value
        assert console_call_args[1]['level'] == "INFO"
        assert console_call_args[1]['format'] == LoggingConfig.DEFAULT_FORMAT

        # Verify file logger configuration
        assert file_call_args[1]['sink'] == "logs/{{cookiecutter.project_slug}}.log"
        assert file_call_args[1]['level'] == "DEBUG"
        assert file_call_args[1]['format'] == LoggingConfig.DEFAULT_FORMAT

        # Verify structured file logger configuration
        assert structured_file_call_args[1]['sink'] == "logs/{{cookiecutter.project_slug}}.json"
        assert structured_file_call_args[1]['level'] == "DEBUG"
        assert structured_file_call_args[1]['format'] == LoggingConfig.DEFAULT_FORMAT
