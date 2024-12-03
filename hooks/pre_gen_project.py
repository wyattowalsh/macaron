import os
import re
import sys


def validate_config():
    project_name = "{{ cookiecutter.project_name }}"
    project_slug = "{{ cookiecutter.project_slug }}"
    use_docker = "{{ cookiecutter.use_docker }}"
    license = "{{ cookiecutter.license }}"

    # Validate project_name
    if not re.match(r'^[A-Za-z ]+$', project_name.strip()):
        print(
            f"ERROR: '{project_name}' is not a valid project name. Use only letters and spaces."
        )
        sys.exit(1)

    # Validate project_slug
    if not re.match(r'^[_a-zA-Z][_a-zA-Z0-9\-]+$', project_slug.strip()):
        print(
            f"ERROR: '{project_slug}' is not a valid project slug. Use only letters, numbers, underscores, and hyphens."
        )
        sys.exit(1)

    # Validate use_docker
    truthy = {"y", "yes", "true", "1"}
    falsy = {"n", "no", "false", "0"}
    use_docker_value = use_docker.strip().lower()
    if use_docker_value not in truthy.union(falsy):
        print("ERROR: Please enter 'yes' or 'no' for use_docker.")
        sys.exit(1)

    # Validate license
    allowed_licenses = [
        "MIT", "BSD-3", "GNU GPL v3.0", "Apache Software License 2.0"
    ]
    if license not in allowed_licenses:
        print(
            f"ERROR: '{license}' is not a valid license. Choose from {allowed_licenses}."
        )
        sys.exit(1)

    # Check if the project directory already exists
    if os.path.exists(project_slug):
        print(
            f"ERROR: The directory '{project_slug}' already exists. Please choose a different project slug."
        )
        sys.exit(1)


if __name__ == "__main__":
    validate_config()
    validate_config()
