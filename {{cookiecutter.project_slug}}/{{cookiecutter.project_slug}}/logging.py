"""{{cookiecutter.project_slug}}/logging.py

custom logger definition using Loguru + Rich
"""
from loguru import logger
from rich.console import Console
from rich.logging import RichHandler

# define logging format
LOGGING_FORMAT = ("<green>{time:YYYY-MM-DD at HH:mm:ss.SSS}</green> | "
                  "<level>{level: <8}</level> | "
                  "<cyan>{module}</cyan> | "
                  "<cyan>{function}</cyan> | "
                  "<cyan>{line}</cyan> | "
                  "PID: <cyan>{process}</cyan> | "
                  "TID: <cyan>{thread}</cyan> | "
                  "<level>{message}</level>")

# create logger
# remove default logger
logger.remove()
# add a console logger
console = Console()
logger.add(
    sink=RichHandler(console=console, show_time=True, show_path=True),
    level="INFO",
    format=LOGGING_FORMAT,
    colorize=True,
    backtrace=True,
    diagnose=True,
)
# add a file logger
logger.add(
    sink="logs/{{cookiecutter.project_slug}}.log",
    level="DEBUG",
    format=LOGGING_FORMAT,
    colorize=True,
    backtrace=True,
    diagnose=True,
    rotation="00:00",
    retention="7 days",
)
# add a structured file logger
logger.add(
    sink="logs/{{cookiecutter.project_slug}}.json",
    level="DEBUG",
    format=LOGGING_FORMAT,
    colorize=True,
    backtrace=True,
    diagnose=True,
    rotation="00:00",
    retention="7 days",
)
