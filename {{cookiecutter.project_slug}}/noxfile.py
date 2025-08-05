"""
Nox configuration for {{ cookiecutter.project_name }}

Nox is a tool for running tests in multiple environments.
This configuration provides sessions for testing, linting, type checking, and documentation.
"""

import nox

# Python versions to test against
PYTHON_VERSIONS = ["{{ cookiecutter.python_version }}", "3.12", "3.11", "3.10"]
{% if cookiecutter.python_version == "3.9" or cookiecutter.python_version == "3.8" %}
PYTHON_VERSIONS.extend(["3.9", "3.8"])
{% endif %}

# Package manager configuration
{% if cookiecutter.package_manager == "uv" %}
PACKAGE_MANAGER = "uv"
{% elif cookiecutter.package_manager == "poetry" %}
PACKAGE_MANAGER = "poetry"
{% else %}
PACKAGE_MANAGER = "pip"
{% endif %}

nox.options.sessions = [
    "tests",
    "lint",
    "type_check",
    {% if cookiecutter.include_security %}"security",{% endif %}
    {% if cookiecutter.include_docs_site %}"docs",{% endif %}
]
nox.options.reuse_existing_virtualenvs = True


def install_dependencies(session, dev=False, docs=False):
    """Install dependencies using the configured package manager."""
    {% if cookiecutter.package_manager == "uv" %}
    session.install("uv")
    if dev:
        session.run("uv", "sync", "--dev", external=True)
    elif docs:
        session.run("uv", "sync", "--group", "docs", external=True)
    else:
        session.run("uv", "sync", external=True)
    {% elif cookiecutter.package_manager == "poetry" %}
    session.install("poetry")
    if dev:
        session.run("poetry", "install", external=True)
    elif docs:
        session.run("poetry", "install", "--with", "docs", external=True)
    else:
        session.run("poetry", "install", "--no-dev", external=True)
    {% else %}
    if dev:
        session.install("-e", ".[dev]")
    elif docs:
        session.install("-e", ".[docs]")
    else:
        session.install("-e", ".")
    {% endif %}


@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    """Run the test suite."""
    install_dependencies(session, dev=True)
    
    # Run tests with coverage
    session.run(
        "pytest",
        "--cov={{ cookiecutter.__package_name }}",
        "--cov-report=term-missing",
        "--cov-report=xml",
        "--cov-report=html",
        "tests/",
        *session.posargs
    )


@nox.session(python="{{ cookiecutter.python_version }}")
def lint(session):
    """Run linting tools."""
    install_dependencies(session, dev=True)
    
    {% if cookiecutter.linter == "ruff" %}
    session.run("ruff", "check", "{{ cookiecutter.__package_name }}", "tests")
    {% elif cookiecutter.linter == "pylint" %}
    session.run("pylint", "{{ cookiecutter.__package_name }}", "tests")
    {% elif cookiecutter.linter == "flake8" %}
    session.run("flake8", "{{ cookiecutter.__package_name }}", "tests")
    {% endif %}


@nox.session(python="{{ cookiecutter.python_version }}")
def format_check(session):
    """Check code formatting."""
    install_dependencies(session, dev=True)
    
    {% if cookiecutter.code_style == "black" %}
    session.run("black", "--check", "{{ cookiecutter.__package_name }}", "tests")
    {% elif cookiecutter.code_style == "ruff-format" %}
    session.run("ruff", "format", "--check", "{{ cookiecutter.__package_name }}", "tests")
    {% endif %}
    
    {% if cookiecutter.import_sorter == "isort" %}
    session.run("isort", "--check-only", "{{ cookiecutter.__package_name }}", "tests")
    {% endif %}


@nox.session(python="{{ cookiecutter.python_version }}")
def format_fix(session):
    """Fix code formatting."""
    install_dependencies(session, dev=True)
    
    {% if cookiecutter.code_style == "black" %}
    session.run("black", "{{ cookiecutter.__package_name }}", "tests")
    {% elif cookiecutter.code_style == "ruff-format" %}
    session.run("ruff", "format", "{{ cookiecutter.__package_name }}", "tests")
    {% endif %}
    
    {% if cookiecutter.import_sorter == "isort" %}
    session.run("isort", "{{ cookiecutter.__package_name }}", "tests")
    {% endif %}


@nox.session(python="{{ cookiecutter.python_version }}")
def type_check(session):
    """Run type checking."""
    install_dependencies(session, dev=True)
    
    {% if cookiecutter.type_checker == "mypy" %}
    session.run("mypy", "{{ cookiecutter.__package_name }}")
    {% elif cookiecutter.type_checker == "pyright" %}
    session.run("pyright", "{{ cookiecutter.__package_name }}")
    {% endif %}


{% if cookiecutter.include_security %}
@nox.session(python="{{ cookiecutter.python_version }}")
def security(session):
    """Run security checks."""
    install_dependencies(session, dev=True)
    
    session.run("bandit", "-r", "{{ cookiecutter.__package_name }}")
    session.run("safety", "check")
{% endif %}


@nox.session(python="{{ cookiecutter.python_version }}")
def benchmark(session):
    """Run performance benchmarks."""
    install_dependencies(session, dev=True)
    
    session.run("pytest", "--benchmark-only", "--benchmark-sort=mean", "tests/")


{% if cookiecutter.include_docs_site %}
@nox.session(python="{{ cookiecutter.python_version }}")
def docs(session):
    """Build documentation."""
    install_dependencies(session, docs=True)
    
    # Install Node.js dependencies for docs
    session.run("npm", "install", "--prefix", "docs", external=True)
    session.run("npm", "run", "build", "--prefix", "docs", external=True)


@nox.session(python="{{ cookiecutter.python_version }}")
def docs_serve(session):
    """Serve documentation locally."""
    install_dependencies(session, docs=True)
    
    session.run("npm", "install", "--prefix", "docs", external=True)
    session.run("npm", "run", "dev", "--prefix", "docs", external=True)
{% endif %}


@nox.session(python="{{ cookiecutter.python_version }}")
def build(session):
    """Build the package."""
    install_dependencies(session, dev=True)
    
    {% if cookiecutter.package_manager == "poetry" %}
    session.run("poetry", "build", external=True)
    {% else %}
    session.install("build")
    session.run("python", "-m", "build")
    {% endif %}


@nox.session(python="{{ cookiecutter.python_version }}")
def clean(session):
    """Clean build artifacts."""
    import shutil
    from pathlib import Path
    
    # Directories to clean
    clean_dirs = [
        "build",
        "dist", 
        "*.egg-info",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".coverage",
        "htmlcov",
        "reports",
    ]
    
    for pattern in clean_dirs:
        for path in Path(".").glob(f"**/{pattern}"):
            if path.is_dir():
                session.log(f"Removing directory: {path}")
                shutil.rmtree(path)
            elif path.is_file():
                session.log(f"Removing file: {path}")
                path.unlink()


@nox.session(python=PYTHON_VERSIONS)
def test_matrix(session):
    """Run tests across Python version matrix."""
    install_dependencies(session, dev=True)
    
    session.run("pytest", "tests/", "-v")


@nox.session(python="{{ cookiecutter.python_version }}")
def coverage(session):
    """Generate and report test coverage."""
    install_dependencies(session, dev=True)
    
    session.run(
        "pytest",
        "--cov={{ cookiecutter.__package_name }}",
        "--cov-report=term-missing",
        "--cov-report=html:htmlcov",
        "--cov-report=xml:coverage.xml",
        "--cov-fail-under=80",
        "tests/"
    )
    
    session.log("Coverage report generated in htmlcov/index.html")


@nox.session(python="{{ cookiecutter.python_version }}")
def pre_commit(session):
    """Run pre-commit hooks."""
    install_dependencies(session, dev=True)
    
    session.run("pre-commit", "run", "--all-files")


@nox.session(python="{{ cookiecutter.python_version }}")
def release_check(session):
    """Run all checks before release."""
    install_dependencies(session, dev=True)
    
    # Run all quality checks
    session.run("pytest", "tests/")
    
    {% if cookiecutter.linter == "ruff" %}
    session.run("ruff", "check", "{{ cookiecutter.__package_name }}", "tests")
    {% endif %}
    
    {% if cookiecutter.type_checker == "mypy" %}
    session.run("mypy", "{{ cookiecutter.__package_name }}")
    {% endif %}
    
    {% if cookiecutter.include_security %}
    session.run("bandit", "-r", "{{ cookiecutter.__package_name }}")
    session.run("safety", "check")
    {% endif %}
    
    # Build package
    {% if cookiecutter.package_manager == "poetry" %}
    session.run("poetry", "build", external=True)
    {% else %}
    session.install("build")
    session.run("python", "-m", "build")
    {% endif %}
    
    session.log("✅ All release checks passed!")