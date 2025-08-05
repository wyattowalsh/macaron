# Contributing to {{ cookiecutter.project_name }}

Thank you for your interest in contributing to {{ cookiecutter.project_name }}! This document provides guidelines and information for contributors.

## 🚀 Quick Start

1. Fork the repository
2. Clone your fork: `git clone {{ cookiecutter.project_repository }}.git`
3. Set up development environment: `make setup`
4. Create a feature branch: `git checkout -b feature/your-feature-name`
5. Make your changes and add tests
6. Run quality checks: `make quality test`
7. Commit your changes: `git commit -m "feat: add amazing feature"`
8. Push to your fork: `git push origin feature/your-feature-name`
9. Create a Pull Request

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Code Style and Standards](#code-style-and-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Release Process](#release-process)

## 📜 Code of Conduct

This project adheres to a code of conduct adapted from the [Contributor Covenant](https://www.contributor-covenant.org/). By participating, you are expected to uphold this code.

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

- **Be respectful**: Use welcoming and inclusive language
- **Be collaborative**: Disagreement is no excuse for poor behavior
- **Be constructive**: Focus on what is best for the community
- **Be responsible**: Own up to mistakes and learn from them

## 🤝 How to Contribute

### Types of Contributions

We welcome several types of contributions:

- 🐛 **Bug Reports**: Help us identify and fix bugs
- ✨ **Feature Requests**: Suggest new features or improvements
- 💻 **Code Contributions**: Implement features, fix bugs, improve performance
- 📝 **Documentation**: Improve docs, tutorials, or examples
- 🧪 **Testing**: Add tests, improve test coverage, or test infrastructure
- 🎨 **Design**: UI/UX improvements, graphics, or visual design
- 🔍 **Code Review**: Review pull requests and provide feedback

### What We're Looking For

- **Bug fixes**: Always welcome, especially with tests
- **Feature implementations**: Check existing issues or discuss first
- **Performance improvements**: Benchmarks and metrics appreciated
- **Documentation improvements**: Examples, tutorials, API docs
- **Test coverage**: Help us reach our coverage goals
- **Developer experience**: Tooling, setup, and workflow improvements

## 🛠️ Development Setup

### Prerequisites

- Python {{ cookiecutter.python_version }}+
{% if cookiecutter.package_manager == "poetry" %}- Poetry 1.8+{% elif cookiecutter.package_manager == "uv" %}- uv{% endif %}
- Git
{% if cookiecutter.include_docker %}- Docker and Docker Compose (optional){% endif %}
- Node.js 18+ (for documentation)

### Environment Setup

```bash
# Clone the repository
git clone {{ cookiecutter.project_repository }}.git
cd {{ cookiecutter.project_slug }}

# Set up development environment
make setup

# Verify setup
make info
```

### Development Tools

We use several tools to maintain code quality:

- **{{ cookiecutter.linter }}**: Code linting
- **{{ cookiecutter.code_style }}**: Code formatting
- **{{ cookiecutter.type_checker }}**: Static type checking
{% if cookiecutter.include_security %}- **Bandit**: Security analysis
- **Safety**: Dependency vulnerability checking{% endif %}
{% if cookiecutter.include_pre_commit %}- **Pre-commit**: Git hooks for automated checks{% endif %}
- **Pytest**: Testing framework
- **Nox**: Testing in multiple environments

### Available Commands

```bash
make help                 # Show all available commands
make setup               # Set up development environment
make test                # Run tests
make test-cov            # Run tests with coverage
make quality             # Run all quality checks
make format              # Format code
make lint                # Run linter
make type-check          # Run type checker
make security            # Run security checks
make docs                # Build documentation
make clean               # Clean build artifacts
```

## 🎨 Code Style and Standards

### Python Code Style

- **Formatter**: {{ cookiecutter.code_style }}
- **Line length**: 88 characters
- **Import sorting**: {{ cookiecutter.import_sorter if cookiecutter.import_sorter != "none" else "Manual" }}
- **Type hints**: Required for public APIs
- **Docstrings**: Google style for all public functions/classes

### Code Quality Requirements

- **Test coverage**: Minimum 80% for new code
- **Type checking**: No type errors allowed
- **Linting**: No linting errors allowed
- **Security**: No security issues from Bandit
- **Dependencies**: No known vulnerabilities

### Code Organization

{% if cookiecutter.use_src_layout %}
```
src/{{ cookiecutter.__package_name }}/
├── __init__.py          # Package initialization and public API
├── core.py              # Core functionality and base classes
├── config.py            # Configuration management
{% if cookiecutter.include_cli_example %}├── cli.py               # Command-line interface{% endif %}
{% if cookiecutter.include_api %}├── api.py               # REST API endpoints{% endif %}
└── utils.py             # Utility functions
```
{% else %}
```
{{ cookiecutter.__package_name }}/
├── __init__.py          # Package initialization and public API
├── core.py              # Core functionality and base classes
├── config.py            # Configuration management
{% if cookiecutter.include_cli_example %}├── cli.py               # Command-line interface{% endif %}
{% if cookiecutter.include_api %}├── api.py               # REST API endpoints{% endif %}
└── utils.py             # Utility functions
```
{% endif %}

### Naming Conventions

- **Functions/variables**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Files/modules**: `snake_case.py`
- **Private members**: `_leading_underscore`

## 🧪 Testing Guidelines

### Test Structure

```
tests/
├── conftest.py          # Shared fixtures and configuration
├── test_core.py         # Core functionality tests
├── test_config.py       # Configuration tests
{% if cookiecutter.include_cli_example %}├── test_cli.py          # CLI tests{% endif %}
{% if cookiecutter.include_api %}├── test_api.py          # API tests{% endif %}
└── integration/         # Integration tests
    └── test_workflows.py
```

### Testing Requirements

- **Unit tests**: For all public functions and methods
- **Integration tests**: For key workflows and external dependencies
- **Parametrized tests**: For testing multiple inputs/scenarios
- **Mock testing**: For external services and complex dependencies
- **Performance tests**: For critical performance paths

### Test Categories

Mark tests with appropriate pytest markers:

```python
@pytest.mark.unit
def test_basic_functionality():
    """Test basic functionality."""
    pass

@pytest.mark.integration  
def test_database_integration():
    """Test database integration."""
    pass

@pytest.mark.slow
def test_performance():
    """Test performance characteristics."""
    pass
```

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run specific test categories
pytest -m "unit"                    # Unit tests only
pytest -m "integration"             # Integration tests only
pytest -m "not slow"                # Skip slow tests

# Run tests in parallel
pytest -n auto

# Run specific test file
pytest tests/test_core.py

# Run with debugging
pytest -s -vv tests/test_core.py::test_specific_function
```

## 📚 Documentation

### Documentation Standards

- **Docstrings**: Required for all public APIs
- **Type hints**: Include type information
- **Examples**: Provide usage examples
- **Error handling**: Document exceptions raised

### Docstring Format

```python
def process_data(data: List[Dict], validate: bool = True) -> ProcessResult:
    """Process input data and return results.
    
    Args:
        data: List of dictionaries containing raw data
        validate: Whether to validate input data before processing
        
    Returns:
        ProcessResult containing processed data and metadata
        
    Raises:
        ValidationError: If data validation fails
        ProcessingError: If data processing fails
        
    Example:
        >>> data = [{"id": 1, "value": "test"}]
        >>> result = process_data(data)
        >>> print(result.count)
        1
    """
```

### Building Documentation

{% if cookiecutter.include_docs_site %}
```bash
# Build documentation
make docs

# Serve documentation locally
make docs-serve

# Clean documentation build
make docs-clean
```
{% endif %}

## 📝 Commit Message Guidelines

{% if cookiecutter.include_commitizen %}
We use [Conventional Commits](https://www.conventionalcommits.org/) with Commitizen:

### Commit Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, etc.)
- **refactor**: Code refactoring without functional changes
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **build**: Build system or dependency changes
- **ci**: CI configuration changes
- **chore**: Other changes (maintenance, etc.)

### Commit Format

```
type(scope): short description

Longer description if needed

Fixes #123
```

### Examples

```bash
feat(api): add user authentication endpoint
fix(cli): handle missing config file gracefully
docs(readme): update installation instructions
test(core): add tests for edge cases
```

### Using Commitizen

```bash
# Interactive commit
cz commit

# Or use git with conventional format
git commit -m "feat: add new feature"
```
{% else %}
### Commit Message Format

Use clear, descriptive commit messages:

```
Add user authentication to API

- Implement JWT token generation
- Add login/logout endpoints  
- Update tests for authentication
- Update documentation

Fixes #123
```
{% endif %}

## 🔄 Pull Request Process

### Before Creating a PR

1. **Create an issue** for discussion (for new features)
2. **Fork the repository** and create a feature branch
3. **Make your changes** following our standards
4. **Add tests** for your changes
5. **Update documentation** if needed
6. **Run quality checks**: `make quality test`
7. **Commit your changes** following our guidelines

### PR Requirements

- ✅ **Tests pass**: All existing and new tests must pass
- ✅ **Quality checks pass**: Linting, type checking, security
- ✅ **Documentation updated**: If applicable
- ✅ **Changelog updated**: For user-facing changes
- ✅ **No merge conflicts**: Rebase on latest main if needed

### PR Description Template

Our PR template includes:

- **Description**: What does this PR do?
- **Related Issues**: Link to relevant issues
- **Type of Change**: Bug fix, feature, documentation, etc.
- **Testing**: How was this tested?
- **Checklist**: Quality, documentation, security checks

### Review Process

1. **Automated checks**: CI must pass
2. **Code review**: At least one maintainer review
3. **Discussion**: Address reviewer feedback
4. **Approval**: Get approval from maintainer
5. **Merge**: Squash and merge (usually)

## 🐛 Issue Reporting

### Before Reporting

1. **Search existing issues** to avoid duplicates
2. **Check documentation** for known limitations
3. **Test with latest version** if possible
4. **Gather relevant information** (OS, Python version, etc.)

### Bug Report Template

Include:

- **Bug description**: Clear description of the issue
- **Steps to reproduce**: Detailed reproduction steps
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: OS, Python version, package version
- **Error messages**: Full error output if applicable

### Feature Request Template

Include:

- **Feature description**: Clear description of the feature
- **Motivation**: Why is this feature needed?
- **Use cases**: Specific scenarios where this helps
- **Implementation ideas**: If you have suggestions
- **Alternatives considered**: Other approaches you've thought about

## 🚀 Release Process

### Version Management

{% if cookiecutter.include_commitizen %}
We use semantic versioning with Commitizen:

```bash
# Bump version automatically
cz bump

# Manual version bump
cz bump --increment PATCH|MINOR|MAJOR
```
{% else %}
We follow [Semantic Versioning](https://semver.org/):

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)
{% endif %}

### Release Checklist

- [ ] All tests pass
- [ ] Documentation is updated
- [ ] CHANGELOG.md is updated
- [ ] Version is bumped appropriately
- [ ] Release notes are prepared
- [ ] CI/CD pipeline passes

### Release Types

- **Alpha/Beta**: Pre-release versions for testing
- **Release Candidate**: Final testing before stable release
- **Stable**: Production-ready release
- **Hotfix**: Critical bug fixes

## 🎯 Getting Help

### Community Resources

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and community discussion
- **Documentation**: [{{ cookiecutter.project_url }}]({{ cookiecutter.project_url }})

### Maintainers

- **{{ cookiecutter.full_name }}** ([@{{ cookiecutter.github }}](https://github.com/{{ cookiecutter.github }})) - Project Lead

### Response Times

- **Bug reports**: Within 48 hours
- **Feature requests**: Within 1 week
- **Pull requests**: Within 1 week
- **Security issues**: Within 24 hours

## 🏆 Recognition

Contributors are recognized in:

- **CONTRIBUTORS.md**: All contributors listed
- **Release notes**: Major contributors highlighted
- **Documentation**: Contributor acknowledgments

## 📄 License

By contributing to {{ cookiecutter.project_name }}, you agree that your contributions will be licensed under the {{ cookiecutter.license_type.split(' (')[0] if '(' in cookiecutter.license_type else cookiecutter.license_type }} License.

---

Thank you for contributing to {{ cookiecutter.project_name }}! 🎉