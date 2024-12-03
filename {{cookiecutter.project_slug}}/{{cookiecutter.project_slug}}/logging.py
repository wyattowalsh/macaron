"""{{cookiecutter.project_slug}}/logging.py

Enhanced logging configuration using Loguru + Rich.

This module provides a robust logging system with:
- Multiple output formats (console, file, JSON)
- Progress bars with themes
- Performance tracking
- Batch logging
- Async logging support
- Statistics collection
- Thread-safe operations

The logging system is configured via YAML and integrates with the
application's central configuration management.
"""
import os
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from functools import partial, lru_cache
from pathlib import Path
from threading import Lock
from typing import Any, Callable, ClassVar, Dict, Iterator, List, Optional, Tuple, Union, Final, Protocol
from weakref import WeakValueDictionary

import orjson
import psutil
import yaml
from loguru import logger
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings
from rich.console import Console
from rich.logging import RichHandler
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)
from rich.style import Style
from rich.theme import Theme
from rich.traceback import Traceback

from .config import config


class LogLevel(str, Enum):
    TRACE = "TRACE"
    DEBUG = "DEBUG"
    INFO = "INFO"
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class ProgressBarStyle:
    """Custom progress bar styling configurations."""
    DEFAULT = {
        "bar_color": "cyan",
        "complete_style": Style(color="green"),
        "progress_style": Style(color="cyan"),
        "spinner_style": Style(color="yellow"),
    }

    RAINBOW = {
        "bar_color": "magenta",
        "complete_style": Style(color="green", bold=True),
        "progress_style": Style(color="rainbow"),
        "spinner_style": Style(color="cyan", bold=True),
    }


class ProgressTheme:
    """Custom progress bar themes."""
    NEON = {
        "bar_color": "bright_cyan",
        "complete_style": Style(color="bright_green", bold=True),
        "progress_style": Style(color="bright_white"),
        "spinner_style": Style(color="bright_magenta"),
        "description_style": Style(color="bright_yellow"),
    }

    MINIMAL = {
        "bar_color": "white",
        "complete_style": Style(color="grey70"),
        "progress_style": Style(color="grey50"),
        "spinner_style": Style(color="grey85"),
        "description_style": Style(color="grey74"),
    }


@dataclass
class LogStats:
    """Log statistics tracking."""
    total_messages: int = 0
    messages_by_level: Dict[str, int] = defaultdict(int)
    errors_count: int = 0
    start_time: float = time.time()
    _lock: ClassVar[Lock] = Lock()

    def update(self, level: str, is_error: bool = False):
        with self._lock:
            self.total_messages += 1
            self.messages_by_level[level] += 1
            if is_error:
                self.errors_count += 1


class StyleConfig(BaseModel):
    color: str
    bold: bool = False


class ThemeConfig(BaseModel):
    bar_color: str
    complete_style: StyleConfig
    progress_style: StyleConfig
    spinner_style: StyleConfig
    description_style: StyleConfig


class ProgressConfig(BaseModel):
    theme: str = "NEON"
    themes: Dict[str, ThemeConfig]


class ConsoleConfig(BaseModel):
    enabled: bool = True
    show_time: bool = True
    show_path: bool = True
    rich_tracebacks: bool = True
    traceback_extra_lines: int = 3
    traceback_theme: str = "monokai"


class FileConfig(BaseModel):
    enabled: bool = True
    rotation_size: str = "100 MB"
    compression: str = "zip"
    retention_days: int = 7


class BatchConfig(BaseModel):
    initial_size: int = 100
    max_size: int = 1000
    min_size: int = 10
    check_interval: int = 60
    high_load_threshold: int = 80
    low_load_threshold: int = 30


class LoggingSettings(BaseSettings):
    app_name: str = "{{cookiecutter.project_slug}}"
    level: str = "INFO"
    log_dir: str = "logs"
    format_string: str = LoggingConfig.DEFAULT_FORMAT
    console: ConsoleConfig = ConsoleConfig()
    file: FileConfig = FileConfig()
    json: FileConfig = FileConfig()
    batch: BatchConfig = BatchConfig()
    progress: ProgressConfig
    parallel: Dict[str, Any] = {"max_workers": 4}

    class Config:
        env_prefix = "LOG_"


class LoggingConfig:
    """Advanced logging configuration and management.
    
    This class handles all aspects of logging configuration and provides
    high-level logging utilities. It supports multiple output formats,
    progress tracking, and performance monitoring.
    
    Attributes:
        app_name (str): Application identifier
        log_level (LogLevel): Minimum logging level
        log_dir (Path): Log file directory
        format_string (str): Log message format
        console (Console): Rich console instance
        progress (Progress): Progress bar manager
        stats (LogStats): Logging statistics
    """
    DEFAULT_FORMAT: Final[str] = (
        "<green>{time:YYYY-MM-DD at HH:mm:ss.SSS}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{module}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "PID: <cyan>{process}</cyan> | "
        "TID: <cyan>{thread}</cyan> | "
        "<level>{message}</level>")
    MAX_BATCH_SIZE: Final[int] = 10000
    PROGRESS_CACHE_SIZE: Final[int] = 100

    def __init__(
        self,
        app_name: str,
        log_level: Union[str, LogLevel] = LogLevel.INFO,
        log_dir: Union[str, Path] = "logs",
        format_string: Optional[str] = None,
        enable_console: bool = True,
        enable_file: bool = True,
        enable_json: bool = True,
        batch_size: int = 100,
        progress_style: Dict[str, Any] = ProgressBarStyle.DEFAULT,
        max_workers: int = 4,
    ):
        self.app_name = app_name
        self.log_level = LogLevel(log_level)
        self.log_dir = Path(log_dir)
        self.format_string = format_string or self.DEFAULT_FORMAT
        self.enable_console = enable_console
        self.enable_file = enable_file
        self.enable_json = enable_json
        self.console = Console()
        self.batch_size = batch_size
        self.progress_style = progress_style
        self._log_batch = []
        self.stats = LogStats()
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self._adaptive_batch_size = batch_size
        self._last_system_check = time.time()
        self._progress_bars: WeakValueDictionary[
            int, Progress] = WeakValueDictionary()
        self._log_buffer = []
        self._flush_lock = Lock()

        # Initialize custom progress bar
        self.progress = Progress(
            SpinnerColumn(style=self.progress_style["spinner_style"]),
            TextColumn("[bold blue]{task.description}"),
            BarColumn(complete_style=self.progress_style["complete_style"],
                      finished_style=self.progress_style["complete_style"]),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
            console=self.console,
        )

        self._initialize_logging()

    @classmethod
    def from_yaml(cls, config_path: Union[str, Path]) -> "LoggingConfig":
        """Create LoggingConfig from YAML file."""
        with open(config_path) as f:
            config_dict = yaml.safe_load(f)
        settings = LoggingSettings(**config_dict["logging"])
        return cls(
            app_name=settings.app_name,
            log_level=settings.level,
            log_dir=settings.log_dir,
            format_string=settings.format_string,
            enable_console=settings.console.enabled,
            enable_file=settings.file.enabled,
            enable_json=settings.json.enabled,
            batch_size=settings.batch.initial_size,
            progress_style=settings.progress.themes[
                settings.progress.theme.lower()].dict(),
            max_workers=settings.parallel["max_workers"],
        )

    @classmethod
    def from_settings(cls) -> "LoggingConfig":
        """Create LoggingConfig from application settings."""
        settings = config.settings.logging
        return cls(
            app_name=settings.app_name,
            log_level=settings.level,
            log_dir=settings.log_dir,
            format_string=settings.format_string,
            enable_console=settings.console.enabled,
            enable_file=settings.file.enabled,
            enable_json=settings.json.enabled,
            batch_size=settings.batch.initial_size,
            progress_style=settings.progress.themes[
                settings.progress.theme.lower()].dict(),
            max_workers=settings.parallel["max_workers"],
        )

    def _initialize_logging(self) -> None:
        """Initialize logging configuration."""
        # Create log directory if it doesn't exist
        self.log_dir.mkdir(parents=True, exist_ok=True)

        # Remove default logger
        logger.remove()

        if self.enable_console:
            self._setup_console_logging()

        if self.enable_file:
            self._setup_file_logging()

        if self.enable_json:
            self._setup_json_logging()

    def _setup_console_logging(self) -> None:
        """Configure console logging."""
        logger.add(
            sink=RichHandler(
                console=self.console,
                show_time=True,
                show_path=True,
                rich_tracebacks=True,
                tracebacks_extra_lines=3,
                tracebacks_theme="monokai",
            ),
            level=self.log_level.value,
            format=self.format_string,
            colorize=True,
            backtrace=True,
            diagnose=True,
            filter=self._log_filter,
        )

    def _setup_file_logging(self) -> None:
        """Configure file logging."""
        logger.add(
            sink=str(self.log_dir / f"{self.app_name}.log"),
            level=LogLevel.DEBUG.value,
            format=self.format_string,
            rotation="100 MB",
            compression="zip",
            retention="7 days",
            backtrace=True,
            diagnose=True,
            enqueue=True,
            filter=self._log_filter,
        )

    def _setup_json_logging(self) -> None:
        """Configure JSON structured logging."""

        def json_serializer(message: Dict[str, Any]) -> str:
            """Custom JSON serializer for log records."""
            log_data = {
                "timestamp": message["time"].isoformat(),
                "level": message["level"].name,
                "message": message["message"],
                "module": message["module"],
                "function": message["function"],
                "line": message["line"],
                "process": message["process"],
                "thread": message["thread"],
                "extra": message.get("extra", {}),
            }
            return orjson.dumps(log_data).decode()

        logger.add(
            sink=str(self.log_dir / f"{self.app_name}.json"),
            level=LogLevel.DEBUG.value,
            serialize=True,
            format=json_serializer,
            rotation="100 MB",
            compression="zip",
            retention="7 days",
            enqueue=True,
            filter=self._log_filter,
        )

    def _log_filter(self, record: Dict[str, Any]) -> bool:
        """Custom log filter."""
        # Add any custom filtering logic here
        return True

    def _adjust_batch_size(self):
        """Dynamically adjust batch size based on system load.
        
        This method implements adaptive batch sizing by:
        1. Monitoring system CPU usage
        2. Reducing batch size under high load
        3. Increasing batch size under low load
        4. Staying within configured min/max limits
        """
        current_time = time.time()
        settings = self._settings.batch

        if current_time - self._last_system_check > settings.check_interval:
            system_load = psutil.cpu_percent()
            if system_load > settings.high_load_threshold:
                self._adaptive_batch_size = max(settings.min_size,
                                                self._adaptive_batch_size // 2)
            elif system_load < settings.low_load_threshold:
                self._adaptive_batch_size = min(settings.max_size,
                                                self._adaptive_batch_size * 2)
            self._last_system_check = current_time

    @contextmanager
    def temporary_level(self, level: Union[str, LogLevel]):
        """Temporarily change the log level."""
        previous_levels = {}
        for handler_id in logger._core.handlers:
            previous_levels[handler_id] = logger._core.handlers[
                handler_id]._levelno
            logger.level(handler_id, level)
        try:
            yield
        finally:
            for handler_id, level in previous_levels.items():
                logger.level(handler_id, level)

    def create_progress_bar(self,
                            total: int,
                            description: str = "Processing",
                            transient: bool = True) -> Progress:
        """Create a custom progress bar."""
        return self.progress.add_task(description,
                                      total=total,
                                      transient=transient)

    def update_progress(self, task_id: int, advance: int = 1):
        """Update progress bar."""
        self.progress.update(task_id, advance=advance)

    @contextmanager
    def progress_context(
            self,
            total: int,
            description: str = "Processing") -> Iterator[ProgressReporter]:
        """Memory-efficient progress tracking."""
        task_id = id(description)
        progress = self._progress_bars.get(task_id)

        if progress is None:
            progress = self.create_themed_progress()
            self._progress_bars[task_id] = progress

        with progress:
            task = progress.add_task(description, total=total)
            try:
                yield ProgressReporter(
                    update=lambda x=1: progress.update(task, advance=x),
                    finish=lambda: progress.remove_task(task))
            finally:
                progress.remove_task(task)

    @contextmanager
    def performance_tracking(self, operation_name: str):
        """Track performance metrics for an operation."""
        start_time = time.perf_counter()
        process = psutil.Process()
        start_memory = process.memory_info().rss / 1024 / 1024  # MB

        try:
            yield
        finally:
            end_time = time.perf_counter()
            end_memory = process.memory_info().rss / 1024 / 1024
            duration = end_time - start_time
            memory_used = end_memory - start_memory

            self.log.info(f"Performance metrics for {operation_name}:\n"
                          f"Duration: {duration:.2f}s\n"
                          f"Memory usage: {memory_used:.2f}MB")

    def batch_log(self, level: str, message: str):
        """Thread-safe batch logging with memory optimization."""
        self._log_buffer.append((level, message))

        # Use double-checked locking pattern
        if len(self._log_buffer) >= self._adaptive_batch_size:
            with self._flush_lock:
                if len(self._log_buffer) >= self._adaptive_batch_size:
                    self.flush_logs()

    def flush_logs(self):
        """Flush batched logs."""
        for level, message in self._log_batch:
            logger.log(level, message)
        self._log_batch.clear()

    async def async_log(self, level: str, message: str):
        """Async logging support."""
        await logger.complete()
        logger.log(level, message)

    def interpolate(self, message: str, **kwargs) -> str:
        """Helper for log message interpolation."""
        try:
            return message.format(**kwargs)
        except KeyError as e:
            return f"Failed to interpolate log message: {message} with args: {kwargs}. Error: {e}"

    def get_stats(self) -> Dict[str, Any]:
        """Get current logging statistics."""
        duration = time.time() - self.stats.start_time
        return {
            "total_messages": self.stats.total_messages,
            "messages_per_second": self.stats.total_messages / duration,
            "messages_by_level": dict(self.stats.messages_by_level),
            "errors_count": self.stats.errors_count,
            "uptime_seconds": duration,
        }

    @contextmanager
    def exception_group(self, group_name: str):
        """Context manager for grouped exception handling."""
        try:
            yield
        except Exception as e:
            tb = Traceback.from_exception(
                exc_type=type(e),
                exc_value=e,
                traceback=e.__traceback__,
                show_locals=True,
                theme="monokai",
            )
            self.console.print(f"\n[red]Error in {group_name}:[/red]")
            self.console.print(tb)
            raise

    def create_themed_progress(self,
                               theme: Dict[str, Any] = ProgressTheme.NEON,
                               **kwargs) -> Progress:
        """Create a progress bar with custom theme."""
        return Progress(
            SpinnerColumn(style=theme["spinner_style"]),
            TextColumn(
                "[{task.description}]",
                style=theme["description_style"],
            ),
            BarColumn(
                complete_style=theme["complete_style"],
                finished_style=theme["complete_style"],
                pulse_style=theme["progress_style"],
            ),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
            console=self.console,
            **kwargs,
        )

    def parallel_log(self,
                     messages: List[Tuple[str, str]],
                     chunk_size: int = 1000):
        """Optimized parallel logging with chunking."""

        def process_chunk(chunk: List[Tuple[str, str]]) -> None:
            with self._flush_lock:
                for level, message in chunk:
                    logger.log(level, message)
                    self.stats.update(level)

        # Process in chunks for better memory usage
        for i in range(0, len(messages), chunk_size):
            chunk = messages[i:i + chunk_size]
            self.executor.submit(process_chunk, chunk)

    @lru_cache(maxsize=32)
    def get_logger(self, name: str) -> "logger":
        """Get cached logger instance."""
        return logger.bind(context=name)

    async def alog(self, level: str, message: str):
        """Enhanced async logging with stats."""
        await logger.complete()
        logger.log(level, message)
        self.stats.update(level)


# Create default logging configuration from settings
log_config = LoggingConfig.from_settings()
log = logger.bind(context=config.settings.app_name)

# Example usage:
if __name__ == "__main__":
    # Enhanced progress bar example with theme
    items = range(100)
    progress = log_config.create_themed_progress(theme=ProgressTheme.NEON)

    with progress:
        task_id = progress.add_task("Processing", total=len(items))
        with log_config.exception_group("item_processing"):
            for item in items:
                time.sleep(0.1)
                progress.update(task_id, advance=1)

    # Performance tracking example
    with log_config.performance_tracking("heavy_operation"):
        # Do some heavy work
        time.sleep(2)

    # Batch logging example
    for i in range(1000):
        log_config.batch_log("INFO", f"Batch log message {i}")
    log_config.flush_logs()

    # Parallel logging example
    messages = [(LogLevel.INFO.value, f"Parallel message {i}")
                for i in range(100)]
    log_config.parallel_log(messages)

    # Print statistics
    stats = log_config.get_stats()
    log_config.console.print(stats)
