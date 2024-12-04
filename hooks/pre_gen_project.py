import re
from typing import List, Optional

from pydantic import BaseModel, Field, validator
from rich.console import Console
from rich.panel import Panel


class Author(BaseModel):
    """Author configuration validation."""
    full_name: str = Field(default=..., min_length=1)
    email: str = Field(
        default=...,
        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    )
    github_username: str = Field(default=..., min_length=1)
    pypi_username: str

    def validate_email(self, v: str) -> str:
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
                        v):
            raise ValueError("Invalid email format")
        return v


class Project(BaseModel):
    """Project configuration validation."""
    name: str = Field(default=..., min_length=1, max_length=100)
    slug: str = Field(default=..., min_length=1, max_length=100)
    version: str = Field(default=..., pattern=r"^\d+\.\d+\.\d+$")
    description: str = Field(default=..., min_length=10)
    repository: str
    documentation: str
    changelog: str

    def validate_name(self, v: str) -> str:
        if not re.match(r"^[A-Za-z][A-Za-z ]*$", v.strip()):
            raise ValueError(
                "Project name must contain only letters and spaces")
        return v

    def validate_slug(self, v: str) -> str:
        if not re.match(r"^[_a-zA-Z][_a-zA-Z0-9\-]*$", v.strip()):
            raise ValueError(
                "Project slug must start with a letter/underscore and "
                "contain only letters, numbers, underscores, and hyphens")
        return v


class License(BaseModel):
    """License configuration validation."""
    ALLOWED_LICENSES = [
        "GNU Affero General Public License v3.0 (AGPL-3.0)",
        "GNU General Public License v3.0 (GPL-3.0)",
        "GNU Lesser General Public License v3.0 (LGPL-3.0)",
        "Mozilla Public License 2.0 (MPL-2.0)",
        "Apache License 2.0 (Apache-2.0)",
        "MIT License (MIT)",
        "Boost Software License 1.0 (BSL-1.0)",
        "The Unlicense",
        "Not open source",
    ]

    type: str

    def validate_license(self, v: str) -> str:
        if v not in self.ALLOWED_LICENSES:
            raise ValueError(
                f"License must be one of: {', '.join(self.ALLOWED_LICENSES)}")
        return v


def get_context_data():
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


def main():
    """Main function."""
    console = Console()
    try:
        config_data = get_context_data()

        # Validate author configuration
        author = Author(**config_data["author"])

        # Validate project configuration
        project = Project(**config_data["project"])

        # Validate license configuration
        license = License(type=config_data["license_type"])

        console.print(
            Panel.fit(
                "[green]Project Configuration Validated Successfully![/green]\n"
                f"Project: {project.name} ({project.slug})\n"
                f"Python: {config_data['python_version']}\n"
                f"License: {license.type}"))

    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
