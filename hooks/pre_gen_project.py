import os
import re
import sys


def validate_config():
    project_name = "{{ cookiecutter.project_name }}"
    project_slug = "{{ cookiecutter.project_slug }}"
    open_source_license = "{{ cookiecutter.open_source_license }}"

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

    # Validate open_source_license
    allowed_licenses = [
        "GNU Affero General Public License v3.0 (AGPL-3.0)",
        "GNU General Public License v3.0 (GPL-3.0)",
        "GNU Lesser General Public License v3.0 (LGPL-3.0)",
        "Mozilla Public License 2.0 (MPL-2.0)",
        "Apache License 2.0 (Apache-2.0)", "MIT License (MIT)",
        "Boost Software License 1.0 (BSL-1.0)", "The Unlicense",
        "Not open source"
    ]
    if open_source_license not in allowed_licenses:
        print(
            f"ERROR: '{open_source_license}' is not a valid license. Choose from {allowed_licenses}."
        )
        sys.exit(1)

    # Check if the project directory already exists
    if os.path.exists(project_slug):
        print(
            f"ERROR: The directory '{project_slug}' already exists. Please choose a different project slug."
        )
        sys.exit(1)


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
module_name = '{{ cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name!' %
          module_name)
    sys.exit(1)

if __name__ == "__main__":
    validate_config()
