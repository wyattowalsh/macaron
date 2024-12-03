#!/usr/bin/env bash

# This script is part of the cookiecutter-python-project template.
# It sets up a complete development environment with Python, Poetry, Node.js,
# and documentation tools.

# Initialize configuration with defaults
: "${SKIP_CHECKS:=0}"
: "${DEBUG:=0}"
: "${RESUME:=0}"
: "${FORCE:=0}"
: "${CI:=0}"
: "${COMPONENTS:=all}"
: "${PYTHON_VERSION:=3.11.4}"
: "${NODE_VERSION:=18.17.1}"
: "${POETRY_VERSION:=1.5.1}"
: "${NVM_VERSION:=0.39.5}"
: "${PRE_COMMIT_VERSION:=3.3.3}"

# Set strict error handling
# shellcheck disable=SC1090,SC1091,SC2059,SC2086
set -euo pipefail
IFS=$'\n\t'

# Script version
SCRIPT_VERSION="1.0.0"

# Color codes for pretty output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Determine script and project paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
CACHE_DIR="${SCRIPT_DIR}/.cache"
PROGRESS_FILE="${CACHE_DIR}/.setup_env_progress"
VERSION_CACHE="${CACHE_DIR}/.version_cache"
DOCS_DIR="${TEMPLATE_ROOT}/docs"

# Available components
declare -A AVAILABLE_COMPONENTS=(
    ["python"]="Python environment (pyenv)"
    ["poetry"]="Poetry package manager"
    ["node"]="Node.js environment (nvm)"
    ["docs"]="Documentation tools"
    ["pre-commit"]="Pre-commit hooks"
    ["all"]="All components"
)

# Add configuration file support
CONFIG_FILE="${SCRIPT_DIR}/.setupenv.conf"
[[ -f "${CONFIG_FILE}" ]] && source "${CONFIG_FILE}"

# Additional configuration defaults
: "${PARALLEL:=1}"
: "${MAX_RETRIES:=3}"
: "${TIMEOUT:=1800}"
: "${LOG_LEVEL:=info}"

# Component dependencies
declare -A COMPONENT_DEPS=(
    ["poetry"]="python"
    ["docs"]="node"
    ["pre-commit"]="python"
)

# Functions for logging
log() {
    local level=$1
    local msg=$2
    local color=""
    case $level in
        "INFO") color=$BLUE ;;
        "OK") color=$GREEN ;;
        "WARN") color=$YELLOW ;;
        "FAIL") color=$RED ;;
    esac
    printf "\r\033[2K  [ %s%s%s ] %s\n" "$color" "$level" "$NC" "$msg"
    [[ "${DEBUG:-0}" -eq 1 ]] && echo "[$(date '+%Y-%m-%d %H:%M:%S')] $level: $msg" >&2
}

info() { log "INFO" "$1"; }
success() { log "OK" "$1"; }
warning() { log "WARN" "$1"; }
fail() { log "FAIL" "$1"; echo ''; exit 1; }

# Shell configuration manager with atomic updates
manage_shell_config() {
    local config_type=$1
    local shell_config
    local temp_config
    
    # Determine shell config file
    if [ -n "${ZSH_VERSION:-}" ]; then
        shell_config="$HOME/.zshrc"
    else
        shell_config="$HOME/.bashrc"
    fi
    
    temp_config=$(mktemp)
    
    # Copy existing config
    cp "$shell_config" "$temp_config"
    
    # Marker for configuration sections
    local start_marker="# >>> $config_type configuration >>>"
    local end_marker="# <<< $config_type configuration <<<"
    
    # Remove existing configuration if present
    if grep -q "$start_marker" "$temp_config"; then
        sed -i.bak "/$start_marker/,/$end_marker/d" "$temp_config"
    fi
    
    # Add new configuration
    {
        echo "$start_marker"
        case $config_type in
            "pyenv")
                echo 'export PYENV_ROOT="$HOME/.pyenv"'
                echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"'
                echo 'eval "$(pyenv init -)"'
                ;;
            "poetry")
                echo 'export PATH="$HOME/.local/bin:$PATH"'
                ;;
            "nvm")
                echo 'export NVM_DIR="$HOME/.nvm"'
                echo '[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"'
                echo '[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"'
                ;;
        esac
        echo "$end_marker"
        echo ''
    } >> "$temp_config"
    
    # Atomically update config file
    mv "$temp_config" "$shell_config"
}

# Detect project context and set variables
detect_project_context() {
    if [[ -f "${TEMPLATE_ROOT}/cookiecutter.json" ]]; then
        PROJECT_CONTEXT="template"
        PROJECT_NAME="cookiecutter-python-project"
        PROJECT_ROOT="${TEMPLATE_ROOT}"
    else
        PROJECT_CONTEXT="project"
        PROJECT_ROOT="${TEMPLATE_ROOT}"
        PROJECT_NAME=$(basename "${PROJECT_ROOT}")
    fi
    
    info "Detected context: ${PROJECT_CONTEXT} (${PROJECT_NAME})"
}

# Cache version information
cache_versions() {
    mkdir -p "${CACHE_DIR}"
    {
        echo "PYTHON_VERSION=${PYTHON_VERSION}"
        echo "NODE_VERSION=${NODE_VERSION}"
        echo "POETRY_VERSION=${POETRY_VERSION}"
        echo "NVM_VERSION=${NVM_VERSION}"
        echo "PRE_COMMIT_VERSION=${PRE_COMMIT_VERSION}"
    } > "${VERSION_CACHE}"
}

# Load cached versions
load_cached_versions() {
    if [[ -f "${VERSION_CACHE}" ]]; then
        # shellcheck source=/dev/null
        source "${VERSION_CACHE}"
    fi
}

# System package manager detection and installation
pkg_install() {
    local packages=("$@")
    
    if [[ "$(uname -s)" == "Darwin" ]]; then
        if ! command -v brew >/dev/null 2>&1; then
            warning "Homebrew not found. Installing..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            # Add Homebrew to PATH for current session
            eval "$(/opt/homebrew/bin/brew shellenv)"
        fi
        HOMEBREW_NO_AUTO_UPDATE=1 brew install "${packages[@]}" || true
    else
        if command -v apt >/dev/null 2>&1; then
            sudo apt update
            sudo apt install -y "${packages[@]}"
        elif command -v yum >/dev/null 2>&1; then
            sudo yum install -y "${packages[@]}"
        elif command -v pacman >/dev/null 2>&1; then
            sudo pacman -Sy --noconfirm "${packages[@]}"
        elif command -v apk >/dev/null 2>&1; then
            sudo apk add --no-cache "${packages[@]}"
        else
            fail "No supported package manager found (apt, yum, pacman, apk)"
        fi
    fi
}

# Component installation status tracking
is_component_installed() {
    local component=$1
    case $component in
        "python")
            command -v pyenv >/dev/null 2>&1 && \
            pyenv versions | grep -q "$PYTHON_VERSION"
            ;;
        "poetry")
            command -v poetry >/dev/null 2>&1 && \
            [[ "$(poetry --version | cut -d' ' -f3)" == "$POETRY_VERSION" ]]
            ;;
        "node")
            command -v node >/dev/null 2>&1 && \
            [[ "$(node -v)" == "v$NODE_VERSION" ]]
            ;;
        "docs")
            [[ -d "$DOCS_DIR" && -f "${DOCS_DIR}/package.json" && -d "${DOCS_DIR}/node_modules" ]]
            ;;
        "pre-commit")
            command -v pre-commit >/dev/null 2>&1 && \
            [[ "$(pre-commit --version | cut -d' ' -f2)" == "$PRE_COMMIT_VERSION" ]]
            ;;
        *)
            return 1
            ;;
    esac
}

# Function to sync versions with project files
sync_versions() {
    info "Detecting project versions..."
    
    if [[ -f "${TEMPLATE_ROOT}/cookiecutter.json" ]]; then
        local py_version
        py_version=$(grep -o '"python_version": *"[^"]*"' "${TEMPLATE_ROOT}/cookiecutter.json" | cut -d'"' -f4)
        if [[ -n "$py_version" ]]; then
            PYTHON_VERSION=$py_version
            info "Using Python version ${PYTHON_VERSION} from cookiecutter.json"
        fi
    fi
    
    if [[ -f "${PROJECT_ROOT}/pyproject.toml" ]]; then
        local poetry_version node_version
        poetry_version=$(grep '^poetry-version = ' "${PROJECT_ROOT}/pyproject.toml" | cut -d'"' -f2 || echo "")
        node_version=$(grep '^node-version = ' "${PROJECT_ROOT}/pyproject.toml" | cut -d'"' -f2 || echo "")
        
        [[ -n "$poetry_version" ]] && POETRY_VERSION=$poetry_version
        [[ -n "$node_version" ]] && NODE_VERSION=$node_version
    fi
    
    cache_versions
}

# Cleanup function
cleanup() {
    local exit_code=$?
    
    if [[ $exit_code -ne 0 ]]; then
        if [[ -n "${COMPLETED_STEPS[*]:-}" ]]; then
            mkdir -p "${CACHE_DIR}"
            printf "%s\n" "${!COMPLETED_STEPS[@]}" > "$PROGRESS_FILE"
        fi
        
        if [[ "${DEBUG:-0}" -eq 1 ]]; then
            warning "Script failed with exit code $exit_code"
            warning "Debug info saved to ${CACHE_DIR}/setup_env_debug.log"
        fi
    else
        rm -f "$PROGRESS_FILE"
    fi
    
    exit $exit_code
}

# Print components
print_components() {
    echo "Available components:"
    for comp in "${!AVAILABLE_COMPONENTS[@]}"; do
        printf "  %-12s %s\n" "$comp" "${AVAILABLE_COMPONENTS[$comp]}"
    done
}

# Print help information
print_help() {
    cat << EOF
Development Environment Setup Script v${SCRIPT_VERSION}

Usage: $0 [options]

This script sets up a complete development environment for ${PROJECT_NAME}.
It can be run both in the template root and in generated projects.

Options:
    -h, --help              Show this help message
    -v, --version          Show script version
    -s, --skip-checks      Skip system requirement checks
    -d, --debug            Enable debug mode (verbose output)
    -r, --resume           Resume from last successful step
    -f, --force            Force reinstallation of components
    -c, --components       Comma-separated list of components to install
                          (default: all)
    --ci                   Run in CI mode (minimal output, no prompts)
    --python-version       Specify Python version
    --node-version         Specify Node.js version
    --poetry-version       Specify Poetry version
    --nvm-version          Specify NVM version
    --pre-commit-version   Specify pre-commit version

Components:
$(print_components)

Example:
    $0 --python-version 3.10.0 --components=python,poetry

Environment variables:
    DEBUG                 Enable debug mode
    CI                    Enable CI mode
    FORCE                 Force reinstallation
    SKIP_CHECKS          Skip system checks
    COMPONENTS           Components to install
    *_VERSION            Override tool versions

The script will detect and use versions from:
1. Command line arguments
2. Environment variables
3. cookiecutter.json (in template)
4. pyproject.toml (in project)
5. Default values
EOF
    exit 0
}

# Parse command line arguments
parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                print_help
                ;;
            -v|--version)
                echo "v${SCRIPT_VERSION}"
                exit 0
                ;;
            -s|--skip-checks)
                SKIP_CHECKS=1
                shift
                ;;
            -d|--debug)
                DEBUG=1
                mkdir -p "${CACHE_DIR}"
                exec 19>&2
                exec 2> >(tee "${CACHE_DIR}/setup_env_debug.log")
                set -x
                shift
                ;;
            -r|--resume)
                RESUME=1
                shift
                ;;
            -f|--force)
                FORCE=1
                shift
                ;;
            -c|--components)
                COMPONENTS=$2
                shift 2
                ;;
            --ci)
                CI=1
                shift
                ;;
            --python-version)
                PYTHON_VERSION=$2
                shift 2
                ;;
            --node-version)
                NODE_VERSION=$2
                shift 2
                ;;
            --poetry-version)
                POETRY_VERSION=$2
                shift 2
                ;;
            --nvm-version)
                NVM_VERSION=$2
                shift 2
                ;;
            --pre-commit-version)
                PRE_COMMIT_VERSION=$2
                shift 2
                ;;
            *)
                echo "Unknown option: $1"
                print_help
                ;;
        esac
    done
}

# Initialize environment
init_environment() {
    # Create cache directory
    mkdir -p "${CACHE_DIR}"
    
    # Load cached versions if not forced
    [[ $FORCE -eq 0 ]] && load_cached_versions
    
    # Load progress if resuming
    if [[ $RESUME -eq 1 && -f "$PROGRESS_FILE" ]]; then
        info "Resuming from previous progress..."
        while IFS= read -r step; do
            COMPLETED_STEPS[$step]=1
        done < "$PROGRESS_FILE"
    fi
    
    # Parse components
    if [[ "$COMPONENTS" != "all" ]]; then
        IFS=',' read -ra SELECTED_COMPONENTS <<< "$COMPONENTS"
        for comp in "${SELECTED_COMPONENTS[@]}"; do
            if [[ ! ${AVAILABLE_COMPONENTS[$comp]+_} ]]; then
                fail "Invalid component: $comp"
            fi
        done
    fi
    
    # Sync versions with project files
    sync_versions
}

# Function to check if a component should be installed
should_install_component() {
    local component=$1
    [[ "$COMPONENTS" == "all" ]] || [[ " ${SELECTED_COMPONENTS[*]} " =~ " ${component} " ]]
}

# Set up trap for cleanup
trap cleanup EXIT INT TERM

# Installation functions for each component
install_python() {
    if ! command -v pyenv >/dev/null 2>&1; then
        if [[ "$(uname -s)" == "Darwin" ]]; then
            pkg_install pyenv
        else
            curl https://pyenv.run | bash
        fi
        manage_shell_config "pyenv"
        
        export PYENV_ROOT="$HOME/.pyenv"
        export PATH="$PYENV_ROOT/bin:$PATH"
        eval "$(pyenv init -)"
    fi

    if ! pyenv versions | grep -q "$PYTHON_VERSION" || [[ $FORCE -eq 1 ]]; then
        PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install "$PYTHON_VERSION"
        pyenv global "$PYTHON_VERSION"
    fi
    success "Python ${PYTHON_VERSION} installed successfully"
}

install_poetry() {
    if command -v poetry >/dev/null 2>&1; then
        current_version=$(poetry --version | cut -d' ' -f3)
        if [ "$current_version" = "$POETRY_VERSION" ] && [[ $FORCE -eq 0 ]]; then
            info "Poetry ${POETRY_VERSION} already installed."
            return
        fi
    fi

    if [[ "$(uname -s)" == "Darwin" ]]; then
        pkg_install "poetry"
    else
        curl -sSL https://install.python-poetry.org | POETRY_VERSION=$POETRY_VERSION python3 -
    fi
    manage_shell_config "poetry"

    export PATH="$HOME/.local/bin:$PATH"
    poetry config virtualenvs.in-project true
    poetry config virtualenvs.create true
    poetry config experimental.system-git-client true

    success "Poetry ${POETRY_VERSION} installed successfully"
}

install_node() {
    if [ ! -d "$HOME/.nvm" ] || [[ $FORCE -eq 1 ]]; then
        if [[ "$(uname -s)" == "Darwin" ]]; then
            pkg_install nvm
        else
            curl -o- "https://raw.githubusercontent.com/nvm-sh/nvm/v${NVM_VERSION}/install.sh" | bash
        fi
        manage_shell_config "nvm"
        
        export NVM_DIR="$HOME/.nvm"
        [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
    fi

    if ! command -v node >/dev/null 2>&1 || [ "$(node -v)" != "v${NODE_VERSION}" ] || [[ $FORCE -eq 1 ]]; then
        nvm install "$NODE_VERSION"
        nvm use "$NODE_VERSION"
        nvm alias default "$NODE_VERSION"
    fi
    success "Node.js ${NODE_VERSION} installed successfully"
}

install_docs() {
    if ! command -v npx >/dev/null 2>&1; then
        fail "npm is not installed. Please ensure Node.js installation was successful."
    fi

    if [[ -d "$DOCS_DIR" ]]; then
        cd "$DOCS_DIR"
        if [[ -f package.json ]]; then
            npm install
        fi
        cd - > /dev/null
    fi
    success "Documentation dependencies installed successfully"
}

install_pre-commit() {
    if [[ "$(uname -s)" == "Darwin" ]]; then
        pkg_install pre-commit
    else
        pip install "pre-commit==$PRE_COMMIT_VERSION"
    fi

    if [[ -f .pre-commit-config.yaml ]]; then
        pre-commit install --install-hooks
    fi
    success "Pre-commit ${PRE_COMMIT_VERSION} installed successfully"
}

install_with_retry() {
    local component=$1
    local retries=0
    local max_retries=$MAX_RETRIES
    
    while [[ $retries -lt $max_retries ]]; do
        if install_"${component}"; then
            return 0
        fi
        ((retries++))
        warning "Retry $retries/$max_retries for $component"
        sleep $((retries * 2))
    done
    return 1
}

parallel_install() {
    local components=("$@")
    local pids=()
    local failed=()
    
    for comp in "${components[@]}"; do
        if [[ ${COMPONENT_DEPS[$comp]+_} ]]; then
            for dep in ${COMPONENT_DEPS[$comp]}; do
                if ! is_component_installed "$dep"; then
                    install_with_retry "$dep"
                fi
            done
        fi
        
        (install_with_retry "$comp") &
        pids+=($!)
    done
    
    for pid in "${pids[@]}"; do
        if ! wait "$pid"; then
            failed+=("${components[i]}")
        fi
    done
    
    [[ ${#failed[@]} -eq 0 ]]
}

# Main installation process
main() {
    detect_project_context
    
    echo "=== Development Environment Setup Script v${SCRIPT_VERSION} ==="
    echo "Setting up development environment for: ${PROJECT_NAME}"
    echo ""
    
    # Parse command line arguments
    parse_args "$@"
    
    # Initialize environment
    init_environment
    
    echo "Components to install:"
    if [[ "$COMPONENTS" == "all" ]]; then
        echo "- All available components"
    else
        for comp in "${SELECTED_COMPONENTS[@]}"; do
            echo "- ${comp} (${AVAILABLE_COMPONENTS[$comp]})"
        done
    fi
    echo ""
    
    # Install components
    if [[ $PARALLEL -eq 1 ]]; then
        local parallel_comps=()
        for comp in "${!AVAILABLE_COMPONENTS[@]}"; do
            if should_install_component "$comp"; then
                parallel_comps+=("$comp")
            fi
        done
        
        if ! parallel_install "${parallel_comps[@]}"; then
            fail "Some components failed to install"
        fi
    else
        for comp in "${!AVAILABLE_COMPONENTS[@]}"; do
            if should_install_component "$comp"; then
                info "Installing ${comp}..."
                "install_${comp}"
            fi
        done
    fi
    
    echo ""
    success "Development environment setup complete!"
    
    if [[ $CI -eq 0 ]]; then
        warning "Please restart your terminal or run:"
        echo "source ~/.bashrc  # for bash"
        echo "source ~/.zshrc   # for zsh"
        echo ""
        info "To verify installations, run:"
        [[ "$COMPONENTS" == "all" || " ${SELECTED_COMPONENTS[*]} " =~ " python " ]] && \
            echo "python --version  # should show ${PYTHON_VERSION}"
        [[ "$COMPONENTS" == "all" || " ${SELECTED_COMPONENTS[*]} " =~ " poetry " ]] && \
            echo "poetry --version  # should show ${POETRY_VERSION}"
        [[ "$COMPONENTS" == "all" || " ${SELECTED_COMPONENTS[*]} " =~ " node " ]] && \
            echo "node --version    # should show ${NODE_VERSION}"
        [[ "$COMPONENTS" == "all" || " ${SELECTED_COMPONENTS[*]} " =~ " pre-commit " ]] && \
            echo "pre-commit --version  # should show ${PRE_COMMIT_VERSION}"
    fi
}

# Run main function
main "$@"