{% if cookiecutter.include_docker %}
# Multi-stage Dockerfile for {{ cookiecutter.project_name }}
# Optimized for production with minimal image size and security best practices

# Build stage
FROM python:{{ cookiecutter.python_version }}-slim as builder

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install package manager
{% if cookiecutter.package_manager == "uv" %}
RUN pip install uv
{% elif cookiecutter.package_manager == "poetry" %}
RUN pip install poetry==1.8.0
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VENV_IN_PROJECT=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache
{% endif %}

# Set work directory
WORKDIR /app

# Copy dependency files
{% if cookiecutter.package_manager == "uv" %}
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev
{% elif cookiecutter.package_manager == "poetry" %}
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev && rm -rf $POETRY_CACHE_DIR
{% else %}
COPY pyproject.toml ./
RUN pip install -e .
{% endif %}

# Production stage
FROM python:{{ cookiecutter.python_version }}-slim as production

# Create non-root user
RUN groupadd --gid 1000 appuser \
    && useradd --uid 1000 --gid appuser --shell /bin/bash --create-home appuser

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH="/app/src"

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Set work directory and copy application
WORKDIR /app

# Copy virtual environment from builder stage
{% if cookiecutter.package_manager in ["uv", "poetry"] %}
COPY --from=builder /app/.venv /app/.venv
{% endif %}

# Copy application code
{% if cookiecutter.use_src_layout %}
COPY src/ ./src/
{% else %}
COPY {{ cookiecutter.__package_name }}/ ./{{ cookiecutter.__package_name }}/
{% endif %}

COPY README.md LICENSE ./

# Create necessary directories and set permissions
RUN mkdir -p /app/logs /app/data \
    && chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Health check
{% if cookiecutter.include_api %}
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1
{% elif cookiecutter.include_cli_example %}
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -m {{ cookiecutter.__package_name }}.cli health-check || exit 1
{% endif %}

# Expose port
{% if cookiecutter.include_api %}
EXPOSE 8000
{% endif %}

# Labels for metadata
LABEL maintainer="{{ cookiecutter.full_name }} <{{ cookiecutter.email }}>" \
      version="{{ cookiecutter.project_version }}" \
      description="{{ cookiecutter.project_description }}" \
      org.opencontainers.image.source="{{ cookiecutter.project_repository }}" \
      org.opencontainers.image.documentation="{{ cookiecutter.project_url }}" \
      org.opencontainers.image.vendor="{{ cookiecutter.full_name }}" \
      org.opencontainers.image.licenses="{{ cookiecutter.license_type.split(' (')[0] if '(' in cookiecutter.license_type else cookiecutter.license_type }}"

# Default command
{% if cookiecutter.include_api %}
CMD ["python", "-m", "{{ cookiecutter.__package_name }}.api"]
{% elif cookiecutter.include_cli_example %}
CMD ["python", "-m", "{{ cookiecutter.__package_name }}.cli", "--help"]
{% else %}
CMD ["python", "-c", "print('{{ cookiecutter.project_name }} Docker container is running!')"]
{% endif %}
{% endif %}