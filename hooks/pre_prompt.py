"""macaron/hooks/pre_prompt.py

Ensures proper libraries are installed if possible:
- pipx
- pyenv
- poetry
- make
- brew (dependency for macOS/Linux)
"""

import platform
import subprocess
import sys
from typing import Callable, Dict

from loguru import logger
from rich.console import Console

console = Console()


def run_command(command, check=True, shell=False):
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
        return None
    except FileNotFoundError:
        logger.error(f"Command '{' '.join(command)}' not found.")
        return None


def check_brew() -> bool:
    """Checks if Homebrew is installed, and installs it if not."""
    if run_command(['brew', '--version']):
        logger.info("brew is installed.")
        return True
    logger.warning("brew is not installed.")
    console.print("[bold yellow]Installing Homebrew...[/bold yellow]")
    if platform.system() in ['Darwin', 'Linux']:
        return bool(
            run_command([
                '/bin/bash', '-c',
                '"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
            ],
                        shell=True))
    logger.error("brew is not supported on Windows.")
    return False


def check_pipx() -> bool:
    """Checks if pipx is installed, and installs it if not."""
    if run_command(['pipx', '--version']):
        logger.info("pipx is installed.")
        return True
    logger.warning("pipx is not installed.")
    console.print("[bold yellow]Installing pipx...[/bold yellow]")
    return bool(
        run_command(['python3', '-m', 'pip', 'install', '--user', 'pipx'])
        and run_command(['python3', '-m', 'pipx', 'ensurepath']))


def check_pyenv() -> bool:
    """Checks if pyenv is installed, and installs it if not."""
    if run_command(['pyenv', '--version']):
        logger.info("pyenv is installed.")
        return True
    logger.warning("pyenv is not installed.")
    console.print("[bold yellow]Installing pyenv...[/bold yellow]")
    if platform.system() == 'Darwin':
        return bool(run_command(['brew', 'install', 'pyenv']))
    elif platform.system() == 'Linux':
        return bool(run_command(['sudo', 'apt-get', 'install', '-y', 'pyenv']))
    logger.error("pyenv installation on Windows must be done manually.")
    console.print(
        "[bold red]Please install pyenv manually using pyenv-win: https://github.com/pyenv-win/pyenv-win[/bold red]"
    )
    return False


def check_poetry() -> bool:
    """Checks if poetry is installed, and installs it if not."""
    if run_command(['poetry', '--version']):
        logger.info("poetry is installed.")
        return True
    logger.warning("poetry is not installed.")
    console.print("[bold yellow]Installing poetry...[/bold yellow]")
    return bool(run_command(['pipx', 'install', 'poetry']))


def check_make() -> bool:
    """Checks if make is installed, and installs it if not."""
    if run_command(['make', '--version']):
        logger.info("make is installed.")
        return True
    logger.warning("make is not installed.")
    console.print("[bold yellow]Installing make...[/bold yellow]")
    if platform.system() == 'Darwin':
        return bool(run_command(['brew', 'install', 'make']))
    elif platform.system() == 'Linux':
        return bool(run_command(['sudo', 'apt-get', 'install', '-y', 'make']))
    logger.error("make installation on Windows must be done manually.")
    console.print(
        "[bold red]Please install make manually using MSYS2 or other tools: https://www.msys2.org/[/bold red]"
    )
    return False


def check_prereqs():
    prereq_checks: Dict[str, Callable[[], bool]] = {
        "brew": check_brew,
        "pipx": check_pipx,
        "pyenv": check_pyenv,
        "poetry": check_poetry,
        "make": check_make
    }

    all_installed = True
    for prereq, check_func in prereq_checks.items():
        if not check_func():
            console.print(
                f"[bold red]{prereq} installation failed or was not found.[/bold red]"
            )
            all_installed = False

    if all_installed:
        console.print(
            "[bold green]All prerequisites are installed.[/bold green]")
    else:
        console.print(
            "[bold yellow]Some prerequisites were not installed. Please install them manually if needed.[/bold yellow]"
        )
        sys.exit(1)


if __name__ == "__main__":
    check_prereqs()
