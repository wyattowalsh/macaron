# Scripts Directory

This directory contains utility scripts for {{ cookiecutter.project_name }} development and maintenance.

## Available Scripts

### 🔧 Development Scripts

#### `setup_dev.py`
Automated development environment setup script.

**Usage:**
```bash
python scripts/setup_dev.py
```

**Features:**
- Installs all development dependencies
- Sets up pre-commit hooks
- Creates development configuration files
- Verifies the installation
- Creates useful development scripts

#### `validate_template.py`
Template validation script to ensure the project structure is correct.

**Usage:**
```bash
python scripts/validate_template.py [project_dir]
```

**Features:**
- Validates file structure
- Checks Python syntax
- Verifies package configuration
- Tests basic functionality

{% if cookiecutter.include_api %}
#### `dev_server.py` *(Auto-generated)*
Development server with hot reload for the API.

**Usage:**
```bash
python scripts/dev_server.py
```

**Features:**
- Starts FastAPI server with auto-reload
- Debug logging enabled
- Accessible at http://localhost:8000
{% endif %}

### 🚀 Deployment Scripts

#### `deploy.py` *(Coming soon)*
Production deployment automation script.

#### `build_release.py` *(Coming soon)*
Release build and packaging script.

### 📊 Maintenance Scripts

#### `update_deps.py` *(Coming soon)*
Dependency update automation script.

#### `cleanup.py` *(Coming soon)*
Project cleanup and optimization script.

## Usage Examples

### Quick Development Setup
```bash
# Clone and setup
git clone {{ cookiecutter.project_repository }}.git
cd {{ cookiecutter.project_slug }}
python scripts/setup_dev.py

# Verify setup
python scripts/validate_template.py

# Start development
make test
{% if cookiecutter.include_api %}
python scripts/dev_server.py
{% endif %}
```

### Continuous Integration
```bash
# Validate project structure
python scripts/validate_template.py

# Run quality checks
make quality

# Run full test suite
make test

# Build package
make build
```

## Creating Custom Scripts

When creating new scripts for this project:

1. **Use Python 3.{{ cookiecutter.python_version.split('.')[1] }}+** for compatibility
2. **Include docstrings** for all functions and modules
3. **Add error handling** for robust execution
4. **Use Rich** for better console output (if available)
5. **Make scripts executable** with appropriate shebang

### Script Template

```python
#!/usr/bin/env python3
"""
Script description here.

This script does X, Y, and Z for {{ cookiecutter.project_name }}.
"""

import sys
from pathlib import Path

try:
    from rich.console import Console
    console = Console()
    def print_styled(msg, style="white"):
        console.print(msg, style=style)
except ImportError:
    def print_styled(msg, style="white"):
        print(msg)

def main():
    """Main entry point."""
    print_styled("Starting script...", "blue")
    
    # Script logic here
    
    print_styled("Script completed!", "green")

if __name__ == "__main__":
    main()
```

## Environment Variables

Scripts may use these environment variables:

- `{{ cookiecutter.__package_name.upper() }}_ENVIRONMENT`: Runtime environment
- `{{ cookiecutter.__package_name.upper() }}_DEBUG`: Enable debug mode
- `{{ cookiecutter.__package_name.upper() }}_LOG_LEVEL`: Logging level

## Dependencies

Most scripts require the development environment to be set up:

```bash
# Install development dependencies
{% if cookiecutter.package_manager == "poetry" %}
poetry install --all-extras
{% elif cookiecutter.package_manager == "uv" %}
uv sync --all-extras --dev
{% else %}
pip install -e .[all]
{% endif %}
```

## Contributing

When adding new scripts:

1. **Document the script** in this README
2. **Add appropriate tests** if the script is complex
3. **Follow the project's code style**
4. **Include usage examples**
5. **Update the main Makefile** if applicable

## Support

For help with scripts:

- Check the script's `--help` output
- Review the script's docstring
- See the main project documentation
- Open an issue if you find bugs