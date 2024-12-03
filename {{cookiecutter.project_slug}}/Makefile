# numanac project Makefile

.ONESHELL:

# https://www.gnu.org/prep/standards/html_node/Makefile-Basics.html#Makefile-Basics
SHELL = /bin/bash

help:           ## Show this help.
	fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'


notebook:  ## Launch jupyter lab from project root
	echo "Starting Jupyter Lab..."
	poetry shell && poetry install --with notebook
	poetry run jupyter lab

format: ## Run formatters on the numanac package
	echo "Running formatters..."
	poetry shell && poetry install
	poetry run isort numanac/ tests/
	poetry run autoflake --recursive numanac/ tests/
	poetry run yapf -i --recursive numanac/ tests/

lint: ## Run linters on the numanac package
	echo "Running linters..."
	poetry shell && poetry install
	poetry run ruff check numanac/ tests/
	poetry run mypy numanac/ tests/
	poetry run pylint numanac/ tests/

test: ## Run tests on the numanac package
	echo "Running tests..."
	poetry shell && poetry install
	poetry run pytest tests/