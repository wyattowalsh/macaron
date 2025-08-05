# {{ cookiecutter.project_name }} - Development Makefile
# 
# This Makefile provides convenient commands for development, testing, and deployment.
# It supports multiple package managers and provides comprehensive tooling integration.

.ONESHELL:

# Configuration
PYTHON_VERSION := {{ cookiecutter.python_version }}
PACKAGE_NAME := {{ cookiecutter.__package_name }}
PROJECT_SLUG := {{ cookiecutter.project_slug }}

# Package manager detection and configuration
{% if cookiecutter.package_manager == "uv" %}
PACKAGE_MANAGER := uv
RUN_CMD := uv run
INSTALL_CMD := uv sync
INSTALL_DEV_CMD := uv sync --dev
INSTALL_ALL_CMD := uv sync --all-extras --dev
{% elif cookiecutter.package_manager == "poetry" %}
PACKAGE_MANAGER := poetry
RUN_CMD := poetry run
INSTALL_CMD := poetry install --no-dev
INSTALL_DEV_CMD := poetry install
INSTALL_ALL_CMD := poetry install --all-extras
{% else %}
PACKAGE_MANAGER := pip
RUN_CMD := python -m
INSTALL_CMD := pip install -e .
INSTALL_DEV_CMD := pip install -e .[dev]
INSTALL_ALL_CMD := pip install -e .[all]
{% endif %}

# https://www.gnu.org/prep/standards/html_node/Makefile-Basics.html#Makefile-Basics
SHELL = /bin/bash

# Colors for pretty output
RED := \033[0;31m
GREEN := \033[0;32m
YELLOW := \033[1;33m
BLUE := \033[0;34m
PURPLE := \033[0;35m
CYAN := \033[0;36m
WHITE := \033[1;37m
RESET := \033[0m

# Default target
.DEFAULT_GOAL := help

help: ## Show this help.
	@echo "$(CYAN){{ cookiecutter.project_name }} - Development Commands$(RESET)"
	@echo "$(WHITE)======================================$(RESET)"
	@echo ""
	@echo "$(YELLOW)Package Manager:$(RESET) $(PACKAGE_MANAGER)"
	@echo "$(YELLOW)Python Version:$(RESET) $(PYTHON_VERSION)"
	@echo ""
	@echo "$(WHITE)Available commands:$(RESET)"
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//' | sed -e 's/^/  /'
	@echo ""

# Installation targets
install: ## Install production dependencies only
	@echo "$(BLUE)Installing production dependencies...$(RESET)"
	$(INSTALL_CMD)

install-dev: ## Install development dependencies
	@echo "$(BLUE)Installing development dependencies...$(RESET)"
	$(INSTALL_DEV_CMD)

install-all: ## Install all dependencies including optional extras
	@echo "$(BLUE)Installing all dependencies...$(RESET)"
	$(INSTALL_ALL_CMD)

# Development environment setup
setup: install-dev setup-pre-commit ## Set up development environment
	@echo "$(GREEN)Development environment setup complete!$(RESET)"

{% if cookiecutter.include_pre_commit %}
setup-pre-commit: ## Install and configure pre-commit hooks
	@echo "$(BLUE)Setting up pre-commit hooks...$(RESET)"
	$(RUN_CMD) pre-commit install
	$(RUN_CMD) pre-commit install --hook-type commit-msg
	@echo "$(GREEN)Pre-commit hooks installed!$(RESET)"
{% else %}
setup-pre-commit: ## Pre-commit not configured
	@echo "$(YELLOW)Pre-commit hooks not configured in this project$(RESET)"
{% endif %}

{% if cookiecutter.include_notebooks %}
notebook: ## Launch jupyter lab from project root
	@echo "$(BLUE)Starting Jupyter Lab...$(RESET)"
	$(RUN_CMD) jupyter lab
{% endif %}

# Code quality targets
{% if cookiecutter.code_style == "black" %}
format: ## Format code with Black
	@echo "$(BLUE)Formatting code with Black...$(RESET)"
	$(RUN_CMD) black $(PACKAGE_NAME) tests
{% elif cookiecutter.code_style == "ruff-format" %}
format: ## Format code with Ruff
	@echo "$(BLUE)Formatting code with Ruff...$(RESET)"
	$(RUN_CMD) ruff format $(PACKAGE_NAME) tests
{% elif cookiecutter.code_style == "yapf" %}
format: ## Format code with YAPF
	@echo "$(BLUE)Formatting code with YAPF...$(RESET)"
	$(RUN_CMD) yapf -i --recursive $(PACKAGE_NAME) tests
{% else %}
format: ## Code formatting not configured
	@echo "$(YELLOW)Code formatting not configured$(RESET)"
{% endif %}

{% if cookiecutter.linter == "ruff" %}
lint: ## Run Ruff linter
	@echo "$(BLUE)Running Ruff linter...$(RESET)"
	$(RUN_CMD) ruff check $(PACKAGE_NAME) tests
{% elif cookiecutter.linter == "pylint" %}
lint: ## Run Pylint
	@echo "$(BLUE)Running Pylint...$(RESET)"
	$(RUN_CMD) pylint $(PACKAGE_NAME) tests
{% elif cookiecutter.linter == "flake8" %}
lint: ## Run Flake8
	@echo "$(BLUE)Running Flake8...$(RESET)"
	$(RUN_CMD) flake8 $(PACKAGE_NAME) tests
{% else %}
lint: ## Linting not configured
	@echo "$(YELLOW)Linting not configured$(RESET)"
{% endif %}

{% if cookiecutter.type_checker == "mypy" %}
type-check: ## Run MyPy type checking
	@echo "$(BLUE)Running MyPy type checking...$(RESET)"
	$(RUN_CMD) mypy $(PACKAGE_NAME) tests
{% elif cookiecutter.type_checker == "pyright" %}
type-check: ## Run Pyright type checking
	@echo "$(BLUE)Running Pyright type checking...$(RESET)"
	$(RUN_CMD) pyright $(PACKAGE_NAME) tests
{% else %}
type-check: ## Type checking not configured
	@echo "$(YELLOW)Type checking not configured$(RESET)"
{% endif %}

quality: format lint type-check ## Run all code quality checks

# Testing targets
test: ## Run tests on the {{ cookiecutter.project_name }} package
	@echo "$(BLUE)Running tests...$(RESET)"
	$(RUN_CMD) pytest tests/

test-cov: ## Run tests with coverage
	@echo "$(BLUE)Running tests with coverage...$(RESET)"
	$(RUN_CMD) pytest --cov=$(PACKAGE_NAME) --cov-report=term-missing --cov-report=html tests/

test-fast: ## Run fast tests only (skip slow tests)
	@echo "$(BLUE)Running fast tests...$(RESET)"
	$(RUN_CMD) pytest -m "not slow" tests/

# Build and release targets
build: clean ## Build wheel and source distribution
	@echo "$(BLUE)Building package...$(RESET)"
{% if cookiecutter.package_manager == "poetry" %}
	poetry build
{% else %}
	python -m build
{% endif %}

clean: ## Clean build artifacts
	@echo "$(BLUE)Cleaning build artifacts...$(RESET)"
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete
	rm -fr .coverage htmlcov/ .pytest_cache/ .mypy_cache/

{% if cookiecutter.include_docs_site %}
docs: ## Build documentation
	@echo "$(BLUE)Building documentation...$(RESET)"
	cd docs && npm run build

docs-serve: ## Serve documentation locally
	@echo "$(BLUE)Serving documentation locally...$(RESET)"
	cd docs && npm run dev
{% endif %}

# Utility targets
info: ## Show project information
	@echo "$(CYAN){{ cookiecutter.project_name }}$(RESET)"
	@echo "$(WHITE)==================$(RESET)"
	@echo "$(YELLOW)Version:$(RESET) {{ cookiecutter.project_version }}"
	@echo "$(YELLOW)Package:$(RESET) $(PACKAGE_NAME)"
	@echo "$(YELLOW)Python:$(RESET) $(PYTHON_VERSION)"
	@echo "$(YELLOW)Package Manager:$(RESET) $(PACKAGE_MANAGER)"

all: setup quality test build ## Run complete development pipeline
	@echo "$(GREEN)Complete development pipeline finished!$(RESET)"