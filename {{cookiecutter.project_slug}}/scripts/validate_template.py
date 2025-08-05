#!/usr/bin/env python3
"""
Template validation script for {{ cookiecutter.project_name }}

This script helps validate the generated project template and ensures
all components are working correctly.
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import List, Optional, Tuple

try:
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.table import Table
    from rich.panel import Panel
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

class ValidationError(Exception):
    """Raised when validation fails."""
    pass

class TemplateValidator:
    """Validates the generated project template."""
    
    def __init__(self, project_dir: Path):
        self.project_dir = Path(project_dir)
        self.console = Console() if RICH_AVAILABLE else None
        self.errors: List[str] = []
        self.warnings: List[str] = []
        
    def print(self, message: str, style: str = "white") -> None:
        """Print message with optional styling."""
        if self.console:
            self.console.print(message, style=style)
        else:
            print(message)
    
    def run_command(self, command: List[str], cwd: Optional[Path] = None) -> Tuple[bool, str]:
        """Run a command and return success status and output."""
        try:
            result = subprocess.run(
                command,
                cwd=cwd or self.project_dir,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            return result.returncode == 0, result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            return False, "Command timed out"
        except Exception as e:
            return False, str(e)
    
    def validate_file_structure(self) -> bool:
        """Validate the basic file structure."""
        self.print("\n🔍 Validating file structure...", "blue")
        
        required_files = [
            "pyproject.toml",
            "README.md",
            "Makefile",
            {% if cookiecutter.use_src_layout %}"src/{{ cookiecutter.__package_name }}/__init__.py",{% else %}"{{ cookiecutter.__package_name }}/__init__.py",{% endif %}
            "tests/test_config.py",
            "tests/test_core.py",
            {% if cookiecutter.include_cli_example %}"tests/test_cli.py",{% endif %}
            {% if cookiecutter.include_api %}"tests/test_api.py",{% endif %}
        ]
        
        optional_files = [
            {% if cookiecutter.include_pre_commit %}".pre-commit-config.yaml",{% endif %}
            {% if cookiecutter.include_docker %}"Dockerfile",
            "docker-compose.yml",{% endif %}
            {% if cookiecutter.include_commitizen %}".cz.toml",{% endif %}
            "noxfile.py",
            "CONTRIBUTING.md",
            "CHANGELOG.md",
            "DEVELOPMENT.md",
        ]
        
        missing_required = []
        missing_optional = []
        
        for file_path in required_files:
            if not (self.project_dir / file_path).exists():
                missing_required.append(file_path)
        
        for file_path in optional_files:
            if not (self.project_dir / file_path).exists():
                missing_optional.append(file_path)
        
        if missing_required:
            self.errors.extend([f"Missing required file: {f}" for f in missing_required])
        
        if missing_optional:
            self.warnings.extend([f"Missing optional file: {f}" for f in missing_optional])
        
        if not missing_required:
            self.print("✅ File structure validation passed", "green")
            return True
        else:
            self.print("❌ File structure validation failed", "red")
            return False
    
    def validate_python_syntax(self) -> bool:
        """Validate Python syntax in all .py files."""
        self.print("\n🐍 Validating Python syntax...", "blue")
        
        python_files = list(self.project_dir.rglob("*.py"))
        syntax_errors = []
        
        for py_file in python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    compile(f.read(), py_file, 'exec')
            except SyntaxError as e:
                syntax_errors.append(f"{py_file}: {e}")
            except Exception as e:
                self.warnings.append(f"Could not check syntax for {py_file}: {e}")
        
        if syntax_errors:
            self.errors.extend(syntax_errors)
            self.print("❌ Python syntax validation failed", "red")
            return False
        else:
            self.print(f"✅ Python syntax validation passed ({len(python_files)} files)", "green")
            return True
    
    def run_validation(self) -> bool:
        """Run all validation checks."""
        if self.console:
            self.console.print(Panel(
                f"🔍 Validating {{ cookiecutter.project_name }} Template",
                title="Template Validator",
                border_style="blue"
            ))
        else:
            print("=== Template Validator ===")
        
        validators = [
            self.validate_file_structure,
            self.validate_python_syntax,
        ]
        
        results = []
        for validator in validators:
            try:
                result = validator()
                results.append(result)
            except Exception as e:
                self.errors.append(f"Validation error in {validator.__name__}: {e}")
                results.append(False)
        
        # Display results
        self.display_results(results)
        
        return all(results) and not self.errors
    
    def display_results(self, results: List[bool]) -> None:
        """Display validation results."""
        if self.console:
            table = Table(title="Validation Results")
            table.add_column("Check", style="cyan")
            table.add_column("Status", style="white")
            
            validators = [
                "File Structure",
                "Python Syntax", 
            ]
            
            for validator, result in zip(validators, results):
                status = "✅ PASS" if result else "❌ FAIL"
                style = "green" if result else "red"
                table.add_row(validator, f"[{style}]{status}[/{style}]")
            
            self.console.print(table)
        else:
            print("\n=== Results ===")
            for i, result in enumerate(results):
                status = "PASS" if result else "FAIL"
                print(f"Check {i+1}: {status}")
        
        # Display errors and warnings
        if self.errors:
            self.print(f"\n❌ Errors ({len(self.errors)}):", "red")
            for error in self.errors:
                self.print(f"  • {error}", "red")
        
        if self.warnings:
            self.print(f"\n⚠️ Warnings ({len(self.warnings)}):", "yellow")
            for warning in self.warnings:
                self.print(f"  • {warning}", "yellow")
        
        if not self.errors and not self.warnings:
            self.print("\n🎉 All validations passed successfully!", "green")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Validate {{ cookiecutter.project_name }} template")
    parser.add_argument(
        "project_dir",
        nargs="?",
        default=".",
        help="Project directory to validate (default: current directory)"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    project_dir = Path(args.project_dir).resolve()
    if not project_dir.exists():
        print(f"Error: Directory {project_dir} does not exist")
        sys.exit(1)
    
    validator = TemplateValidator(project_dir)
    success = validator.run_validation()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()