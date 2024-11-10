# test_logging.py

import importlib
from unittest import mock

import pytest
from loguru import logger

from .logging import LOGGING_FORMAT


def test_logger_configuration():
    with mock.patch('rich.logging.RichHandler') as MockRichHandler, \
         mock.patch('rich.console.Console') as MockConsole, \
         mock.patch('loguru.logger.add') as MockLoggerAdd, \
         mock.patch('loguru.logger.remove') as MockLoggerRemove:

        # Re-import the logger module to trigger the configuration
        importlib.reload(
            importlib.import_module('.logging',
                                    package='{{cookiecutter.project_slug}}'))

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
        assert console_call_args[1]['format'] == LOGGING_FORMAT

        # Verify file logger configuration
        assert file_call_args[1][
            'sink'] == "logs/{{cookiecutter.project_slug}}.log"
        assert file_call_args[1]['level'] == "DEBUG"
        assert file_call_args[1]['format'] == LOGGING_FORMAT

        # Verify structured file logger configuration
        assert structured_file_call_args[1][
            'sink'] == "logs/{{cookiecutter.project_slug}}.json"
        assert structured_file_call_args[1]['level'] == "DEBUG"
        assert structured_file_call_args[1]['format'] == LOGGING_FORMAT
