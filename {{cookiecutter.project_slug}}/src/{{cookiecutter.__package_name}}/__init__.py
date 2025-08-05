"""{{ cookiecutter.project_description }}"""

__version__ = "{{ cookiecutter.project_version }}"
__author__ = "{{ cookiecutter.full_name }}"
__email__ = "{{ cookiecutter.email }}"
__license__ = "{{ cookiecutter.license_type.split(' (')[0] if '(' in cookiecutter.license_type else cookiecutter.license_type }}"

# Public API
{% if cookiecutter.include_cli_example %}from .cli import main as cli_main{% endif %}
{% if cookiecutter.include_api %}from .api import app{% endif %}
from .config import get_config, Config
from .core import *

__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "get_config",
    "Config",
    {% if cookiecutter.include_cli_example %}"cli_main",{% endif %}
    {% if cookiecutter.include_api %}"app",{% endif %}
]