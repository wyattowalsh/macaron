"""Test CLI functionality for {{ cookiecutter.project_name }}."""

{% if cookiecutter.include_cli_example %}
import pytest
from typer.testing import CliRunner
from unittest.mock import patch, MagicMock
import tempfile
import os
from pathlib import Path

from {{ cookiecutter.__package_name }}.cli import app, cli_main, setup_logging
from {{ cookiecutter.__package_name }}.config import Config


@pytest.fixture
def runner():
    """Create a CLI test runner."""
    return CliRunner()


@pytest.fixture
def temp_config_file():
    """Create a temporary config file for testing."""
    config_data = {
        "app_name": "Test CLI App",
        "debug": True,
        "log_level": "DEBUG"
    }
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        import yaml
        yaml.dump(config_data, f)
        yield f.name
    
    os.unlink(f.name)


class TestCLIBasics:
    """Test basic CLI functionality."""
    
    def test_cli_help(self, runner):
        """Test CLI help output."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "{{ cookiecutter.project_description }}" in result.output
        assert "--version" in result.output
        assert "--config" in result.output
    
    def test_version_option(self, runner):
        """Test version option."""
        result = runner.invoke(app, ["--version"])
        assert result.exit_code == 0
        assert "{{ cookiecutter.project_name }}" in result.output
        assert "{{ cookiecutter.project_version }}" in result.output
    
    def test_debug_option(self, runner):
        """Test debug option."""
        result = runner.invoke(app, ["--debug", "hello"])
        assert result.exit_code == 0
    
    def test_quiet_option(self, runner):
        """Test quiet option."""
        result = runner.invoke(app, ["--quiet", "hello"])
        assert result.exit_code == 0
    
    def test_config_file_option(self, runner, temp_config_file):
        """Test config file option."""
        result = runner.invoke(app, ["--config", temp_config_file, "hello"])
        assert result.exit_code == 0


class TestHelloCommand:
    """Test the hello command."""
    
    def test_hello_default(self, runner):
        """Test hello command with default parameters."""
        result = runner.invoke(app, ["hello"])
        assert result.exit_code == 0
        assert "Hello, World!" in result.output
    
    def test_hello_with_name(self, runner):
        """Test hello command with custom name."""
        result = runner.invoke(app, ["hello", "Alice"])
        assert result.exit_code == 0
        assert "Hello, Alice!" in result.output
    
    def test_hello_with_count(self, runner):
        """Test hello command with count option."""
        result = runner.invoke(app, ["hello", "--count", "3"])
        assert result.exit_code == 0
        assert "1." in result.output
        assert "2." in result.output
        assert "3." in result.output
    
    def test_hello_uppercase(self, runner):
        """Test hello command with uppercase option."""
        result = runner.invoke(app, ["hello", "test", "--uppercase"])
        assert result.exit_code == 0
        assert "HELLO, TEST!" in result.output
    
    def test_hello_with_progress(self, runner):
        """Test hello command with progress bar."""
        result = runner.invoke(app, ["hello", "--count", "2", "--progress"])
        assert result.exit_code == 0
    
    @pytest.mark.parametrize("name,count", [
        ("Alice", 1),
        ("Bob", 2),
        ("Charlie", 3),
    ])
    def test_hello_parametrized(self, runner, name, count):
        """Test hello command with various parameters."""
        result = runner.invoke(app, ["hello", name, "--count", str(count)])
        assert result.exit_code == 0
        assert f"Hello, {name}!" in result.output


{% if cookiecutter.include_async %}
class TestAsyncHelloCommand:
    """Test the async hello command."""
    
    def test_async_hello_default(self, runner):
        """Test async hello command with default parameters."""
        result = runner.invoke(app, ["async-hello"])
        assert result.exit_code == 0
        assert "Hello async, World!" in result.output
    
    def test_async_hello_with_name(self, runner):
        """Test async hello command with custom name."""
        result = runner.invoke(app, ["async-hello", "AsyncTest"])
        assert result.exit_code == 0
        assert "Hello async, AsyncTest!" in result.output
{% endif %}


class TestConfigInfoCommand:
    """Test the config-info command."""
    
    def test_config_info(self, runner):
        """Test config info command."""
        result = runner.invoke(app, ["config-info"])
        assert result.exit_code == 0
        assert "Configuration" in result.output
        assert "{{ cookiecutter.project_name }}" in result.output
        assert "{{ cookiecutter.project_version }}" in result.output
    
    def test_config_info_with_custom_config(self, runner, temp_config_file):
        """Test config info with custom config file."""
        result = runner.invoke(app, ["--config", temp_config_file, "config-info"])
        assert result.exit_code == 0
        assert "Test CLI App" in result.output


class TestHealthCheckCommand:
    """Test the health-check command."""
    
    def test_health_check_success(self, runner):
        """Test successful health check."""
        result = runner.invoke(app, ["health-check"])
        assert result.exit_code == 0
        assert "Health Check Results" in result.output
        assert "✅" in result.output
    
    def test_health_check_with_debug(self, runner):
        """Test health check with debug mode."""
        result = runner.invoke(app, ["--debug", "health-check"])
        assert result.exit_code == 0


class TestCLILogging:
    """Test CLI logging functionality."""
    
    def test_setup_logging(self):
        """Test logging setup function."""
        config = Config(log_level="DEBUG", log_file=None)
        
        # Should not raise any exceptions
        setup_logging(config)
    
    def test_setup_logging_with_file(self):
        """Test logging setup with file output."""
        with tempfile.NamedTemporaryFile(delete=False) as f:
            temp_log_file = f.name
        
        try:
            config = Config(log_level="INFO", log_file=temp_log_file)
            setup_logging(config)
            
            # Log file should be created
            assert os.path.exists(temp_log_file)
        finally:
            if os.path.exists(temp_log_file):
                os.unlink(temp_log_file)


class TestCLIErrorHandling:
    """Test CLI error handling."""
    
    def test_cli_main_keyboard_interrupt(self):
        """Test CLI main function with keyboard interrupt."""
        with patch('{{ cookiecutter.__package_name }}.cli.app') as mock_app:
            mock_app.side_effect = KeyboardInterrupt()
            
            with pytest.raises(SystemExit) as exc_info:
                cli_main()
            
            assert exc_info.value.code == 1
    
    def test_cli_main_exception(self):
        """Test CLI main function with general exception."""
        with patch('{{ cookiecutter.__package_name }}.cli.app') as mock_app:
            mock_app.side_effect = Exception("Test error")
            
            with pytest.raises(SystemExit) as exc_info:
                cli_main()
            
            assert exc_info.value.code == 1
    
    def test_invalid_command(self, runner):
        """Test invalid command handling."""
        result = runner.invoke(app, ["invalid-command"])
        assert result.exit_code != 0


class TestCLIIntegration:
    """Integration tests for CLI functionality."""
    
    def test_full_workflow(self, runner, temp_config_file):
        """Test a full workflow with multiple commands."""
        # Test config info
        result = runner.invoke(app, ["--config", temp_config_file, "config-info"])
        assert result.exit_code == 0
        
        # Test hello command
        result = runner.invoke(app, ["--config", temp_config_file, "hello", "Integration"])
        assert result.exit_code == 0
        assert "Hello, Integration!" in result.output
        
        # Test health check
        result = runner.invoke(app, ["--config", temp_config_file, "health-check"])
        assert result.exit_code == 0
    
    def test_multiple_options(self, runner):
        """Test multiple CLI options together."""
        result = runner.invoke(app, [
            "--debug",
            "--verbose",
            "hello",
            "MultiTest",
            "--count", "2",
            "--uppercase"
        ])
        assert result.exit_code == 0
        assert "HELLO, MULTITEST!" in result.output


@pytest.mark.slow
class TestCLIPerformance:
    """Performance tests for CLI functionality."""
    
    def test_command_execution_time(self, runner):
        """Test command execution time."""
        import time
        
        start_time = time.time()
        result = runner.invoke(app, ["hello", "Performance"])
        end_time = time.time()
        
        assert result.exit_code == 0
        # Should complete quickly (less than 1 second)
        assert (end_time - start_time) < 1.0
    
    def test_large_count_performance(self, runner):
        """Test performance with large count."""
        result = runner.invoke(app, ["hello", "Performance", "--count", "100"])
        assert result.exit_code == 0


class TestCLIEdgeCases:
    """Test edge cases for CLI functionality."""
    
    def test_empty_name(self, runner):
        """Test hello command with empty name."""
        result = runner.invoke(app, ["hello", ""])
        assert result.exit_code == 0
        assert "Hello, !" in result.output
    
    def test_special_characters_in_name(self, runner):
        """Test hello command with special characters."""
        result = runner.invoke(app, ["hello", "Test-User_123!"])
        assert result.exit_code == 0
        assert "Hello, Test-User_123!" in result.output
    
    def test_unicode_name(self, runner):
        """Test hello command with unicode characters."""
        result = runner.invoke(app, ["hello", "Ñoño 🚀"])
        assert result.exit_code == 0
        assert "Hello, Ñoño 🚀!" in result.output
    
    def test_zero_count(self, runner):
        """Test hello command with zero count."""
        result = runner.invoke(app, ["hello", "Test", "--count", "0"])
        assert result.exit_code == 0
        # Should not output any greetings
        assert "Hello, Test!" not in result.output
    
    def test_large_count(self, runner):
        """Test hello command with very large count."""
        result = runner.invoke(app, ["hello", "Test", "--count", "1000"])
        assert result.exit_code == 0

{% else %}
# Placeholder tests when CLI is not included
def test_cli_not_included():
    """Test that CLI functionality is not included when disabled."""
    # This test ensures the template handles the case where CLI is disabled
    assert True  # Placeholder
{% endif %}