#  {{cookiecutter.project_name}} Makefile

.ONESHELL:

# https://www.gnu.org/prep/standards/html_node/Makefile-Basics.html#Makefile-Basics
SHELL = /bin/bash

help:           ## Show this help.
	fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

notebook:  ## Launch jupyter lab from project root
	echo "Starting Jupyter Lab..."
	poetry shell && poetry install --with notebook
	poetry run jupyter lab

format: ## Run formatters on the {{cookiecutter.project_name}} package
	echo "Running formatters..."
	poetry shell && poetry install
	poetry run isort {{cookiecutter.project_name}}/ tests/
	poetry run autoflake --recursive {{cookiecutter.project_name}}/ tests/
	poetry run yapf -i --recursive {{cookiecutter.project_name}}/ tests/

lint: ## Run linters on the {{cookiecutter.project_name}} package
	echo "Running linters..."
	poetry shell && poetry install
	poetry run ruff check {{cookiecutter.project_name}}/ tests/
	poetry run mypy {{cookiecutter.project_name}}/ tests/
	poetry run pylint {{cookiecutter.project_name}}/ tests/

test: ## Run tests on the {{cookiecutter.project_name}} package
	echo "Running tests..."
	poetry shell && poetry install
	poetry run pytest tests/