import datetime
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List, Optional

from rich.console import Console
from rich.panel import Panel


class ProjectSetup:
    """Handles post-generation project setup."""

    def __init__(self):
        self.console = Console()
        self.context = self.get_context_data()
        self.project_dir = Path.cwd()

    def get_context_data(self) -> Dict:
        """Get the context data from cookiecutter."""
        return {
            "author": {
                "full_name": "{{ cookiecutter.author_full_name }}",
                "email": "{{ cookiecutter.author_email }}",
                "github_username": "{{ cookiecutter.author_github_username }}",
                "pypi_username": "{{ cookiecutter.author_pypi_username }}"
            },
            "project": {
                "name": "{{ cookiecutter.project_name }}",
                "slug": "{{ cookiecutter.project_slug }}",
                "version": "{{ cookiecutter.project_version }}",
                "description": "{{ cookiecutter.project_description }}",
                "repository": "{{ cookiecutter.project_repository }}",
                "documentation": "{{ cookiecutter.project_documentation }}",
                "changelog": "{{ cookiecutter.project_changelog }}"
            },
            "python_version": "{{ cookiecutter.python_version }}",
            "license_type": "{{ cookiecutter.license_type }}"
        }

    def run_command(self,
                    command: List[str],
                    cwd: Optional[Path] = None) -> None:
        """Run a shell command."""
        try:
            subprocess.run(command,
                           cwd=cwd or self.project_dir,
                           check=True,
                           capture_output=True,
                           text=True)
        except subprocess.CalledProcessError as e:
            msg = f"Error running command {' '.join(command)}: {e.stderr}"
            self.console.print(f"[red]{msg}[/red]")
            raise RuntimeError(msg)

    def setup_git(self) -> None:
        """Initialize git repository and create initial commit."""
        try:
            self.run_command(["git", "init"])
            self.run_command(["git", "add", "."])
            author = (f"{self.context['author']['full_name']} "
                      f"<{self.context['author']['email']}>")
            self.run_command([
                "git", "commit", "-m", "Initial commit from macaron template",
                "--author", author
            ])
            self.console.print("[green]Git repository initialized[/green]")
        except Exception as e:
            self.console.print(
                f"[yellow]Warning: Could not initialize git: {str(e)}[/yellow]"
            )

    def setup_license(self) -> None:
        """Set up the project license."""
        license_type = self.context["license_type"]
        license_file = self.project_dir / "LICENSE"

        if license_type == "Not open source":
            if license_file.exists():
                license_file.unlink()
            self.console.print(
                "[yellow]No license file created - project is not open source[/yellow]"
            )
            return

        # Map license types to their file identifiers
        license_map = {
            "GNU Affero General Public License v3.0 (AGPL-3.0)": "agpl-3.0",
            "GNU General Public License v3.0 (GPL-3.0)": "gpl-3.0",
            "GNU Lesser General Public License v3.0 (LGPL-3.0)": "lgpl-3.0",
            "Mozilla Public License 2.0 (MPL-2.0)": "mpl-2.0",
            "Apache License 2.0 (Apache-2.0)": "apache-2.0",
            "MIT License (MIT)": "mit",
            "Boost Software License 1.0 (BSL-1.0)": "bsl-1.0",
            "The Unlicense": "unlicense"
        }

        license_id = license_map.get(license_type)
        if not license_id:
            self.console.print(
                f"[yellow]Warning: Unknown license type {license_type}[/yellow]"
            )
            return

        # Create a basic license file
        year = datetime.datetime.now().year
        license_content = (
            f"Copyright (c) {year} {self.context['author']['full_name']}\n\n"
            f"This project is licensed under the {license_type}.\n"
            f"For the full license text, please visit: https://choosealicense.com/licenses/{license_id}/\n"
        )
        license_file.write_text(license_content)
        self.console.print(
            f"[green]License file created ({license_type})[/green]")

    def create_virtual_environment(self) -> None:
        """Create and set up Python virtual environment."""
        try:
            venv_dir = self.project_dir / ".venv"

            # Create virtual environment
            self.run_command(["python", "-m", "venv", str(venv_dir)])

            # Install base dependencies
            pip_path = venv_dir / "bin" / "pip"
            self.run_command([str(pip_path), "install", "--upgrade", "pip"])
            self.run_command([str(pip_path), "install", "poetry"])

            self.console.print("[green]Virtual environment created[/green]")
        except Exception as e:
            self.console.print(
                f"[yellow]Warning: Virtual environment setup failed: {e}[/yellow]"
            )

    def cleanup(self) -> None:
        """Clean up temporary files and directories."""
        patterns = [
            "**/__pycache__",
            "**/*.pyc",
            "**/*.pyo",
            "**/*.pyd",
            ".Python",
            "env",
            "build",
            "develop-eggs",
            "dist",
            "downloads",
            "eggs",
            ".eggs",
            "lib",
            "lib64",
            "parts",
            "sdist",
            "var",
            "wheels",
            "*.egg-info",
            ".installed.cfg",
            "*.egg",
        ]

        for pattern in patterns:
            for path in self.project_dir.glob(pattern):
                if path.is_file():
                    path.unlink()
                elif path.is_dir():
                    shutil.rmtree(path)

    def run(self) -> None:
        """Run all post-generation tasks."""
        try:
            self.console.print(
                Panel("[bold blue]Starting project setup...[/bold blue]"))

            # Create virtual environment
            self.create_virtual_environment()

            # Set up license
            self.setup_license()

            # Initialize git repository
            self.setup_git()

            # Clean up temporary files
            self.cleanup()

            success_message = (
                "[bold green]Project setup completed![/bold green]\n"
                f"Project: {self.context['project']['name']}\n"
                f"Location: {self.project_dir}\n"
                "Next steps:\n"
                "1. cd into your project directory\n"
                "2. Activate your virtual environment\n"
                "3. Run 'poetry install' to install dependencies")
            self.console.print(Panel(success_message))

        except Exception as e:
            self.console.print(
                f"[red]Error during project setup: {str(e)}[/red]")
            raise SystemExit(1)


if __name__ == "__main__":
    setup = ProjectSetup()
    setup.run()
