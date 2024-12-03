<div align='center'>
    <img src="./docs/static/img/banner.png" alt="macaron project banner" />
    <h1>🍪 macaron</h1>
    <p><em>A cookiecutter bundle of the best Python project resources</em></p>
</div>

<div align="center">

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL%203.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Documentation](https://img.shields.io/badge/docs-w4w.dev%2Fmacaron-blue)](https://w4w.dev/macaron)
[![GitHub Issues](https://img.shields.io/github/issues/wyattowalsh/macaron)](https://github.com/wyattowalsh/macaron/issues)

</div>

## 🚀 Quick Start

Make sure you have [pipx](https://github.com/pypa/pipx) installed, then run:

```bash
pipx install cookiecutter
pipx run cookiecutter gh:wyattowalsh/macaron
```

## 🛠️ Development Environment Setup

The project includes a comprehensive environment setup script (`setup_env.sh`) that configures a complete development environment.

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

### Usage

Basic setup:

```bash
./scripts/setup_env.sh
```

Options:

- `-h, --help`: Show help message
- `-v, --version`: Show script version
- `-s, --skip-checks`: Skip system requirement checks
- `-d, --debug`: Enable debug mode
- `-r, --resume`: Resume from last successful step

### Configuration

The setup script can be configured through multiple methods (in order of precedence):

1. Command line arguments
2. Environment variables
3. Configuration file (.setupenv.conf)
4. Project files (cookiecutter.json, pyproject.toml)
5. Default values

## 📚 Documentation

For complete documentation, please visit [macaron.w4w.dev](https://macaron.w4w.dev)
