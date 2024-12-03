# Development Guide

## Setting Up Your Development Environment

1. **Clone the repository**:
    ```bash
    git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
    cd {{ cookiecutter.project_slug }}
    ```

2. **Install dependencies**:
    ```bash
    poetry install
    ```

3. **Activate the development environment**:
    ```bash
    poetry shell
    ```

4. **Run the test suite**:
    ```bash
    poetry run pytest
    ```

5. **Format and lint code**:
    ```bash
    poetry run black .
    poetry run flake8
    ```

## Issue Tracking and Contributions

Please refer to our [Issue Templates](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues/new/choose) to submit or contribute to:

- [Bug Reports](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues/new?template=bug_report.md)
- [Feature Requests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues/new?template=feature_request.md)