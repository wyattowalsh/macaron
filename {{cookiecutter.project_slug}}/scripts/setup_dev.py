#!/usr/bin/env python3
"""
Setup script for {{ cookiecutter.project_name }} development environment

This script automates the setup of a complete development environment
with all necessary tools and configurations.
"""

import os
import subprocess
import sys
import platform
from pathlib import Path
from typing import List, Optional

try:
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.panel import Panel
    from rich.prompt import Confirm
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False


class DevelopmentSetup:
    """Handles development environment setup."""
    
    def __init__(self):
        self.console = Console() if RICH_AVAILABLE else None
        self.project_dir = Path.cwd()
        self.system = platform.system()
        
    def print(self, message: str, style: str = "white") -> None:
        """Print message with optional styling."""
        if self.console:
            self.console.print(message, style=style)
        else:
            print(message)
    
    def run_command(self, command: List[str], check: bool = True) -> bool:
        """Run a command and return success status."""
        try:
            self.print(f"Running: {' '.join(command)}", "dim")
            result = subprocess.run(command, check=check, capture_output=True, text=True)
            if result.stdout:
                self.print(result.stdout, "dim")
            return True
        except subprocess.CalledProcessError as e:
            self.print(f"Command failed: {e}", "red")
            if e.stderr:
                self.print(f"Error: {e.stderr}", "red")
            return False
        except FileNotFoundError:
            self.print(f"Command not found: {command[0]}", "red")
            return False
    
    def check_tool(self, tool: str, version_arg: str = "--version") -> bool:
        """Check if a tool is available."""
        try:
            subprocess.run([tool, version_arg], capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def install_python_tools(self) -> bool:
        """Install Python development tools."""
        self.print("\n📦 Installing Python development tools...", "blue")
        
        # Check Python version
        if sys.version_info < ({{ cookiecutter.python_version.split('.')[0] }}, {{ cookiecutter.python_version.split('.')[1] }}):
            self.print(f"❌ Python {{ cookiecutter.python_version }}+ required, got {sys.version}", "red")
            return False
        
        {% if cookiecutter.package_manager == "poetry" %}
        # Install Poetry if not available
        if not self.check_tool("poetry"):
            self.print("Installing Poetry...", "yellow")
            if not self.run_command([
                sys.executable, "-m", "pip", "install", "poetry>=1.8.0"
            ]):
                return False
        
        # Install dependencies
        return self.run_command(["poetry", "install", "--all-extras"])
        
        {% elif cookiecutter.package_manager == "uv" %}
        # Install uv if not available
        if not self.check_tool("uv"):
            self.print("Installing uv...", "yellow")
            if not self.run_command([
                sys.executable, "-m", "pip", "install", "uv"
            ]):
                return False
        
        # Install dependencies
        return self.run_command(["uv", "sync", "--all-extras", "--dev"])
        
        {% else %}
        # Install with pip
        return self.run_command([
            sys.executable, "-m", "pip", "install", "-e", ".[all]"
        ])
        {% endif %}
    
    def setup_git_hooks(self) -> bool:
        """Set up Git hooks."""
        self.print("\n🪝 Setting up Git hooks...", "blue")
        
        {% if cookiecutter.include_pre_commit %}
        # Install pre-commit hooks
        if not self.run_command([sys.executable, "-m", "pre_commit", "install"]):
            return False
        
        if not self.run_command([
            sys.executable, "-m", "pre_commit", "install", "--hook-type", "commit-msg"
        ]):
            return False
        
        # Run pre-commit on all files
        self.print("Running pre-commit on all files...", "yellow")
        self.run_command([sys.executable, "-m", "pre_commit", "run", "--all-files"], check=False)
        {% endif %}
        
        return True
    
    def setup_development_config(self) -> bool:
        """Set up development configuration."""
        self.print("\n⚙️ Setting up development configuration...", "blue")
        
        # Create development config file
        dev_config = self.project_dir / "config.dev.yaml"
        if not dev_config.exists():
            config_content = f"""# Development configuration for {{ cookiecutter.project_name }}
app_name: "{{ cookiecutter.project_name }} (Development)"
debug: true
log_level: DEBUG
environment: development

{% if cookiecutter.include_api %}
# API settings
api_host: "0.0.0.0"
api_port: 8000
api_reload: true
{% endif %}

{% if cookiecutter.include_database %}
# Database settings
database_url: "sqlite:///./{{ cookiecutter.project_slug }}_dev.db"
database_echo: true
{% endif %}

# Development settings
max_workers: 2
timeout: 60.0
"""
            
            with open(dev_config, "w", encoding="utf-8") as f:
                f.write(config_content)
            
            self.print(f"Created development config: {dev_config}", "green")
        
        # Create .env file for development
        env_file = self.project_dir / ".env"
        if not env_file.exists():
            env_content = f"""# Development environment variables for {{ cookiecutter.project_name }}
{{ cookiecutter.__package_name.upper() }}_ENVIRONMENT=development
{{ cookiecutter.__package_name.upper() }}_DEBUG=true
{{ cookiecutter.__package_name.upper() }}_LOG_LEVEL=DEBUG

{% if cookiecutter.include_api %}
# API configuration
{{ cookiecutter.__package_name.upper() }}_API_HOST=localhost
{{ cookiecutter.__package_name.upper() }}_API_PORT=8000
{{ cookiecutter.__package_name.upper() }}_API_RELOAD=true
{% endif %}

{% if cookiecutter.include_database %}
# Database configuration
{{ cookiecutter.__package_name.upper() }}_DATABASE_URL=sqlite:///./{{ cookiecutter.project_slug }}_dev.db
{{ cookiecutter.__package_name.upper() }}_DATABASE_ECHO=true
{% endif %}
"""
            
            with open(env_file, "w", encoding="utf-8") as f:
                f.write(env_content)
            
            self.print(f"Created environment file: {env_file}", "green")
        
        return True
    
    def create_development_scripts(self) -> bool:
        """Create useful development scripts."""
        self.print("\n📝 Creating development scripts...", "blue")
        
        scripts_dir = self.project_dir / "scripts"
        scripts_dir.mkdir(exist_ok=True)
        
        # Development server script
        {% if cookiecutter.include_api %}
        dev_server_script = scripts_dir / "dev_server.py"
        if not dev_server_script.exists():
            script_content = '''#!/usr/bin/env python3
"""Development server for {{ cookiecutter.project_name }}"""

import subprocess
import sys
from pathlib import Path

def main():
    """Start development server with hot reload."""
    project_dir = Path(__file__).parent.parent
    
    # Start the API server with reload
    cmd = [
        sys.executable, "-m", "uvicorn",
        "{{ cookiecutter.__package_name }}.api:app",
        "--reload",
        "--host", "0.0.0.0",
        "--port", "8000",
        "--log-level", "debug"
    ]
    
    print(f"Starting development server: {' '.join(cmd)}")
    subprocess.run(cmd, cwd=project_dir)

if __name__ == "__main__":
    main()
'''
            
            with open(dev_server_script, "w", encoding="utf-8") as f:
                f.write(script_content)
            
            dev_server_script.chmod(0o755)
            self.print(f"Created development server script: {dev_server_script}", "green")
        {% endif %}
        
        return True
    
    def verify_setup(self) -> bool:
        """Verify the development setup."""
        self.print("\n✅ Verifying setup...", "blue")
        
        # Test import
        try:
            {% if cookiecutter.use_src_layout %}
            sys.path.insert(0, str(self.project_dir / "src"))
            {% endif %}
            import {{ cookiecutter.__package_name }}
            self.print(f"✅ Package import successful: {{ cookiecutter.__package_name }} v{{{ cookiecutter.__package_name }}.__version__}", "green")
        except ImportError as e:
            self.print(f"❌ Package import failed: {e}", "red")
            return False
        
        # Test basic functionality
        try:
            from {{ cookiecutter.__package_name }}.core import hello_world
            result = hello_world("Setup")
            self.print(f"✅ Core functionality test: {result}", "green")
        except Exception as e:
            self.print(f"❌ Core functionality test failed: {e}", "red")
            return False
        
        # Test configuration
        try:
            from {{ cookiecutter.__package_name }}.config import get_config
            config = get_config()
            self.print(f"✅ Configuration test: {config.app_name}", "green")
        except Exception as e:
            self.print(f"❌ Configuration test failed: {e}", "red")
            return False
        
        return True
    
    def run_setup(self) -> bool:
        """Run the complete setup process."""
        if self.console:
            self.console.print(Panel(
                "🚀 Setting up {{ cookiecutter.project_name }} Development Environment",
                title="Development Setup",
                border_style="green"
            ))
        else:
            print("=== Development Setup ===")
        
        setup_steps = [
            ("Python Tools", self.install_python_tools),
            ("Git Hooks", self.setup_git_hooks),
            ("Development Config", self.setup_development_config),
            ("Development Scripts", self.create_development_scripts),
            ("Verification", self.verify_setup),
        ]
        
        if RICH_AVAILABLE:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=self.console,
            ) as progress:
                for name, step_func in setup_steps:
                    task = progress.add_task(f"Setting up {name}...", total=None)
                    success = step_func()
                    if success:
                        progress.update(task, description=f"[green]✅ {name} completed[/green]")
                    else:
                        progress.update(task, description=f"[red]❌ {name} failed[/red]")
                        return False
        else:
            for name, step_func in setup_steps:
                print(f"Setting up {name}...")
                if not step_func():
                    print(f"❌ {name} failed")
                    return False
                print(f"✅ {name} completed")
        
        return True


def main():
    """Main entry point."""
    setup = DevelopmentSetup()
    
    try:
        success = setup.run_setup()
        
        if success:
            setup.print("\n🎉 Development environment setup completed successfully!", "green")
            setup.print("\nNext steps:", "blue")
            setup.print("  1. Run tests: make test", "white")
            setup.print("  2. Start development: make dev", "white")
            {% if cookiecutter.include_api %}
            setup.print("  3. Start API server: python scripts/dev_server.py", "white")
            {% endif %}
            setup.print("  4. See all commands: make help", "white")
        else:
            setup.print("\n❌ Setup failed. Please check the errors above.", "red")
            sys.exit(1)
    
    except KeyboardInterrupt:
        setup.print("\n⚠️ Setup interrupted by user", "yellow")
        sys.exit(1)
    except Exception as e:
        setup.print(f"\n❌ Setup error: {e}", "red")
        sys.exit(1)


if __name__ == "__main__":
    main()