# Project Scripts

This directory contains utility scripts for the project.

## setup_env.sh

Environment setup script that configures a complete development environment for both the template and generated projects.

### Features

- Flexible configuration via command line arguments, environment variables, config files
- Parallel component installation with dependency resolution
- Smart version detection and management
- Automatic retry mechanism for failed installations
- Progress tracking with resume capability
- Atomic shell configuration management
- Cross-platform package management
- Comprehensive logging and debugging support
- CI/CD optimized with automated mode
- Cross-platform support (Linux, macOS)

### Configuration

The script can be configured through multiple methods (in order of precedence):

1. Command line arguments
2. Environment variables
3. Configuration file (.setupenv.conf)
4. Project files (cookiecutter.json, pyproject.toml)
5. Default values

Configuration file example (.setupenv.conf):
```

### Usage

Basic usage:

```bash
./scripts/setup_env.sh
```

Options:

- `-h, --help`: Show help message
- `-v, --version`: Show script version
- `-s, --skip-checks`: Skip system requirement checks
- `-d, --debug`: Enable debug mode
- `-r, --resume`: Resume from last successful step
- `-f, --force`: Force reinstallation of components
- `--python-version`: Specify Python version
- `--node-version`: Specify Node.js version
- `--poetry-version`: Specify Poetry version
- `--nvm-version`: Specify NVM version

Example with specific versions:

```bash
./scripts/setup_env.sh --python-version 3.10.0 --poetry-version 1.4.0
```

### Integration

The script integrates with:

1. cookiecutter.json for template defaults
2. pyproject.toml for project-specific versions
3. package.json for documentation dependencies
