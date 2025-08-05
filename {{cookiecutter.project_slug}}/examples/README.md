# Examples Directory

This directory contains practical usage examples for {{ cookiecutter.project_name }}.

## Available Examples

### 📚 Core Examples

#### `basic_usage.py`
Demonstrates basic functionality and core features.

**Run with:**
```bash
{% if cookiecutter.use_src_layout %}
PYTHONPATH=src python examples/basic_usage.py
{% else %}
python examples/basic_usage.py
{% endif %}
```

**Features shown:**
- Basic greeting functionality
- Configuration management
- Base class usage
{% if cookiecutter.include_async %}- Async operations{% endif %}
- Error handling

{% if cookiecutter.include_cli_example %}
#### `cli_examples.py`
Shows CLI usage patterns and advanced command-line features.

**Run with:**
```bash
python examples/cli_examples.py
```

**Features shown:**
- Command-line argument parsing
- Interactive prompts
- Progress bars
- Output formatting
{% endif %}

{% if cookiecutter.include_api %}
#### `api_examples.py`
Demonstrates API usage and client integration.

**Run with:**
```bash
# Start the API server first
uvicorn {{ cookiecutter.__package_name }}.api:app --reload

# Then run the examples
python examples/api_examples.py
```

**Features shown:**
- API client usage
- Endpoint testing
- Error handling
- Response processing
{% endif %}

{% if cookiecutter.include_database %}
#### `database_examples.py`
Shows database operations and data management.

**Run with:**
```bash
python examples/database_examples.py
```

**Features shown:**
- Database connection
- CRUD operations
- Query building
- Transaction management
{% endif %}

### 🔧 Advanced Examples

#### `configuration_examples.py`
Advanced configuration patterns and environment management.

#### `testing_examples.py`
Shows how to write effective tests for your code.

#### `performance_examples.py`
Performance optimization techniques and benchmarking.

## Running Examples

### Prerequisites

Make sure you have the development environment set up:

```bash
# Install dependencies
{% if cookiecutter.package_manager == "poetry" %}
poetry install --all-extras
{% elif cookiecutter.package_manager == "uv" %}
uv sync --all-extras --dev
{% else %}
pip install -e .[all]
{% endif %}

# Set up development environment
python scripts/setup_dev.py
```

### Environment Setup

Some examples may require environment variables:

```bash
# Development environment
export {{ cookiecutter.__package_name.upper() }}_ENVIRONMENT=development
export {{ cookiecutter.__package_name.upper() }}_DEBUG=true
export {{ cookiecutter.__package_name.upper() }}_LOG_LEVEL=DEBUG

{% if cookiecutter.include_api %}
# API configuration
export {{ cookiecutter.__package_name.upper() }}_API_HOST=localhost
export {{ cookiecutter.__package_name.upper() }}_API_PORT=8000
{% endif %}

{% if cookiecutter.include_database %}
# Database configuration
export {{ cookiecutter.__package_name.upper() }}_DATABASE_URL=sqlite:///./examples.db
{% endif %}
```

### Running All Examples

```bash
# Run basic examples
{% if cookiecutter.use_src_layout %}
PYTHONPATH=src python examples/basic_usage.py
{% else %}
python examples/basic_usage.py
{% endif %}

{% if cookiecutter.include_cli_example %}
# Test CLI examples
python examples/cli_examples.py
{% endif %}

{% if cookiecutter.include_api %}
# Start API server (in another terminal)
uvicorn {{ cookiecutter.__package_name }}.api:app --reload

# Run API examples
python examples/api_examples.py
{% endif %}
```

## Creating Your Own Examples

When creating new examples:

1. **Follow the existing structure**
2. **Include comprehensive docstrings**
3. **Add error handling**
4. **Make examples self-contained**
5. **Update this README**

### Example Template

```python
"""
Example: [Brief Description]

This example demonstrates [what it does] for {{ cookiecutter.project_name }}.
"""

from {{ cookiecutter.__package_name }} import [imports]


def example_function():
    """Demonstrate [specific functionality]."""
    print("=== [Example Name] ===\n")
    
    # Example code here
    
    print("✅ Example completed\n")


def main():
    """Run the example."""
    print("{{ cookiecutter.project_name }} - [Example Name]")
    print("=" * 50)
    
    example_function()
    
    print("For more information, see:")
    print("- Documentation: [URL]")
    print("- API Reference: [URL]")


if __name__ == "__main__":
    main()
```

## Interactive Examples

Some examples include interactive components:

{% if cookiecutter.include_cli_example %}
- **CLI Examples**: Interactive command-line prompts
{% endif %}
{% if cookiecutter.include_api %}
- **API Examples**: Real API calls to running server
{% endif %}
- **Configuration Examples**: Dynamic configuration loading

## Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Make sure you're in the project root
   cd {{ cookiecutter.project_slug }}
   
   # Set Python path for src layout
   {% if cookiecutter.use_src_layout %}
   export PYTHONPATH=src
   {% endif %}
   ```

2. **Missing Dependencies**
   ```bash
   # Install all dependencies
   {% if cookiecutter.package_manager == "poetry" %}
   poetry install --all-extras
   {% elif cookiecutter.package_manager == "uv" %}
   uv sync --all-extras --dev
   {% else %}
   pip install -e .[all]
   {% endif %}
   ```

3. **Configuration Issues**
   ```bash
   # Check configuration
   python -c "from {{ cookiecutter.__package_name }}.config import get_config; print(get_config())"
   ```

{% if cookiecutter.include_api %}
4. **API Connection Issues**
   ```bash
   # Make sure API server is running
   uvicorn {{ cookiecutter.__package_name }}.api:app --reload
   
   # Test API health
   curl http://localhost:8000/health
   ```
{% endif %}

### Getting Help

- Check the main [README.md](../README.md)
- Review [DEVELOPMENT.md](../DEVELOPMENT.md)
- See the [documentation]({{ cookiecutter.project_url }})
- Open an [issue]({{ cookiecutter.project_repository }}/issues) if you find bugs

## Contributing Examples

We welcome contributions of new examples! Please:

1. **Fork the repository**
2. **Create a new example file**
3. **Update this README**
4. **Test your example**
5. **Submit a pull request**

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines.