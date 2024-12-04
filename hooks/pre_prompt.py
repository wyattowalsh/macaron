import os
import platform
import subprocess
import sys
from typing import Callable, Dict, List, Optional, Union

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Confirm

console = Console()


class PrerequisiteError(Exception):
    """Custom exception for prerequisite check failures."""
    pass


class SystemConfiguration:
    """Handles system configuration and validation."""

    REQUIRED_ENV_VARS = ["USER", "HOME"]
    PACKAGE_MANAGERS = {"Darwin": "brew", "Linux": "apt", "Windows": "choco"}

    def __init__(self) -> None:
        self.system: str = platform.system()
        self.package_manager: Optional[str] = self.PACKAGE_MANAGERS.get(self.system)
        self.console: Console = console

    def validate_environment(self) -> None:
        """Validates required environment variables."""
        missing_vars = [var for var in self.REQUIRED_ENV_VARS if var not in os.environ]
        if missing_vars:
            raise PrerequisiteError(
                f"Missing environment variables: {', '.join(missing_vars)}"
            )

    def get_package_manager(self) -> Optional[str]:
        """Returns the appropriate package manager for the current system."""
        if not self.package_manager:
            self.console.print(
                f"[yellow]Warning: No default package manager for "
                f"{self.system}[/yellow]"
            )
        return self.package_manager


class CommandRunner:
    """Handles command execution and package installation."""

    def __init__(self) -> None:
        self.console: Console = console

    def run_command(
        self,
        command: Union[str, List[str]],
        check: bool = True,
        shell: bool = False,
        capture_output: bool = True,
    ) -> Optional[str]:
        """Executes a command and returns the output."""
        try:
            if isinstance(command, str):
                command = command.strip().split()

            result = subprocess.run(
                command,
                stdout=subprocess.PIPE if capture_output else None,
                stderr=subprocess.PIPE if capture_output else None,
                text=True,
                check=check,
                shell=shell,
            )
            return result.stdout.strip() if capture_output else None

        except subprocess.CalledProcessError as e:
            cmd_str = " ".join(command)
            self.console.print(
                f"[red]Error executing command '{cmd_str}': {e.stderr.strip()}[/red]"
            )
        except FileNotFoundError:
            self.console.print(f"[red]Command not found: {command[0]}[/red]")
        return None


class PrerequisiteChecker:
    """Manages prerequisite checking and installation."""

    def __init__(self) -> None:
        self.system_config = SystemConfiguration()
        self.command_runner = CommandRunner()
        self.console: Console = console

    def check_and_install_prerequisites(self) -> None:
        """Checks and installs all required prerequisites."""
        prerequisites = self._get_prerequisites()

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console,
        ) as progress:
            for name, installer in prerequisites.items():
                task = progress.add_task(f"Checking {name}...", total=None)
                try:
                    self._check_and_install(name, installer)
                    progress.update(
                        task, description=f"[green]{name} is ready[/green]"
                    )
                except PrerequisiteError as e:
                    progress.update(
                        task, description=f"[red]{name} failed: {str(e)}[/red]"
                    )
                    if not Confirm.ask(f"Continue without {name}?"):
                        sys.exit(1)

    def _get_prerequisites(self) -> Dict[str, Callable[[], bool]]:
        """Returns a dictionary of prerequisites and their installers."""
        package_manager = self.system_config.get_package_manager()

        return {
            "git": lambda: self._install_with_package_manager(package_manager, "git"),
            "python": lambda: self._install_with_package_manager(
                package_manager, "python3"
            ),
            "pip": lambda: self._install_with_package_manager(
                package_manager, "python3-pip"
            ),
            "poetry": self._install_poetry,
            "docker": lambda: self._install_with_package_manager(
                package_manager, "docker"
            ),
        }

    def _check_and_install(self, name: str, installer: Callable[[], bool]) -> None:
        """Checks if a prerequisite is installed and installs it if needed."""
        if not self._is_installed(name):
            self.console.print(f"[yellow]Installing {name}...[/yellow]")
            if not installer():
                raise PrerequisiteError(f"Failed to install {name}")

    def _is_installed(self, command: str) -> bool:
        """Checks if a command is available."""
        which_cmd = "which" if platform.system() != "Windows" else "where"
        return (
            self.command_runner.run_command([which_cmd, command], check=False)
            is not None
        )

    def _install_with_package_manager(
        self, manager: Optional[str], package: str
    ) -> bool:
        """Installs a package using the system's package manager."""
        if not manager:
            self.console.print(
                f"[red]No package manager available to install {package}[/red]"
            )
            return False

        commands = {
            "brew": ["brew", "install"],
            "apt": ["sudo", "apt-get", "install", "-y"],
            "choco": ["choco", "install", "-y"],
        }

        if manager not in commands:
            self.console.print(f"[red]Unsupported package manager: {manager}[/red]")
            return False

        return (
            self.command_runner.run_command([*commands[manager], package], shell=False)
            is not None
        )

    def _install_poetry(self) -> bool:
        """Installs Poetry using the official installer."""
        return (
            self.command_runner.run_command(
                "curl -sSL https://install.python-poetry.org | python3 -",
                shell=True,
            )
            is not None
        )


def main() -> None:
    """Main function to run prerequisite checks."""
    try:
        checker = PrerequisiteChecker()
        checker.system_config.validate_environment()
        checker.check_and_install_prerequisites()
        console.print(
            "[green]All prerequisites are installed successfully![/green]"
        )
    except PrerequisiteError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)
    except KeyboardInterrupt:
        console.print("\n[yellow]Setup interrupted by user[/yellow]")
        sys.exit(1)


if __name__ == "__main__":
    main()