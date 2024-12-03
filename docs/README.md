# }

{{ cookiecutter.project_description }}
![Python Version](https://img.shields.io/badge/python-{{ cookiecutter.python_version }}-blue)
{% if cookiecutter.open_source_license != "Not open source" %}
![License](https://img.shields.io/badge/license-{{ cookiecutter.open_source_license | replace(" ", "%20")}}-blue)
{% endif %}
![Stars](https://img.shields.io/github/stars/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}?style=social)
![Forks](https://img.shields.io/github/forks/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}?style=social)
![Issues](https://img.shields.io/github/issues/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
![Contributors](https://img.shields.io/github/contributors/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
![Last Commit](https://img.shields.io/github/last-commit/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
![Commit Activity](https://img.shields.io/github/commit-activity/m/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

## Installation

### Prerequisites

- [Python {{ cookiecutter.python_version }}](https://www.python.org/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Pyenv](https://github.com/pyenv/pyenv#installation)

```bash
# Clone the repository
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
# Navigate into the project directory
cd {{ cookiecutter.project_slug }}
# Install dependencies using Poetry
poetry install

---

## Usage

```zsh
poetry run python {{ cookiecutter.project_slug }}
```

## Development


