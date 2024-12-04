import re
import sys
from typing import Dict


def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def validate_project_name(name: str) -> bool:
    """Validate project name format."""
    return bool(re.match(r"^[A-Za-z][A-Za-z ]*$", name.strip()))


def validate_project_slug(slug: str) -> bool:
    """Validate project slug format."""
    return bool(re.match(r"^[_a-zA-Z][_a-zA-Z0-9\-]*$", slug.strip()))


def validate_version(version: str) -> bool:
    """Validate version format (e.g., 1.0.0)."""
    return bool(re.match(r"^\d+\.\d+\.\d+$", version))


def validate_python_version(version: str) -> bool:
    """Validate Python version format (e.g., 3.11, 3.13)."""
    try:
        major, minor = map(int, version.split('.'))
        return major == 3 and 8 <= minor <= 13  # Python 3.8 to 3.13
    except ValueError:
        return False


ALLOWED_LICENSES = [
    "GNU Affero General Public License v3.0 (AGPL-3.0)",
    "GNU General Public License v3.0 (GPL-3.0)",
    "GNU Lesser General Public License v3.0 (LGPL-3.0)",
    "Mozilla Public License 2.0 (MPL-2.0)", "Apache License 2.0 (Apache-2.0)",
    "MIT License (MIT)", "Boost Software License 1.0 (BSL-1.0)",
    "The Unlicense", "Not open source"
]


def validate_license(license_type: str) -> bool:
    """Validate license type."""
    return license_type in ALLOWED_LICENSES


def get_context_data() -> Dict:
    """Get the context data from cookiecutter."""
    return {
        "author": {
            "full_name": "{{ cookiecutter.full_name }}",
            "email": "{{ cookiecutter.email }}",
            "github_username": "{{ cookiecutter.github }}"
        },
        "project": {
            "name": "{{ cookiecutter.project_name }}",
            "slug": "{{ cookiecutter.project_slug }}",
            "version": "{{ cookiecutter.project_version }}",
            "description": "{{ cookiecutter.project_description }}",
            "repository": "{{ cookiecutter.project_repository }}",
            "documentation": "{{ cookiecutter.project_url }}",
            "changelog": "{{ cookiecutter.project_changelog }}"
        },
        "python_version": "{{ cookiecutter.python_version }}",
        "license_type": "{{ cookiecutter.license_type }}"
    }


def validate_url(url: str) -> bool:
    """Validate URL format."""
    pattern = (r'^https?:\/\/(localhost(:\d+)?|'
               r'((www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}))'
               r'\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$')
    return bool(re.match(pattern, url))


def main() -> None:
    """Main function to validate project configuration."""
    try:
        context = get_context_data()

        # Validate author information
        if not validate_email(context["author"]["email"]):
            print("ERROR: Invalid email format")
            sys.exit(1)

        # Validate project information
        if not validate_project_name(context["project"]["name"]):
            print("ERROR: Project name must contain only letters and spaces")
            sys.exit(1)

        if not validate_project_slug(context["project"]["slug"]):
            print("ERROR: Project slug must start with a letter/underscore and"
                  " contain only letters, numbers, underscores, and hyphens")
            sys.exit(1)

        if not validate_version(context["project"]["version"]):
            print("ERROR: Version must be in format X.Y.Z (e.g., 1.0.0)")
            sys.exit(1)

        if len(context["project"]["description"]) < 10:
            print("ERROR: Project description must be at least 10 characters"
                  " long")
            sys.exit(1)

        # Validate URLs
        for url_field in ["repository", "documentation", "changelog"]:
            url = context["project"][url_field]
            if url and not validate_url(url):
                print(f"ERROR: Invalid {url_field} URL format")
                sys.exit(1)

        # Validate Python version
        if not validate_python_version(context["python_version"]):
            print("ERROR: Python version must be Python 3.8-3.13")
            sys.exit(1)

        # Validate license
        if not validate_license(context["license_type"]):
            print(
                f"ERROR: License must be one of: {', '.join(ALLOWED_LICENSES)}"
            )
            sys.exit(1)

        print("Project configuration validated successfully!")
        print(f"Project: {context['project']['name']}"
              f" ({context['project']['slug']})")
        print(f"Python: {context['python_version']}")
        print(f"License: {context['license_type']}")

    except Exception as e:
        print(f"ERROR: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
