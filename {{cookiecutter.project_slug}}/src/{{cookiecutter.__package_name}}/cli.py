"""Command-line interface for {{ cookiecutter.project_name }}.

This module provides a comprehensive CLI using Typer with:
- Rich console output
- Progress bars
- Error handling
- Configuration management
- Logging setup
"""

import sys
from pathlib import Path
from typing import Any, List, Optional

import typer
from rich import print as rprint
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.panel import Panel
from loguru import logger

from .config import Config, get_config
from .core import hello_world{% if cookiecutter.include_async %}, async_hello_world{% endif %}
{% if cookiecutter.include_async %}import asyncio{% endif %}

# Create the main Typer app
app = typer.Typer(
    name="{{ cookiecutter.project_slug }}",
    help="{{ cookiecutter.project_description }}",
    rich_markup_mode="markdown",
    no_args_is_help=True,
    context_settings={"help_option_names": ["-h", "--help"]},
)

# Create console for rich output
console = Console()


def setup_logging(config: Config) -> None:
    """Setup logging configuration."""
    logger.remove()  # Remove default logger
    
    # Add console logging
    logger.add(
        sys.stderr,
        level=config.log_level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
               "<level>{level: <8}</level> | "
               "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
               "<level>{message}</level>",
        colorize=True,
    )
    
    # Add file logging if specified
    if config.log_file:
        logger.add(
            config.log_file,
            level=config.log_level,
            format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
            rotation="10 MB",
            retention="10 days",
        )


def version_callback(show_version: bool) -> None:
    """Show version information."""
    if show_version:
        from . import __version__, __author__
        rprint(f"[bold green]{{ cookiecutter.project_name }}[/bold green] version [bold blue]{__version__}[/bold blue]")
        rprint(f"by [italic]{__author__}[/italic]")
        raise typer.Exit()


@app.callback()
def main(
    ctx: typer.Context,
    version: bool = typer.Option(False, "--version", "-v", callback=version_callback, is_eager=True, help="Show version and exit"),
    config_file: Optional[Path] = typer.Option(None, "--config", "-c", help="Configuration file path"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode"),
    verbose: bool = typer.Option(False, "--verbose", help="Enable verbose output"),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Suppress output"),
) -> None:
    """{{ cookiecutter.project_description }}
    
    A modern Python CLI application with rich features and comprehensive tooling.
    """
    # Load configuration
    config_overrides = {}
    if debug:
        config_overrides["debug"] = True
        config_overrides["log_level"] = "DEBUG"
    elif verbose:
        config_overrides["log_level"] = "INFO"
    elif quiet:
        config_overrides["log_level"] = "ERROR"
    
    config = get_config(config_file, **config_overrides)
    setup_logging(config)
    
    # Store config in context for subcommands
    ctx.obj = config
    
    logger.info(f"Starting {{ cookiecutter.project_name }} v{config.version}")


@app.command()
def hello(
    ctx: typer.Context,
    name: str = typer.Argument("World", help="Name to greet"),
    count: int = typer.Option(1, "--count", "-c", help="Number of greetings"),
    uppercase: bool = typer.Option(False, "--uppercase", "-u", help="Convert to uppercase"),
    show_progress: bool = typer.Option(False, "--progress", "-p", help="Show progress bar"),
) -> None:
    """Say hello to someone.
    
    This is a sample command that demonstrates various CLI features.
    """
    config: Config = ctx.obj
    logger.info(f"Hello command called with name='{name}', count={count}")
    
    if show_progress and count > 1:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Generating greetings...", total=count)
            for i in range(count):
                message = hello_world(name)
                if uppercase:
                    message = message.upper()
                rprint(f"[green]{i+1}.[/green] {message}")
                progress.advance(task)
    else:
        for i in range(count):
            message = hello_world(name)
            if uppercase:
                message = message.upper()
            rprint(f"[green]{i+1}.[/green] {message}")
    
    logger.info(f"Generated {count} greeting(s)")


{% if cookiecutter.include_async %}
@app.command()
def async_hello(
    ctx: typer.Context,
    name: str = typer.Argument("World", help="Name to greet"),
) -> None:
    """Say hello asynchronously.
    
    Demonstrates async functionality in CLI commands.
    """
    config: Config = ctx.obj
    logger.info(f"Async hello command called with name='{name}'")
    
    async def _async_hello():
        message = await async_hello_world(name)
        rprint(f"[green]Async:[/green] {message}")
    
    asyncio.run(_async_hello())
    logger.info("Async hello completed")
{% endif %}


@app.command()
def config_info(ctx: typer.Context) -> None:
    """Show current configuration."""
    config: Config = ctx.obj
    
    table = Table(title="Configuration")
    table.add_column("Setting", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")
    table.add_column("Source", style="yellow")
    
    # Add configuration rows
    settings = [
        ("App Name", config.app_name, "config"),
        ("Version", config.version, "config"),
        ("Environment", config.environment, "config"),
        ("Debug", str(config.debug), "config"),
        ("Log Level", config.log_level, "config"),
        {% if cookiecutter.include_api %}
        ("API Host", config.api_host, "config"),
        ("API Port", str(config.api_port), "config"),
        {% endif %}
    ]
    
    for setting, value, source in settings:
        table.add_row(setting, value, source)
    
    console.print(table)


@app.command()
def health_check(ctx: typer.Context) -> None:
    """Perform a health check of the application."""
    config: Config = ctx.obj
    logger.info("Performing health check")
    
    checks = []
    
    # Basic functionality check
    try:
        result = hello_world("Health Check")
        checks.append(("Core functionality", "✅ PASS", "green"))
    except Exception as e:
        checks.append(("Core functionality", f"❌ FAIL: {e}", "red"))
    
    {% if cookiecutter.include_async %}
    # Async functionality check
    try:
        async def _check_async():
            return await async_hello_world("Health Check")
        asyncio.run(_check_async())
        checks.append(("Async functionality", "✅ PASS", "green"))
    except Exception as e:
        checks.append(("Async functionality", f"❌ FAIL: {e}", "red"))
    {% endif %}
    
    # Configuration check
    try:
        assert config.app_name
        assert config.version
        checks.append(("Configuration", "✅ PASS", "green"))
    except Exception as e:
        checks.append(("Configuration", f"❌ FAIL: {e}", "red"))
    
    # Display results
    table = Table(title="Health Check Results")
    table.add_column("Component", style="cyan")
    table.add_column("Status", style="white")
    
    all_passed = True
    for component, status, color in checks:
        table.add_row(component, f"[{color}]{status}[/{color}]")
        if "FAIL" in status:
            all_passed = False
    
    console.print(table)
    
    if all_passed:
        rprint("\n[green]✅ All health checks passed![/green]")
        logger.info("Health check completed successfully")
    else:
        rprint("\n[red]❌ Some health checks failed![/red]")
        logger.error("Health check failed")
        raise typer.Exit(1)


def cli_main() -> None:
    """Entry point for the CLI application."""
    try:
        app()
    except KeyboardInterrupt:
        rprint("\n[yellow]Operation cancelled by user[/yellow]")
        logger.info("CLI interrupted by user")
        sys.exit(1)
    except Exception as e:
        rprint(f"\n[red]Error: {e}[/red]")
        logger.error(f"CLI error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    cli_main()