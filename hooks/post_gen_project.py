import asyncio
import json
import os
import platform
import shutil
import subprocess
import sys
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

from loguru import logger
from pydantic import BaseModel, Field
from rich.console import Console
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn

# Configure logging
logger.add("post_generation.log", rotation="1 MB", level="INFO")
console = Console()


class PostGenerationError(Exception):
    """Custom exception for post-generation failures."""
    pass


class ProjectSetup(BaseModel):
    """Project setup configuration."""
    project_slug: str
    python_version: str
    features: Dict[str, bool]
    ci_provider: str
    documentation: Dict[str, Any]
    packaging: Dict[str, bool]
    formatting: Dict[str, Any]


@dataclass
class SetupState:
    """Tracks setup progress for rollback."""
    git_initialized: bool = False
    venv_created: bool = False
    dependencies_installed: bool = False
    docker_setup: bool = False
    ci_setup: bool = False
    pre_commit_setup: bool = False
    documentation_setup: bool = False
    formatting_setup: bool = False


class AsyncCommandRunner:
    """Handles asynchronous command execution."""

    def __init__(self):
        self.console = Console()

    async def run_command(self,
                          command: List[str],
                          timeout: int = 300,
                          check: bool = True,
                          capture_output: bool = True,
                          cwd: Optional[Path] = None) -> Optional[str]:
        """Executes a command asynchronously."""
        try:
            process = await asyncio.create_subprocess_exec(
                *command,
                stdout=asyncio.subprocess.PIPE if capture_output else None,
                stderr=asyncio.subprocess.PIPE if capture_output else None,
                cwd=str(cwd) if cwd else None)

            try:
                stdout, stderr = await asyncio.wait_for(process.communicate(),
                                                        timeout=timeout)
            except asyncio.TimeoutError:
                process.kill()
                raise PostGenerationError(
                    f"Command timed out after {timeout} seconds")

            if check and process.returncode != 0:
                raise PostGenerationError(
                    f"Command failed with exit code {process.returncode}: "
                    f"{stderr.decode() if stderr else ''}")

            return stdout.decode().strip() if stdout else None

        except FileNotFoundError:
            raise PostGenerationError(f"Command not found: {command[0]}")


class ProjectSetupManager:
    """Manages project setup and initialization."""

    def __init__(self):
        self.console = Console()
        self.command_runner = AsyncCommandRunner()
        self.setup_state = SetupState()
        self._load_config()
        self.project_dir = Path.cwd()

    def _load_config(self) -> None:
        """Loads project configuration."""
        self.config = ProjectSetup(
            project_slug="{{ cookiecutter.project.slug }}",
            python_version="{{ cookiecutter.python.version }}",
            features={
                "use_git": {{cookiecutter.features.use_git}},
                "use_venv": {{cookiecutter.features.use_venv}},
                "use_docker": {{cookiecutter.features.use_docker}},
                "use_ci": {{cookiecutter.features.use_ci}},
                "use_pre_commit": {{cookiecutter.features.use_pre_commit}},
                "use_dependabot": {{cookiecutter.features.use_dependabot}}
            },
            ci_provider="{{ cookiecutter.features.ci_provider }}",
            documentation={
                "enabled": {{cookiecutter.documentation.enabled}},
                "type": "{{ cookiecutter.documentation.type }}",
                "hosting": "{{ cookiecutter.documentation.hosting }}"
            },
            packaging={
                "use_poetry": {{cookiecutter.packaging.use_poetry}},
                "use_setuptools": {{cookiecutter.packaging.use_setuptools}},
                "publish_to_pypi": {{cookiecutter.packaging.publish_to_pypi}}
            },
            formatting={
                "line_length": {{cookiecutter.formatting.line_length}},
                "quotes": "{{ cookiecutter.formatting.quotes }}",
                "line_endings": "{{ cookiecutter.formatting.line_endings }}"
            })

    @contextmanager
    def _progress_tracker(self, total: int) -> Progress:
        """Creates a progress tracker context."""
        progress = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=self.console)
        try:
            with progress:
                yield progress
        finally:
            progress.stop()

    async def init_git(self, progress: Progress, task_id: int) -> None:
        """Initializes git repository with error handling."""
        try:
            await self.command_runner.run_command(["git", "init"])

            # Configure git
            await self.command_runner.run_command(
                ["git", "config", "core.autocrlf", "input"])

            # Create .gitignore if it doesn't exist
            gitignore = self.project_dir / ".gitignore"
            if not gitignore.exists():
                gitignore.write_text(self._get_gitignore_content())

            await self.command_runner.run_command(["git", "add", "."])
            await self.command_runner.run_command(
                ["git", "commit", "-m", "Initial commit"])
            self.setup_state.git_initialized = True
            progress.update(task_id, advance=1)
        except PostGenerationError as e:
            logger.error(f"Git initialization failed: {str(e)}")
            await self._rollback()
            raise

    def _get_gitignore_content(self) -> str:
        """Returns content for .gitignore file."""
        return """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Testing
.coverage
htmlcov/
.tox/
.pytest_cache/

# Documentation
docs/_build/
site/

# Misc
.DS_Store
"""

    async def setup_python_env(self, progress: Progress, task_id: int) -> None:
        """Sets up Python environment and dependencies."""
        try:
            if self.config.packaging["use_poetry"]:
                await self._setup_poetry()
            else:
                await self._setup_venv()
            progress.update(task_id, advance=1)
        except PostGenerationError as e:
            logger.error(f"Python environment setup failed: {str(e)}")
            await self._rollback()
            raise

    async def _setup_poetry(self) -> None:
        """Sets up Poetry for dependency management."""
        try:
            # Install poetry if not available
            await self.command_runner.run_command([
                "curl", "-sSL", "https://install.python-poetry.org", "-o",
                "install-poetry.py"
            ])
            await self.command_runner.run_command(
                [sys.executable, "install-poetry.py"])
            os.unlink("install-poetry.py")

            # Configure poetry
            await self.command_runner.run_command(
                ["poetry", "config", "virtualenvs.in-project", "true"])
            await self.command_runner.run_command(["poetry", "install"])
            self.setup_state.dependencies_installed = True
        except PostGenerationError as e:
            raise PostGenerationError(f"Poetry setup failed: {str(e)}")

    async def _setup_venv(self) -> None:
        """Creates and configures virtual environment."""
        venv_dir = self.project_dir / "venv"
        try:
            await self.command_runner.run_command(
                [sys.executable, "-m", "venv",
                 str(venv_dir)])
            self.setup_state.venv_created = True

            # Install dependencies
            pip_executable = venv_dir / ("Scripts" if platform.system()
                                         == "Windows" else "bin") / "pip"

            await self.command_runner.run_command(
                [str(pip_executable), "install", "-U", "pip"])

            requirements_file = self.project_dir / "requirements.txt"
            if requirements_file.exists():
                await self.command_runner.run_command([
                    str(pip_executable), "install", "-r",
                    str(requirements_file)
                ])
            self.setup_state.dependencies_installed = True
        except PostGenerationError as e:
            raise PostGenerationError(
                f"Virtual environment setup failed: {str(e)}")

    async def setup_docker(self, progress: Progress, task_id: int) -> None:
        """Sets up Docker configuration."""
        try:
            if self.config.features["use_docker"]:
                dockerfile = self.project_dir / "Dockerfile"
                docker_compose = self.project_dir / "docker-compose.yml"

                # Create Dockerfile
                dockerfile.write_text(self._get_dockerfile_content())

                # Create docker-compose.yml
                docker_compose.write_text(self._get_docker_compose_content())

                self.setup_state.docker_setup = True
                progress.update(task_id, advance=1)
        except Exception as e:
            logger.error(f"Docker setup failed: {str(e)}")
            await self._rollback()
            raise PostGenerationError(f"Failed to setup Docker: {str(e)}")

    def _get_dockerfile_content(self) -> str:
        """Returns content for Dockerfile."""
        return f"""
FROM python:{self.config.python_version}-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
"""

    def _get_docker_compose_content(self) -> str:
        """Returns content for docker-compose.yml."""
        return """
version: '3.8'

services:
  app:
    build: .
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      - PYTHONUNBUFFERED=1
"""

    async def setup_ci(self, progress: Progress, task_id: int) -> None:
        """Sets up CI configuration."""
        try:
            if self.config.features["use_ci"]:
                if self.config.ci_provider == "github-actions":
                    await self._setup_github_actions()
                elif self.config.ci_provider == "gitlab-ci":
                    await self._setup_gitlab_ci()

                self.setup_state.ci_setup = True
                progress.update(task_id, advance=1)
        except Exception as e:
            logger.error(f"CI setup failed: {str(e)}")
            await self._rollback()
            raise PostGenerationError(f"Failed to setup CI: {str(e)}")

    async def _setup_github_actions(self) -> None:
        """Sets up GitHub Actions workflows."""
        workflows_dir = self.project_dir / ".github" / "workflows"
        workflows_dir.mkdir(parents=True, exist_ok=True)

        # Create CI workflow
        ci_workflow = workflows_dir / "ci.yml"
        ci_workflow.write_text(self._get_github_actions_ci_content())

        # Create dependabot config if enabled
        if self.config.features["use_dependabot"]:
            dependabot_config = self.project_dir / ".github" / "dependabot.yml"
            dependabot_config.write_text(self._get_dependabot_content())

    def _get_github_actions_ci_content(self) -> str:
        """Returns content for GitHub Actions CI workflow."""
        return f"""
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["{self.config.python_version}"]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{{{ matrix.python-version }}}}
      uses: actions/setup-python@v2
      with:
        python-version: ${{{{ matrix.python-version }}}}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest
"""

    def _get_dependabot_content(self) -> str:
        """Returns content for dependabot.yml."""
        return """
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
"""

    async def _setup_gitlab_ci(self) -> None:
        """Sets up GitLab CI configuration."""
        gitlab_ci = self.project_dir / ".gitlab-ci.yml"
        gitlab_ci.write_text(self._get_gitlab_ci_content())

    def _get_gitlab_ci_content(self) -> str:
        """Returns content for .gitlab-ci.yml."""
        return f"""
image: python:{self.config.python_version}

stages:
  - test
  - deploy

before_script:
  - python -V
  - pip install -r requirements.txt

test:
  stage: test
  script:
    - pytest
  only:
    - main
    - merge_requests
"""

    async def setup_documentation(self, progress: Progress,
                                  task_id: int) -> None:
        """Sets up project documentation."""
        try:
            if self.config.documentation["enabled"]:
                if self.config.documentation["type"] == "sphinx":
                    await self._setup_sphinx()
                elif self.config.documentation["type"] == "mkdocs":
                    await self._setup_mkdocs()

                self.setup_state.documentation_setup = True
                progress.update(task_id, advance=1)
        except Exception as e:
            logger.error(f"Documentation setup failed: {str(e)}")
            await self._rollback()
            raise PostGenerationError(
                f"Failed to setup documentation: {str(e)}")

    async def _setup_sphinx(self) -> None:
        """Sets up Sphinx documentation."""
        docs_dir = self.project_dir / "docs"
        docs_dir.mkdir(exist_ok=True)

        # Run sphinx-quickstart
        await self.command_runner.run_command([
            "sphinx-quickstart", "-q", "-p", self.config.project_slug, "-a",
            "{{ cookiecutter.author.full_name }}", "-v",
            "{{ cookiecutter.project.version }}", "-r",
            "{{ cookiecutter.project.version }}", "-l", "en", "--ext-autodoc",
            "--ext-viewcode", "--ext-napoleon", "--makefile", "--batchfile",
            str(docs_dir)
        ])

        # Update conf.py with theme and extensions
        conf_py = docs_dir / "source" / "conf.py"
        conf_content = conf_py.read_text()
        conf_content = conf_content.replace("html_theme = 'alabaster'",
                                            "html_theme = 'sphinx_rtd_theme'")
        conf_content = conf_content.replace(
            "extensions = [",
            "extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', "
            "'sphinx.ext.napoleon', 'sphinx_rtd_theme',")
        conf_py.write_text(conf_content)

    async def _setup_mkdocs(self) -> None:
        """Sets up MkDocs documentation."""
        mkdocs_yml = self.project_dir / "mkdocs.yml"
        mkdocs_yml.write_text(self._get_mkdocs_content())

        # Create docs directory and index
        docs_dir = self.project_dir / "docs"
        docs_dir.mkdir(exist_ok=True)
        index_md = docs_dir / "index.md"
        index_md.write_text(
            f"# {self.config.project_slug}\n\nWelcome to the documentation.")

    def _get_mkdocs_content(self) -> str:
        """Returns content for mkdocs.yml."""
        return f"""
site_name: {self.config.project_slug}
theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - toc.integrate
    - search.suggest
    - search.highlight
    - content.tabs.link
    - content.code.annotation
    - content.code.copy
  language: en
  palette:
    - scheme: default
      toggle:
        icon: material/toggle-switch-off-outline
        name: Switch to dark mode
      primary: teal
      accent: purple
    - scheme: slate
      toggle:
        icon: material/toggle-switch
        name: Switch to light mode
      primary: teal
      accent: lime

plugins:
  - search
  - mkdocstrings

markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - admonition
  - pymdownx.arithmatex:
      generic: true
  - footnotes
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.mark
"""

    async def setup_formatting(self, progress: Progress, task_id: int) -> None:
        """Sets up code formatting tools."""
        try:
            # Create .editorconfig
            editorconfig = self.project_dir / ".editorconfig"
            editorconfig.write_text(self._get_editorconfig_content())

            if self.config.features["use_pre_commit"]:
                # Create pre-commit config
                pre_commit_config = self.project_dir / ".pre-commit-config.yaml"
                pre_commit_config.write_text(
                    self._get_pre_commit_config_content())

                # Install pre-commit hooks
                await self.command_runner.run_command(
                    ["pre-commit", "install"])

            self.setup_state.formatting_setup = True
            progress.update(task_id, advance=1)
        except Exception as e:
            logger.error(f"Formatting setup failed: {str(e)}")
            await self._rollback()
            raise PostGenerationError(f"Failed to setup formatting: {str(e)}")

    def _get_editorconfig_content(self) -> str:
        """Returns content for .editorconfig."""
        return f"""
root = true

[*]
end_of_line = {self.config.formatting["line_endings"].replace("\\\\", "")}
insert_final_newline = true
trim_trailing_whitespace = true
charset = utf-8

[*.{{py,rst,txt}}]
indent_style = space
indent_size = 4
max_line_length = {self.config.formatting["line_length"]}

[*.{{yml,yaml,json,toml}}]
indent_style = space
indent_size = 2
"""

    def _get_pre_commit_config_content(self) -> str:
        """Returns content for .pre-commit-config.yaml."""
        return f"""
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files

-   repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
    -   id: black
        args: [--line-length, "{self.config.formatting["line_length"]}"]

-   repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
    -   id: isort
        args: ["--profile", "black", "--line-length", "{self.config.formatting["line_length"]}"]

-   repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
    -   id: flake8
        args: ["--max-line-length", "{self.config.formatting["line_length"]}"]

-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
    -   id: mypy
        additional_dependencies: [types-all]
"""

    async def _rollback(self) -> None:
        """Rolls back changes on failure."""
        if self.setup_state.git_initialized:
            try:
                git_dir = self.project_dir / ".git"
                if git_dir.exists():
                    shutil.rmtree(git_dir)
            except Exception as e:
                logger.error(
                    f"Failed to rollback git initialization: {str(e)}")

        if self.setup_state.venv_created:
            try:
                venv_dir = self.project_dir / "venv"
                if venv_dir.exists():
                    shutil.rmtree(venv_dir)
            except Exception as e:
                logger.error(f"Failed to rollback venv creation: {str(e)}")

        if self.setup_state.docker_setup:
            try:
                for file in ["Dockerfile", "docker-compose.yml"]:
                    file_path = self.project_dir / file
                    if file_path.exists():
                        file_path.unlink()
            except Exception as e:
                logger.error(f"Failed to rollback Docker setup: {str(e)}")

        if self.setup_state.ci_setup:
            try:
                if self.config.ci_provider == "github-actions":
                    github_dir = self.project_dir / ".github"
                    if github_dir.exists():
                        shutil.rmtree(github_dir)
                elif self.config.ci_provider == "gitlab-ci":
                    gitlab_ci = self.project_dir / ".gitlab-ci.yml"
                    if gitlab_ci.exists():
                        gitlab_ci.unlink()
            except Exception as e:
                logger.error(f"Failed to rollback CI setup: {str(e)}")

    async def setup_project(self) -> None:
        """Sets up the project with progress tracking."""
        total_steps = sum([
            self.config.features["use_git"],
            True,  # Python environment setup is always needed
            self.config.features["use_docker"],
            self.config.features["use_ci"],
            self.config.documentation["enabled"],
            True,  # Formatting setup is always needed
        ])

        with self._progress_tracker(total_steps) as progress:
            try:
                # Initialize git if requested
                if self.config.features["use_git"]:
                    task_id = progress.add_task("Initializing git...", total=1)
                    await self.init_git(progress, task_id)

                # Setup Python environment
                task_id = progress.add_task("Setting up Python environment...",
                                            total=1)
                await self.setup_python_env(progress, task_id)

                # Setup Docker if requested
                if self.config.features["use_docker"]:
                    task_id = progress.add_task("Setting up Docker...",
                                                total=1)
                    await self.setup_docker(progress, task_id)

                # Setup CI if requested
                if self.config.features["use_ci"]:
                    task_id = progress.add_task("Setting up CI...", total=1)
                    await self.setup_ci(progress, task_id)

                # Setup documentation if enabled
                if self.config.documentation["enabled"]:
                    task_id = progress.add_task("Setting up documentation...",
                                                total=1)
                    await self.setup_documentation(progress, task_id)

                # Setup formatting
                task_id = progress.add_task("Setting up formatting...",
                                            total=1)
                await self.setup_formatting(progress, task_id)

                self._display_success()

            except Exception as e:
                self._display_error(str(e))
                sys.exit(1)

    def _display_success(self) -> None:
        """Displays success message with setup details."""
        self.console.print(
            Panel.fit(
                f"[green]Project Setup Completed Successfully![/green]\n"
                f"Project: {self.config.project_slug}\n"
                f"Features Enabled:\n"
                f"  - Git: {self.setup_state.git_initialized}\n"
                f"  - Dependencies: {self.setup_state.dependencies_installed}\n"
                f"  - Docker: {self.setup_state.docker_setup}\n"
                f"  - CI/CD: {self.setup_state.ci_setup}\n"
                f"  - Documentation: {self.setup_state.documentation_setup}\n"
                f"  - Formatting: {self.setup_state.formatting_setup}",
                title="Setup Success",
                border_style="green"))

    def _display_error(self, error_msg: str) -> None:
        """Displays error message with details."""
        self.console.print(
            Panel.fit(f"[red]Error: {error_msg}[/red]",
                      title="Setup Error",
                      border_style="red"))


async def main():
    """Main function to run project setup."""
    try:
        setup_manager = ProjectSetupManager()
        await setup_manager.setup_project()
    except KeyboardInterrupt:
        console.print("\n[yellow]Setup interrupted by user[/yellow]")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
