import os
import sys
import platform
import subprocess
from typing import Dict, Callable, Optional
from cookiecutter.utils import simple_filter
from loguru import logger
from rich.console import Console
from pathlib import Path

console = Console()

# Check for required environment variables
required_env_vars = ["USER", "HOME"]
missing_vars = [var for var in required_env_vars if var not in os.environ]
if missing_vars:
    console.print(
        f"[bold red]ERROR: Missing environment variables: {', '.join(missing_vars)}[/bold red]"
    )
    sys.exit(1)


# Define a local Jinja2 filter
@simple_filter
def slugify(value: str) -> str:
    import re

    value = value.lower()
    value = re.sub(r"[\s_]+", "-", value)
    value = re.sub(r"[^a-z0-9\-]", "", value)
    return value


def run_command(command: list,
                check: bool = True,
                shell: bool = False) -> Optional[str]:
    """Runs a command and returns the output or None if failed."""
    try:
        result = subprocess.run(command,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True,
                                check=check,
                                shell=shell)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logger.error(
            f"Command '{' '.join(command)}' failed: {e.stderr.strip()}")
    except FileNotFoundError:
        logger.error(f"Command '{' '.join(command)}' not found.")
    return None


def install_package(manager: str, package: str) -> bool:
    """Attempts to install a package using the specified package manager."""
    console.print(
        f"[bold yellow]Installing {package} with {manager}...[/bold yellow]")
    if manager == "brew":
        return bool(run_command(["brew", "install", package]))
    elif manager == "pipx":
        return bool(run_command(["pipx", "install", package]))
    elif manager == "apt":
        return bool(run_command(["sudo", "apt-get", "install", "-y", package]))
    else:
        logger.error(f"Package manager '{manager}' is not supported.")
        return False


def check_and_install(command: str, install_func: Callable[[], bool]) -> bool:
    """Checks if a command exists, and runs install_func if it doesn't."""
    if run_command([command, "--version"]):
        logger.info(f"{command} is installed.")
        return True
    logger.warning(f"{command} is not installed.")
    return install_func()


def check_prereqs():
    success = True
    system_platform = platform.system()

    # Determine the package manager based on the OS
    if system_platform == "Darwin":
        package_manager = "brew"
    elif system_platform == "Linux":
        package_manager = "apt"
    else:
        logger.error(
            "Unsupported operating system for automatic installation.")
        package_manager = None

    # Define installation functions
    def install_brew() -> bool:
        if system_platform == "Darwin":
            return run_command(
                [
                    "/bin/bash",
                    "-c",
                    '"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
                ],
                shell=True,
            ) is not None
        return False

    def install_pipx() -> bool:
        return run_command(
            [sys.executable, "-m", "pip", "install", "--user",
             "pipx"]) is not None

    # Check and install prerequisites
    prerequisites = [
        ("brew", install_brew),
        ("pipx", install_pipx),
        (
            "pyenv",
            lambda: install_package(package_manager, "pyenv")
            if package_manager else False,
        ),
        ("poetry", lambda: install_package("pipx", "poetry")),
        (
            "make",
            lambda: install_package(package_manager, "make")
            if package_manager else False,
        ),
    ]

    for cmd, install_func in prerequisites:
        if not check_and_install(cmd, install_func):
            console.print(
                f"[bold red]{cmd} installation failed or was not found.[/bold red]"
            )
            success = False

    if success:
        console.print(
            "[bold green]All prerequisites are installed.[/bold green]")
    else:
        console.print(
            "[bold yellow]Some prerequisites were not installed. Please install them manually if needed.[/bold yellow]"
        )
        sys.exit(1)


if __name__ == "__main__":
    check_prereqs()
