# Development Guide for {{ cookiecutter.project_name }}

This document provides detailed information for developers working on {{ cookiecutter.project_name }}.

## 🏗️ Architecture Overview

{{ cookiecutter.project_name }} is built with a modular architecture that emphasizes:

- **Separation of concerns**: Clear boundaries between components
- **Testability**: Easy to test individual components
- **Extensibility**: Simple to add new features
- **Maintainability**: Clean, well-documented code

### Project Structure

{% if cookiecutter.use_src_layout %}
```
{{ cookiecutter.project_slug }}/
├── src/{{ cookiecutter.__package_name }}/     # Main package source code
│   ├── __init__.py                 # Package initialization and public API
│   ├── core.py                     # Core functionality and base classes
│   ├── config.py                   # Configuration management
│   {% if cookiecutter.include_cli_example %}├── cli.py                      # Command-line interface{% endif %}
│   {% if cookiecutter.include_api %}├── api.py                      # REST API endpoints{% endif %}
│   └── utils.py                    # Utility functions
├── tests/                          # Test suite
│   ├── conftest.py                 # Shared test configuration
│   ├── test_core.py                # Core functionality tests
│   ├── test_config.py              # Configuration tests
│   {% if cookiecutter.include_cli_example %}├── test_cli.py                 # CLI tests{% endif %}
│   {% if cookiecutter.include_api %}├── test_api.py                 # API tests{% endif %}
│   └── integration/                # Integration tests
├── docs/                           # Documentation
├── scripts/                        # Development and deployment scripts
{% if cookiecutter.include_notebooks %}├── notebooks/                      # Jupyter notebooks{% endif %}
{% if cookiecutter.include_examples %}├── examples/                       # Usage examples{% endif %}
├── .github/                        # GitHub configuration
├── pyproject.toml                  # Project configuration
├── Makefile                        # Development commands
{% if cookiecutter.include_docker %}├── Dockerfile                      # Container configuration
├── docker-compose.yml              # Multi-service setup{% endif %}
└── README.md                       # Project overview
```
{% else %}
```
{{ cookiecutter.project_slug }}/
├── {{ cookiecutter.__package_name }}/           # Main package source code
│   ├── __init__.py                 # Package initialization and public API
│   ├── core.py                     # Core functionality and base classes
│   ├── config.py                   # Configuration management
│   {% if cookiecutter.include_cli_example %}├── cli.py                      # Command-line interface{% endif %}
│   {% if cookiecutter.include_api %}├── api.py                      # REST API endpoints{% endif %}
│   └── utils.py                    # Utility functions
├── tests/                          # Test suite
├── docs/                           # Documentation
├── scripts/                        # Development and deployment scripts
└── ... (other files)
```
{% endif %}

## 🔧 Development Environment Setup

### Prerequisites

- **Python {{ cookiecutter.python_version }}+**: Primary programming language
{% if cookiecutter.package_manager == "poetry" %}- **Poetry**: Dependency management and packaging{% elif cookiecutter.package_manager == "uv" %}- **uv**: Fast Python package installer and resolver{% endif %}
- **Git**: Version control
- **Make**: Task automation
{% if cookiecutter.include_docker %}- **Docker**: Containerization (optional){% endif %}
- **Node.js**: Documentation build system

### Quick Setup

1. **Clone the repository**:

   ```bash
   git clone {{ cookiecutter.project_repository }}.git
   cd {{ cookiecutter.project_slug }}
   ```

2. **Set up development environment**:

   ```bash
   make setup
   ```

3. **Verify installation**:

   ```bash
   make info
   make test
   ```

### Manual Setup

If you prefer manual setup:

```bash
# Install dependencies
{% if cookiecutter.package_manager == "poetry" %}
poetry install --all-extras
{% elif cookiecutter.package_manager == "uv" %}
uv sync --all-extras --dev
{% else %}
pip install -e .[all]
{% endif %}

# Install pre-commit hooks
{% if cookiecutter.include_pre_commit %}
pre-commit install
pre-commit install --hook-type commit-msg
{% endif %}

# Run tests
make test
```

## 🧪 Testing Strategy

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run specific test types
pytest -m unit                 # Unit tests only
pytest -m integration          # Integration tests only
pytest -m "not slow"           # Skip slow tests

# Run in parallel
pytest -n auto
```

### Test Organization

- **Unit tests**: Test individual functions and classes
- **Integration tests**: Test component interactions
- **API tests**: Test REST API endpoints
- **CLI tests**: Test command-line interface
- **Performance tests**: Benchmark critical paths

## 🎨 Code Quality

### Development Commands

```bash
# Format code
make format

# Run linter
make lint

# Run type checker
make type-check

# Run all quality checks
make quality

# Run security checks
make security
```

### Tools Used

- **{{ cookiecutter.code_style }}**: Code formatting
{% if cookiecutter.import_sorter != "none" %}- **{{ cookiecutter.import_sorter }}**: Import sorting{% endif %}
- **{{ cookiecutter.linter }}**: Code linting
- **{{ cookiecutter.type_checker }}**: Static type checking
{% if cookiecutter.include_security %}- **Bandit**: Security analysis
- **Safety**: Dependency vulnerability scanning{% endif %}

## 🐛 Debugging

### Debug Mode

```bash
# Run with debug logging
{{ cookiecutter.project_slug }} --debug command

# Run API with debug mode
uvicorn {{ cookiecutter.__package_name }}.api:app --reload --log-level debug
```

### Profiling

```bash
# Profile performance
python -m cProfile -o profile.stats script.py
python -m pstats profile.stats

# Memory profiling (if memory_profiler is installed)
python -m memory_profiler script.py
```

## 📝 Documentation

{% if cookiecutter.include_docs_site %}
### Building Documentation

```bash
# Build documentation
make docs

# Serve documentation locally
make docs-serve

# Clean documentation build
make docs-clean
```
{% endif %}

### Code Documentation Standards

- **Docstrings**: Required for all public functions and classes
- **Type hints**: Required for all function signatures
- **Comments**: Only for complex business logic
- **Examples**: Include usage examples in docstrings

## 🚀 Deployment

### Build Process

```bash
# Run full pipeline
make all

# Individual steps
make quality    # Code quality checks
make test       # Run test suite
make security   # Security analysis
make build      # Build package
```

{% if cookiecutter.include_docker %}
### Docker Development

```bash
# Build and run with Docker Compose
docker-compose up --build

# Development mode with hot reload
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```
{% endif %}

## 📊 Performance Monitoring

### Benchmarking

```bash
# Run performance benchmarks
make benchmark

# Profile specific functions
pytest --benchmark-only tests/test_performance.py
```

## 🔐 Security

### Security Checks

```bash
# Run security analysis
make security

# Check dependencies for vulnerabilities
safety check

# Scan code for security issues
bandit -r {{ cookiecutter.__package_name }}
```

## 🤝 Contributing

### Workflow

1. **Create feature branch**: `git checkout -b feature/description`
2. **Make changes**: Implement feature with tests
3. **Run quality checks**: `make quality test`
4. **Commit changes**: Use conventional commit format
5. **Push and create PR**: Follow PR template
6. **Code review**: Address reviewer feedback
7. **Merge**: Squash and merge when approved

### Commit Message Format

{% if cookiecutter.include_commitizen %}
We use [Conventional Commits](https://www.conventionalcommits.org/):

```bash
# Examples
feat: add new authentication feature
fix: resolve memory leak in data processing
docs: update API documentation
test: add integration tests for user workflow
```

Use Commitizen for interactive commits:

```bash
cz commit
```
{% else %}
Use clear, descriptive commit messages:

```bash
git commit -m "Add user authentication feature

- Implement JWT token generation
- Add login/logout endpoints
- Update tests and documentation"
```
{% endif %}

## 🎯 Issue Tracking and Contributions

Please use our GitHub issue templates:

- [🐛 Bug Reports]({{ cookiecutter.project_repository }}/issues/new?template=bug_report.yml)
- [✨ Feature Requests]({{ cookiecutter.project_repository }}/issues/new?template=feature_request.yml)

## 🆘 Troubleshooting

### Common Issues

1. **Import errors**: Check virtual environment activation
2. **Test failures**: Run tests individually to isolate issues
3. **Dependency conflicts**: Update lock file or use fresh environment
4. **Build failures**: Check Python version and dependencies

### Getting Help

- **Documentation**: Check [project documentation]({{ cookiecutter.project_url }})
- **Issues**: Search [existing issues]({{ cookiecutter.project_repository }}/issues)
- **Discussions**: Use [GitHub Discussions]({{ cookiecutter.project_repository }}/discussions)

### Debug Information

```bash
# Show environment info
make env

# Show project status
make status

# Show installed packages
{% if cookiecutter.package_manager == "poetry" %}
poetry show
{% elif cookiecutter.package_manager == "uv" %}
uv tree
{% else %}
pip list
{% endif %}
```

---

For more detailed information, see [CONTRIBUTING.md](CONTRIBUTING.md).
