import os
import re
import sys
from typing import Dict, List, Optional
from pathlib import Path

from pydantic import BaseModel, Field, validator, root_validator
from rich.console import Console
from rich.panel import Panel
from loguru import logger

# Configure logging
logger.add("project_generation.log", rotation="1 MB", level="INFO")
console = Console()


class ValidationError(Exception):
    """Custom exception for validation failures."""
    pass


class AuthorConfig(BaseModel):
    """Author configuration validation."""
    full_name: str = Field(..., min_length=1)
    email: str = Field(
        ...,
        regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    )
    github_username: str = Field(..., min_length=1)
    pypi_username: str

    @validator("email")
    def validate_email(cls, v: str) -> str:
        if not re.match(
            r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", v
        ):
            raise ValueError("Invalid email format")
        return v


class ProjectURLs(BaseModel):
    """Project URLs validation."""
    repository: str
    documentation: str
    changelog: str


class ProjectConfig(BaseModel):
    """Project configuration validation."""
    name: str = Field(..., min_length=1, max_length=100)
    slug: str = Field(..., min_length=1, max_length=100)
    version: str = Field(..., regex=r"^\d+\.\d+\.\d+$")
    description: str = Field(..., min_length=10)
    keywords: List[str]
    urls: ProjectURLs

    @validator("name")
    def validate_name(cls, v: str) -> str:
        if not re.match(r"^[A-Za-z][A-Za-z ]*$", v.strip()):
            raise ValueError(
                "Project name must contain only letters and spaces"
            )
        return v.strip()

    @validator("slug")
    def validate_slug(cls, v: str) -> str:
        if not re.match(r"^[_a-zA-Z][_a-zA-Z0-9\-]*$", v.strip()):
            raise ValueError(
                "Project slug must start with a letter/underscore and "
                "contain only letters, numbers, underscores, and hyphens"
            )
        return v.strip()


class PythonDependencies(BaseModel):
    """Python dependencies validation."""
    development: List[str]
    documentation: List[str]
    production: List[str]

    @validator("*")
    def validate_dependencies(cls, v: List[str]) -> List[str]:
        for dep in v:
            if not re.match(r"^[a-zA-Z0-9\-_]+>=\d+\.\d+\.\d+$", dep):
                raise ValueError(f"Invalid dependency format: {dep}")
        return v


class PythonConfig(BaseModel):
    """Python configuration validation."""
    version: str = Field(..., regex=r"^\d+\.\d+$")
    requires_python: str = Field(..., regex=r"^>=\d+\.\d+$")
    dependencies: PythonDependencies


class FeaturesConfig(BaseModel):
    """Features configuration validation."""
    use_git: bool
    use_venv: bool
    use_docker: bool
    use_ci: bool
    ci_provider: str
    use_pre_commit: bool
    use_dependabot: bool

    @validator("ci_provider")
    def validate_ci_provider(cls, v: str) -> str:
        allowed = ["github-actions", "gitlab-ci", "none"]
        if v not in allowed:
            raise ValueError(
                f"CI provider must be one of: {', '.join(allowed)}"
            )
        return v


class TestingConfig(BaseModel):
    """Testing configuration validation."""
    use_pytest: bool
    use_tox: bool
    minimum_coverage: int = Field(..., ge=0, le=100)


class DocumentationConfig(BaseModel):
    """Documentation configuration validation."""
    enabled: bool
    type: str
    hosting: str

    @validator("type", "hosting")
    def validate_doc_options(cls, v: str, field) -> str:
        allowed = {
            "type": ["sphinx", "mkdocs", "none"],
            "hosting": ["readthedocs", "github-pages", "none"],
        }
        if v not in allowed[field.name]:
            raise ValueError(
                f"{field.name} must be one of: "
                f"{', '.join(allowed[field.name])}"
            )
        return v


class PackagingConfig(BaseModel):
    """Packaging configuration validation."""
    use_poetry: bool
    use_setuptools: bool
    publish_to_pypi: bool

    @root_validator
    def validate_packaging(cls, values: Dict) -> Dict:
        if values.get("use_poetry") and values.get("use_setuptools"):
            raise ValueError("Cannot use both poetry and setuptools")
        if not values.get("use_poetry") and not values.get("use_setuptools"):
            raise ValueError("Must use either poetry or setuptools")
        return values


class LicenseConfig(BaseModel):
    """License configuration validation."""
    type: str
    file: str = Field(default="LICENSE")
    header: bool = Field(default=True)

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

    @validator("type")
    def validate_license(cls, v: str) -> str:
        if v not in cls.ALLOWED_LICENSES:
            raise ValueError(
                f"License must be one of: {', '.join(cls.ALLOWED_LICENSES)}"
            )
        return v


class FormattingConfig(BaseModel):
    """Formatting configuration validation."""
    line_length: int = Field(..., ge=79, le=120)
    quotes: str = Field(..., regex=r"^(single|double)$")
    line_endings: str = Field(..., regex=r"^\\n|\\r\\n$")


class AnalyticsConfig(BaseModel):
    """Analytics configuration validation."""
    gtm_container_id: Optional[str] = None
    use_google_analytics: bool = False
    use_plausible: bool = False

    @validator("gtm_container_id")
    def validate_gtm_id(cls, v: Optional[str]) -> Optional[str]:
        if v and not re.match(r"^GTM-[A-Z0-9]{7}$", v):
            raise ValueError("Invalid GTM container ID format")
        return v


class MainConfig(BaseModel):
    """Main configuration validation."""
    author: AuthorConfig
    project: ProjectConfig
    python: PythonConfig
    features: FeaturesConfig
    testing: TestingConfig
    documentation: DocumentationConfig
    packaging: PackagingConfig
    license: LicenseConfig
    formatting: FormattingConfig
    analytics: AnalyticsConfig


class ProjectValidator:
    """Handles project validation and setup."""

    def __init__(self) -> None:
        self.console: Console = console
        self._cache_dir = Path.home() / ".macaron" / "cache"
        self._cache_dir.mkdir(parents=True, exist_ok=True)

    def validate_config(self) -> None:
        """Validates all project configuration."""
        try:
            # Extract values from cookiecutter context
            config_data = {
                "author": {
                    "full_name": "{{ cookiecutter.author.full_name }}",
                    "email": "{{ cookiecutter.author.email }}",
                    "github_username": "{{ cookiecutter.author.github_username }}",
                    "pypi_username": "{{ cookiecutter.author.pypi_username }}",
                },
                "project": {
                    "name": "{{ cookiecutter.project.name }}",
                    "slug": "{{ cookiecutter.project.slug }}",
                    "version": "{{ cookiecutter.project.version }}",
                    "description": "{{ cookiecutter.project.description }}",
                    "keywords": ["{{ cookiecutter.project.keywords }}"],
                    "urls": {
                        "repository": "{{ cookiecutter.project.urls.repository }}",
                        "documentation": "{{ cookiecutter.project.urls.documentation }}",
                        "changelog": "{{ cookiecutter.project.urls.changelog }}",
                    },
                },
                "python": {
                    "version": "{{ cookiecutter.python.version }}",
                    "requires_python": "{{ cookiecutter.python.requires_python }}",
                    "dependencies": {
                        "development": ["{{ cookiecutter.python.dependencies.development }}"],
                        "documentation": ["{{ cookiecutter.python.dependencies.documentation }}"],
                        "production": ["{{ cookiecutter.python.dependencies.production }}"],
                    },
                },
                "features": {
                    "use_git": "{{ cookiecutter.features.use_git }}",
                    "use_venv": "{{ cookiecutter.features.use_venv }}",
                    "use_docker": "{{ cookiecutter.features.use_docker }}",
                    "use_ci": "{{ cookiecutter.features.use_ci }}",
                    "ci_provider": "{{ cookiecutter.features.ci_provider }}",
                    "use_pre_commit": "{{ cookiecutter.features.use_pre_commit }}",
                    "use_dependabot": "{{ cookiecutter.features.use_dependabot }}",
                },
                "testing": {
                    "use_pytest": "{{ cookiecutter.testing.use_pytest }}",
                    "use_tox": "{{ cookiecutter.testing.use_tox }}",
                    "minimum_coverage": "{{ cookiecutter.testing.minimum_coverage }}",
                },
                "documentation": {
                    "enabled": "{{ cookiecutter.documentation.enabled }}",
                    "type": "{{ cookiecutter.documentation.type }}",
                    "hosting": "{{ cookiecutter.documentation.hosting }}",
                },
                "packaging": {
                    "use_poetry": "{{ cookiecutter.packaging.use_poetry }}",
                    "use_setuptools": "{{ cookiecutter.packaging.use_setuptools }}",
                    "publish_to_pypi": "{{ cookiecutter.packaging.publish_to_pypi }}",
                },
                "license": {
                    "type": "{{ cookiecutter.license.type }}",
                    "file": "{{ cookiecutter.license.file }}",
                    "header": "{{ cookiecutter.license.header }}",
                },
                "formatting": {
                    "line_length": "{{ cookiecutter.formatting.line_length }}",
                    "quotes": "{{ cookiecutter.formatting.quotes }}",
                    "line_endings": "{{ cookiecutter.formatting.line_endings }}",
                },
                "analytics": {
                    "gtm_container_id": "{{ cookiecutter.analytics.gtm_container_id }}",
                    "use_google_analytics": "{{ cookiecutter.analytics.use_google_analytics }}",
                    "use_plausible": "{{ cookiecutter.analytics.use_plausible }}",
                },
            }

            # Validate using Pydantic model
            config = MainConfig(**config_data)

            # Additional validations
            self._validate_directory(config.project.slug)
            self._validate_python_compatibility(config.python.version)
            self._validate_dependencies_compatibility(config.python.dependencies)

            # Cache valid configuration
            self._cache_config(config)
            self._display_success(config)

        except Exception as e:
            self._handle_validation_error(e)

    def _validate_directory(self, project_slug: str) -> None:
        """Validates project directory availability."""
        if os.path.exists(project_slug):
            raise ValidationError(
                f"Directory '{project_slug}' already exists. "
                "Please choose a different project name."
            )

    def _validate_python_compatibility(self, version: str) -> None:
        """Validates Python version compatibility."""
        current_version = sys.version_info
        required_version = tuple(map(int, version.split(".")))

        if current_version < required_version:
            raise ValidationError(
                f"Project requires Python {version} but current version is "
                f"{'.'.join(map(str, current_version[:3]))}"
            )

    def _validate_dependencies_compatibility(
        self, dependencies: PythonDependencies
    ) -> None:
        """Validates dependencies compatibility."""
        all_deps = (
            dependencies.development
            + dependencies.documentation
            + dependencies.production
        )
        seen_packages = {}
        for dep in all_deps:
            name, _, version_spec = dep.partition(">=")
            if name in seen_packages and seen_packages[name] != version_spec:
                raise ValidationError(
                    f"Conflicting versions for {name}: "
                    f"{seen_packages[name]} vs {version_spec}"
                )
            seen_packages[name] = version_spec

    def _cache_config(self, config: MainConfig) -> None:
        """Caches valid configuration for future use."""
        cache_file = self._cache_dir / f"{config.project.slug}_config.json"
        cache_file.write_text(config.json(indent=2))

    def _display_success(self, config: MainConfig) -> None:
        """Displays success message with project details."""
        self.console.print(
            Panel.fit(
                f"[green]Project Configuration Validated Successfully![/green]\n"
                f"Project: {config.project.name} ({config.project.slug})\n"
                f"Python: {config.python.version}\n"
                f"License: {config.license.type}\n"
                f"Features: Git={config.features.use_git}, "
                f"Docker={config.features.use_docker}, "
                f"CI={config.features.use_ci}",
                title="Validation Success",
                border_style="green",
            )
        )

    def _handle_validation_error(self, error: Exception) -> None:
        """Handles validation errors with detailed messages."""
        error_msg = str(error)
        logger.error(f"Validation failed: {error_msg}")

        self.console.print(
            Panel.fit(
                f"[red]Error: {error_msg}[/red]",
                title="Validation Error",
                border_style="red",
            )
        )
        sys.exit(1)


def main() -> None:
    """Main function to run project validation."""
    try:
        validator = ProjectValidator()
        validator.validate_config()
    except KeyboardInterrupt:
        console.print("\n[yellow]Validation interrupted by user[/yellow]")
        sys.exit(1)


if __name__ == "__main__":
    main()