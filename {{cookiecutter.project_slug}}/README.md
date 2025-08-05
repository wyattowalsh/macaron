<div align="center">
  <h1>🚀 {{ cookiecutter.project_name }}</h1>
  <p><em>{{ cookiecutter.project_description }}</em></p>
  
  [![Version](https://img.shields.io/badge/version-{{ cookiecutter.project_version }}-blue.svg)]({{ cookiecutter.project_repository }}/releases)
  [![Python](https://img.shields.io/badge/python-{{ cookiecutter.python_version }}+-blue.svg)](https://www.python.org/downloads/)
  [![License](https://img.shields.io/badge/license-{{ cookiecutter.license_type.split(' (')[0] if '(' in cookiecutter.license_type else cookiecutter.license_type | replace(' ', '%20') }}-green.svg)](./LICENSE)
  
  {% if cookiecutter.include_ci_workflow %}[![CI]({{ cookiecutter.project_repository }}/actions/workflows/ci.yml/badge.svg)]({{ cookiecutter.project_repository }}/actions/workflows/ci.yml){% endif %}
  {% if cookiecutter.include_codecov %}[![codecov](https://codecov.io/gh/{{ cookiecutter.github }}/{{ cookiecutter.project_slug }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github }}/{{ cookiecutter.project_slug }}){% endif %}
  [![Code style: {{ cookiecutter.code_style }}](https://img.shields.io/badge/code%20style-{{ cookiecutter.code_style }}-000000.svg)](https://{{ 'github.com/psf/black' if cookiecutter.code_style == 'black' else 'github.com/astral-sh/ruff' if cookiecutter.code_style == 'ruff-format' else 'github.com/google/yapf' }})
  {% if cookiecutter.type_checker != "none" %}[![Type checker: {{ cookiecutter.type_checker }}](https://img.shields.io/badge/type%20checker-{{ cookiecutter.type_checker }}-blue.svg)](https://{{ 'mypy-lang.org' if cookiecutter.type_checker == 'mypy' else 'github.com/microsoft/pyright' }}){% endif %}
  
  ![Stars](https://img.shields.io/github/stars/{{ cookiecutter.github }}/{{ cookiecutter.project_slug }}?style=social)
  ![Forks](https://img.shields.io/github/forks/{{ cookiecutter.github }}/{{ cookiecutter.project_slug }}?style=social)
  ![Issues](https://img.shields.io/github/issues/{{ cookiecutter.github }}/{{ cookiecutter.project_slug }})
  ![Contributors](https://img.shields.io/github/contributors/{{ cookiecutter.github }}/{{ cookiecutter.project_slug }})
  ![Last Commit](https://img.shields.io/github/last-commit/{{ cookiecutter.github }}/{{ cookiecutter.project_slug }})
</div>

## ✨ Features

- 🐍 **Modern Python**: Built with Python {{ cookiecutter.python_version }}+ and modern best practices
- 📦 **Package Management**: Uses {{ cookiecutter.package_manager }} for dependency management
{% if cookiecutter.include_cli_example %}- 🖥️ **CLI Interface**: Rich command-line interface with Typer and Rich{% endif %}
{% if cookiecutter.include_api %}- 🌐 **REST API**: FastAPI-based REST API with automatic OpenAPI documentation{% endif %}
{% if cookiecutter.include_async %}- ⚡ **Async Support**: Full async/await support for high-performance operations{% endif %}
{% if cookiecutter.include_database %}- 🗃️ **Database Integration**: {{ cookiecutter.database_type.title() }} database support with SQLAlchemy{% endif %}
- 🧪 **Comprehensive Testing**: pytest with coverage reporting and advanced testing features
- 🔍 **Code Quality**: {{ cookiecutter.linter }} linting, {{ cookiecutter.code_style }} formatting, and {{ cookiecutter.type_checker }} type checking
{% if cookiecutter.include_pre_commit %}- 🪝 **Pre-commit Hooks**: Automated code quality checks before commits{% endif %}
{% if cookiecutter.include_docker %}- 🐳 **Docker Support**: Multi-stage Dockerfile and docker-compose setup{% endif %}
{% if cookiecutter.include_docs_site %}- 📚 **Documentation**: Comprehensive documentation with modern docs site{% endif %}
{% if cookiecutter.include_ci_workflow %}- 🚀 **CI/CD**: GitHub Actions workflows for testing, quality checks, and deployment{% endif %}
{% if cookiecutter.include_monitoring %}- 📊 **Monitoring**: Built-in observability with Prometheus and Grafana{% endif %}
{% if cookiecutter.include_security %}- 🔒 **Security**: Security scanning with Bandit and Safety{% endif %}

## Table of Contents

- [Technologies Used](#technologies-used)
- [Project Demo](#project-demo)
- [GitHub Actions](#github-actions)
- [Screenshots](#screenshots)
- [Star History](#star-history)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Issue Templates](#issue-templates)
- [License](#license)
- [Feedback](#feedback)

## Technologies Used

![Pyenv](https://img.shields.io/badge/version%20manager-pyenv-blue)

## Project Demo

![Demo GIF](https://user-images.githubusercontent.com/your-username/your-project-demo.gif)

## GitHub Actions

![Build Status](https://github.com/{{ cookiecutter.github }}/{{ cookiecutter.project_slug }}/actions/workflows/format-lint-test.yml/badge.svg)

## Screenshots

<p align="center">
  <img src="https://user-images.githubusercontent.com/your-username/screenshot1.png" alt="Screenshot 1" width="400"/>
  <img src="https://user-images.githubusercontent.com/your-username/screenshot2.png" alt="Screenshot 2" width="400"/>
</p>

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos={{ cookiecutter.github }}/{{ cookiecutter.project_slug }}&type=Date)](https://star-history.com/#{{ cookiecutter.github }}/{{ cookiecutter.project_slug }}&Date)

## Installation

### Prerequisites

- [Python {{ cookiecutter.python_version }}](https://www.python.org/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Pyenv](https://github.com/pyenv/pyenv#installation)

```bash
# Clone the repository
git clone https://github.com/{{ cookiecutter.github }}/{{ cookiecutter.project_slug }}.git

# Navigate into the project directory
cd {{ cookiecutter.project_slug }}

# Install dependencies using Poetry
poetry install
```

## Usage

```bash
poetry run python -m {{ cookiecutter.project_slug }}
```

## Development

For details on contributing to development and setting up the development environment, please refer to [DEVELOPMENT.md](DEVELOPMENT.md).

### Issue Templates

To help facilitate contributions and track issues effectively, please refer to our [Issue Templates](https://github.com/{{ cookiecutter.github }}/{{ cookiecutter.project_slug }}/issues/new/choose) to submit:

- Bug reports
- Feature requests
- Documentation issues

## Documentation

Documentation can be found at [Documentation Link](https://github.com/{{ cookiecutter.github }}/{{ cookiecutter.project_slug }}/wiki).

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Feedback

If you have any feedback or suggestions, feel free to open an issue or reach out directly at [email@example.com](mailto:email@example.com).

## License

Distributed under the {{ cookiecutter.license_type }} License. See `LICENSE` for more information.

---

<p align="center">💻 Made with ❤️ and Python by {{ cookiecutter.full_name }}</p>