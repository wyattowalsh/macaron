import re
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, root_validator, validator
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
    keywords: List[str]
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


class Python(BaseModel):
    """Python configuration validation."""
    version: str
    requires: str
    dev_dependencies: List[str]
    doc_dependencies: List[str]
    prod_dependencies: List[str]

    def validate_dependencies(self, v: List[str]) -> List[str]:
        for dep in v:
            if not re.match(r"^[a-zA-Z0-9\-_]+>=\d+\.\d+\.\d+$", dep):
                raise ValueError(f"Invalid dependency format: {dep}")
        return v


class Features(BaseModel):
    """Features configuration validation."""
    use_git: bool
    use_venv: bool
    use_docker: bool
    use_ci: bool
    ci_provider: str
    use_pre_commit: bool
    use_dependabot: bool

    def validate_ci_provider(self, v: str) -> str:
        allowed = ["github-actions", "gitlab-ci", "none"]
        if v not in allowed:
            raise ValueError(
                f"CI provider must be one of: {', '.join(allowed)}")
        return v


class Documentation(BaseModel):
    """Documentation configuration validation."""
    enabled: bool
    type: str
    hosting: str

    def validate_doc_options(self, v: str, field) -> str:
        allowed = {
            "type": ["sphinx", "mkdocs", "none"],
            "hosting": ["readthedocs", "github-pages", "none"],
        }
        if v not in allowed[field.name]:
            raise ValueError(
                f"{field.name} must be one of: {', '.join(allowed[field.name])}"
            )
        return v


class Packaging(BaseModel):
    """Packaging configuration validation."""
    use_poetry: bool
    use_setuptools: bool
    publish_to_pypi: bool

    def validate_packaging(self, values: Dict) -> Dict:
        if values.get("use_poetry") and values.get("use_setuptools"):
            raise ValueError("Cannot use both poetry and setuptools")
        if not values.get("use_poetry") and not values.get("use_setuptools"):
            raise ValueError("Must use either poetry or setuptools")
        return values


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
    file: str
    header: bool

    def validate_license(self, v: str) -> str:
        if v not in self.ALLOWED_LICENSES:
            raise ValueError(
                f"License must be one of: {', '.join(self.ALLOWED_LICENSES)}")
        return v


class Analytics(BaseModel):
    """Analytics configuration validation."""
    gtm_container_id: Optional[str]
    use_google_analytics: bool
    use_plausible: bool

    def validate_gtm_id(self, v: Optional[str]) -> Optional[str]:
        if v and not re.match(r"^GTM-[A-Z0-9]{7}$", v):
            raise ValueError("Invalid GTM container ID format")
        return v


def get_context_data() -> Dict:
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
            "keywords": {{cookiecutter.project_keywords}},
            "repository": "{{ cookiecutter.project_repository }}",
            "documentation": "{{ cookiecutter.project_documentation }}",
            "changelog": "{{ cookiecutter.project_changelog }}"
        },
        "python": {
            "version": "{{ cookiecutter.python_version }}",
            "requires": "{{ cookiecutter.python_requires }}",
            "dev_dependencies": {{cookiecutter.python_dev_dependencies}},
            "doc_dependencies": {{cookiecutter.python_doc_dependencies}},
            "prod_dependencies": {{cookiecutter.python_prod_dependencies}}
        },
        "use_git": {{cookiecutter.use_git}},
        "use_venv": {{cookiecutter.use_venv}},
        "use_docker": {{cookiecutter.use_docker}},
        "use_ci": {{cookiecutter.use_ci}},
        "ci_provider": "{{ cookiecutter.ci_provider }}",
        "use_pre_commit": {{cookiecutter.use_pre_commit}},
        "use_dependabot": {{cookiecutter.use_dependabot}},
        "use_pytest": {{cookiecutter.use_pytest}},
        "use_tox": {{cookiecutter.use_tox}},
        "minimum_coverage": {{cookiecutter.minimum_coverage}},
        "docs_enabled": {{cookiecutter.docs_enabled}},
        "docs_type": "{{ cookiecutter.docs_type }}",
        "docs_hosting": "{{ cookiecutter.docs_hosting }}",
        "use_poetry": {{cookiecutter.use_poetry}},
        "use_setuptools": {{cookiecutter.use_setuptools}},
        "publish_to_pypi": {{cookiecutter.publish_to_pypi}},
        "license_type": "{{ cookiecutter.license_type }}",
        "license_file": "{{ cookiecutter.license_file }}",
        "license_header": {{cookiecutter.license_header}},
        "line_length": {{cookiecutter.line_length}},
        "quote_style": "{{ cookiecutter.quote_style }}",
        "line_endings": "{{ cookiecutter.line_endings }}",
        "gtm_container_id": "{{ cookiecutter.gtm_container_id }}",
        "use_google_analytics": {{cookiecutter.use_google_analytics}},
        "use_plausible": {{cookiecutter.use_plausible}}
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

        # Validate Python configuration
        python = Python(**config_data["python"])

        # Create and validate features configuration
        features = Features(use_git=config_data["use_git"],
                            use_venv=config_data["use_venv"],
                            use_docker=config_data["use_docker"],
                            use_ci=config_data["use_ci"],
                            ci_provider=config_data["ci_provider"],
                            use_pre_commit=config_data["use_pre_commit"],
                            use_dependabot=config_data["use_dependabot"])

        # Create and validate documentation configuration
        docs = Documentation(enabled=config_data["docs_enabled"],
                             type=config_data["docs_type"],
                             hosting=config_data["docs_hosting"])

        # Create and validate packaging configuration
        packaging = Packaging(use_poetry=config_data["use_poetry"],
                              use_setuptools=config_data["use_setuptools"],
                              publish_to_pypi=config_data["publish_to_pypi"])

        # Create and validate license configuration
        license = License(type=config_data["license_type"],
                          file=config_data["license_file"],
                          header=config_data["license_header"])

        # Create and validate analytics configuration
        analytics = Analytics(
            gtm_container_id=config_data["gtm_container_id"],
            use_google_analytics=config_data["use_google_analytics"],
            use_plausible=config_data["use_plausible"])

        console.print(
            Panel.fit(
                "[green]Project Configuration Validated Successfully![/green]\n"
                f"Project: {project.name} ({project.slug})\n"
                f"Python: {python.version}\n"
                f"License: {license.type}"))

    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
