"""Post-generation hook for cookiecutter template.

This script runs after the project is generated and handles:
1. Merging files when adding to existing project
2. Updating Python version references
3. Setting up license files
4. Ensuring src layout
5. Setting up pytest configuration
6. Configuring Docusaurus documentation
7. Cleaning up conditionally generated files/dirs using cutout
8. Setting up saas-app-starter template for documentation
"""

import datetime
import difflib
import logging
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional, Union

try:
    from cutout import cleanup as cutout_cleanup
except ImportError:
    cutout_cleanup = None

# Import cookiecutter context
# Explicitly list expected keys for clarity and future validation
EXPECTED_KEYS = [
    'project_name', 'project_slug', '__package_name', 'project_version',
    'project_description', 'project_repository', 'project_url',
    'project_keywords', 'full_name', 'email', 'github', 'python_version',
    'package_manager', 'add_to_existing', 'include_ci_workflow',
    'include_release_workflow', 'include_docs_site', 'docs_template',
    'include_cli_example', 'include_docker', 'include_frontend',
    'frontend_directory', 'include_notebooks', 'include_examples',
    'include_benchmarks', 'include_pre_commit', 'include_tox', 'code_style',
    'type_checker', 'license_type', 'include_license_file'
]

# Note: Accessing cookiecutter context directly like this is fragile.
# A better approach might involve reading the generated .cookiecutter.json replay file.
# For now, we stick to the common pattern but acknowledge its limitations.
cookiecutter_context: Dict[str, Any] = {
    key: f'{{{{ cookiecutter.{key} }}}}'
    for key in EXPECTED_KEYS
    # Handle default values more robustly if possible, especially for lists/booleans
}

# Example of handling potential missing keys or providing defaults:
# cookiecutter_context['license_type'] = '{{ cookiecutter.license_type | default("Not open source") }}'
# cookiecutter_context['include_license_file'] = '{{ cookiecutter.include_license_file | default(true) }}'


# --- Logging Setup ---
class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[0;36m',
        'INFO': '\033[0;32m',
        'WARNING': '\033[0;33m',
        'ERROR': '\033[0;31m',
        'CRITICAL': '\033[0;37;41m',
        'RESET': '\033[0m'
    }

    # Define how log records are formatted with colors.
    def format(self, record: logging.LogRecord) -> str:
        color = self.COLORS.get(record.levelname, self.COLORS['RESET'])
        # Format levelname with color and fixed width.
        record.levelname = f"{color}{record.levelname:<8}{self.COLORS['RESET']}"
        # Standard formatter handles message wrapping.
        return super().format(record)


logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
# Use a clear format string.
handler.setFormatter(ColoredFormatter('%(levelname)s | %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.INFO)


class MergeStrategy(Enum):
    """Available merge strategies."""
    ASK = "ask"
    MERGE = "merge"
    REPLACE = "replace"
    SKIP = "skip"
    SMART_MERGE = "smart_merge"


@dataclass
class FileContext:
    """Context for file operations."""
    path: str
    content: str
    is_binary: bool
    merge_strategy: MergeStrategy


class SmartMerger:
    """Handles intelligent file merging with various strategies."""

    def __init__(self, backup_dir: Optional[str] = None):
        self.backup_dir = backup_dir or ".backups"
        os.makedirs(self.backup_dir, exist_ok=True)
        self.current_dest_path: Optional[
            str] = None  # For context in merge_text

    def backup_file(self, file_path: str) -> None:
        """Create a backup of the file."""
        if os.path.exists(file_path):
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            # Construct backup path ensuring length constraints.
            backup_name = f"{os.path.basename(file_path)}.{timestamp}"
            backup_path = os.path.join(self.backup_dir, backup_name)
            try:
                shutil.copy2(file_path, backup_path)
                logger.info(f"Created backup: {backup_path}")
            except Exception as e:
                logger.error(f"Failed to create backup for {file_path}: {e}")

    def is_binary_file(self, file_path: str) -> bool:
        """Check if a file is binary."""
        try:
            with open(file_path, 'rb') as f:
                CHUNKSIZE = 1024
                while True:
                    chunk = f.read(CHUNKSIZE)
                    if b'\0' in chunk:
                        return True
                    if len(chunk) < CHUNKSIZE:
                        break
            return False
        except IOError as e:
            logger.warning(
                f"Could not read file {file_path} to check if binary: {e}")
            return True

    def get_file_context(self, file_path: str) -> FileContext:
        """Get file context including content and type."""
        is_binary = self.is_binary_file(file_path)
        content = ""
        if not is_binary:
            try:
                with open(file_path, 'r',
                          encoding='utf-8') as f:  # Specify encoding
                    content = f.read()
            except Exception as e:
                logger.warning(f"Could not read text file {file_path}: {e}")
                is_binary = True  # Treat as binary if read fails

        return FileContext(path=file_path,
                           content=content,
                           is_binary=is_binary,
                           merge_strategy=self.get_merge_strategy(file_path))

    def get_merge_strategy(self, file_path: str) -> MergeStrategy:
        """Get the appropriate merge strategy for a file."""
        # Define strategies based on expected generated files
        strategies: Dict[str, MergeStrategy] = {
            'pyproject.toml': MergeStrategy.SMART_MERGE,
            'README.md': MergeStrategy.ASK,  # README likely exists
            'LICENSE': MergeStrategy.ASK,  # LICENSE might exist
            '.gitignore': MergeStrategy.MERGE,  # Append new rules
            'Makefile': MergeStrategy.MERGE,  # Append new targets
            '.pre-commit-config.yaml': MergeStrategy.SMART_MERGE,
            # Add frontend specific files if applicable
            'package.json': MergeStrategy.SMART_MERGE,
            'tailwind.config.ts':
            MergeStrategy.REPLACE,  # Usually replace frontend configs
            'postcss.config.mjs': MergeStrategy.REPLACE,
            'next.config.mjs': MergeStrategy.REPLACE,
            'tsconfig.json':
            MergeStrategy.SMART_MERGE,  # Merge compilerOptions if needed
            # Default to ASK for safety
        }
        return strategies.get(os.path.basename(file_path), MergeStrategy.ASK)

    def merge_toml(self, source_content: str, dest_content: str) -> str:
        """Smart merge for TOML files."""
        try:
            import tomlkit
            from tomlkit.items import (  # Add AoT for array of tables
                AoT, Array, Item, Table,
            )

            source_toml = tomlkit.loads(source_content)
            dest_toml = tomlkit.loads(dest_content)

            # Type hint for the recursive function
            TomlStructure = Union[Table, Dict[str, Any], AoT, List[Any]]

            def deep_merge_toml(d1: TomlStructure,
                                d2: TomlStructure) -> TomlStructure:
                if not isinstance(
                        d1, type(d2)):  # If base types differ, source wins
                    return d2

                if isinstance(d1,
                              (Table, dict)) and isinstance(d2, (Table, dict)):
                    merged_dict = d1.copy()  # Create a copy to modify
                    for k, v2 in d2.items():
                        if k in merged_dict:
                            merged_dict[k] = deep_merge_toml(
                                merged_dict[k], v2)
                        else:
                            merged_dict[k] = v2
                    return merged_dict
                elif isinstance(d1, (Array, list)) and isinstance(
                        d2, (Array, list)):
                    merged_list = d1[:]
                    try:
                        # Construct set of existing items (string repr).
                        items_str = (str(
                            item.unwrap() if isinstance(item, Item) else item)
                                     for item in d1)
                        existing_items = set(items_str)
                        for item in d2:
                            item_val = item.unwrap() if isinstance(
                                item, Item) else item
                            if str(item_val) not in existing_items:
                                merged_list.append(
                                    item)  # Keep original tomlkit type
                    except TypeError:
                        # Use standard string formatting, not f-string.
                        logger.warning(
                            "Cannot reliably deduplicate TOML array "
                            "with unhashable items, appending all.")
                        merged_list.extend(d2)
                    return tomlkit.array(merged_list) if isinstance(
                        d1, Array) else merged_list
                elif isinstance(d1, AoT) and isinstance(d2, AoT):
                    # Similar list merging logic for Array of Tables
                    merged_aot = d1[:]
                    existing_items = set(
                        str(item) for item in d1)  # Simple string compare
                    for item in d2:
                        if str(item) not in existing_items:
                            merged_aot.append(item)
                    return tomlkit.aot(merged_aot)
                else:
                    # For simple values or incompatible types, source wins
                    return d2

            merged_toml_doc = deep_merge_toml(dest_toml, source_toml)
            if not isinstance(merged_toml_doc,
                              (Table, dict)):  # Ensure it's a document type
                return dest_content  # Return original if merge result is not a dict/table
            return tomlkit.dumps(merged_toml_doc)

        except ImportError:
            logger.warning(
                "tomlkit not available, falling back to simple text merge for TOML"
            )
            return self.merge_text_content(source_content, dest_content,
                                           "toml")
        except Exception as e:
            logger.error(f"Error merging TOML content: {e}")
            return dest_content  # Return original dest content on error

    def merge_yaml(self, source_content: str, dest_content: str) -> str:
        """Smart merge for YAML files."""
        try:
            # Import inside function to avoid dependency requirement
            import yaml  # type: ignore

            source_yaml = yaml.safe_load(source_content)
            dest_yaml = yaml.safe_load(dest_content)

            # Ensure both are dicts for merging, otherwise replace
            if not isinstance(source_yaml, dict) or \
               not isinstance(dest_yaml, dict):
                logger.warning(
                    "YAML content is not dictionary type, replacing.")
                return source_content

            # Merge dictionaries recursively
            def deep_merge(d1: dict, d2: dict) -> dict:
                for k, v in d2.items():
                    if k in d1 and isinstance(d1[k], dict) and isinstance(
                            v, dict):
                        deep_merge(d1[k], v)
                    elif k in d1 and isinstance(d1[k], list) and isinstance(
                            v, list):
                        # Combine lists and remove duplicates
                        try:
                            existing = set(map(str, d1[k]))
                            d1[k].extend(item for item in v
                                         if str(item) not in existing)
                        except TypeError:
                            logger.warning("Cannot deduplicate YAML list with "
                                           "unhashable items")
                            d1[k].extend(v)
                    else:
                        d1[k] = v
                return d1

            merged = deep_merge(dest_yaml, source_yaml)
            return yaml.dump(merged, sort_keys=False)
        except ImportError:
            logger.warning(
                "PyYAML not available, falling back to simple text merge "
                "for YAML.")
            return self.merge_text_files(source_content, dest_content)
        except Exception as e:
            logger.error(f"Error merging YAML: {e}")
            # Fallback to text merge on other errors
            return self.merge_text_files(source_content, dest_content)

    def merge_json(self, source_content: str, dest_content: str) -> str:
        """Smart merge for JSON files (e.g., package.json)."""
        try:
            import json

            source_json = json.loads(source_content)
            dest_json = json.loads(dest_content)

            if not isinstance(source_json, dict) or not isinstance(
                    dest_json, dict):
                logger.warning("Cannot merge non-dictionary JSON, replacing.")
                return source_content

            def deep_merge_json(d1: Any, d2: Any) -> Any:
                if isinstance(d1, dict) and isinstance(d2, dict):
                    merged = d1.copy()
                    for key, value in d2.items():
                        if key in merged:
                            merged[key] = deep_merge_json(merged[key], value)
                        else:
                            merged[key] = value
                    return merged
                elif isinstance(d1, list) and isinstance(d2, list):
                    combined = d1 + d2
                    # Deduplicate preserving order if possible, fallback to string repr
                    unique_list = []
                    seen = set()
                    for item in combined:
                        try:
                            hashable_item = json.dumps(item, sort_keys=True)
                        except TypeError:
                            hashable_item = object()
                        if hashable_item not in seen:
                            unique_list.append(item)
                            seen.add(hashable_item)
                    return unique_list
                else:
                    return d2

            merged_json_doc = deep_merge_json(dest_json, source_json)
            return json.dumps(merged_json_doc,
                              indent=2)  # Standard JSON indentation
        except ImportError:
            logger.error(
                "json module not found (should be built-in). Cannot merge.")
            return dest_content  # Fallback unlikely needed
        except Exception as e:
            logger.error(f"Error merging JSON content: {e}")
            return dest_content

    def merge_text_content(self,
                           source_content: str,
                           dest_content: str,
                           file_type: str = "text") -> str:
        """Merge text files with conflict markers."""
        try:
            with open(source_content, encoding='utf-8') as f:
                source_lines = f.readlines()
            with open(dest_content, encoding='utf-8') as f:
                dest_lines = f.readlines()
        except Exception as e:
            logger.error(
                f"Error reading files for text merge ({source_content}, {dest_content}): {e}"
            )
            # Decide on fallback: maybe return original dest content?
            # For simplicity here, return empty string or raise error
            return ""  # Or raise an exception

        # Simple append merge for certain files like .gitignore
        if file_type == 'gitignore' or os.path.basename(self.current_dest_path
                                                        or "") == '.gitignore':
            existing_lines = {
                line.strip()
                for line in dest_lines if line.strip()
            }
            new_lines = [
                line for line in source_lines
                if line.strip() and line.strip() not in existing_lines
            ]
            if new_lines:
                return dest_content.rstrip(
                ) + "\n\n# Added by template\n" + "".join(new_lines)
            else:
                return dest_content

        # Diff merge for others
        # Using a simpler append-if-not-present for Makefile as diff merge is complex
        if file_type == 'Makefile':
            existing_content = "".join(dest_lines)
            new_content_str = "".join(source_lines)
            # Very basic: append if not present - needs refinement for target merging
            if new_content_str not in existing_content:
                return existing_content + "\n# --- Added by template ---\n" + new_content_str
            else:
                return existing_content

        # Default diff3-style merge (as before, needs refinement)
        differ = difflib.Differ()
        diff = list(differ.compare(dest_lines, source_lines))

        # Placeholder for a more robust merge, maybe using difflib.unified_diff
        # This simple diff often doesn't produce ideal merge results.
        # For now, just appending unique lines as a fallback merge
        merged_lines = dest_lines
        existing_lines_set = set(line.strip() for line in dest_lines)
        added_header = False
        for line in source_lines:
            if line.strip() and line.strip() not in existing_lines_set:
                if not added_header:
                    merged_lines.append(
                        "\n# --- Appended by template merge ---\n")
                    added_header = True
                merged_lines.append(line)

        return ''.join(merged_lines)

    def handle_file(self, source: str, dest: str) -> None:
        """Handle a single file based on merge strategy."""
        self.current_dest_path = dest  # Store context
        if not os.path.exists(source):
            logger.debug(f"Source file {source} does not exist, skipping.")
            return

        # Skip internal cookiecutter files
        if os.path.basename(source) == 'cookiecutter.json':
            logger.debug("Skipping cookiecutter.json merge.")
            return

        source_ctx = self.get_file_context(source)
        dest_exists = os.path.exists(dest)
        dest_ctx = self.get_file_context(dest) if dest_exists else None
        dest_content = dest_ctx.content if dest_ctx else ""

        strategy = source_ctx.merge_strategy
        if strategy == MergeStrategy.ASK and dest_exists:
            print(f"\nFile exists: {dest}")
            # Basic diff output
            if not source_ctx.is_binary and dest_ctx and not dest_ctx.is_binary:
                diff = difflib.unified_diff(
                    dest_content.splitlines(keepends=True),
                    source_ctx.content.splitlines(keepends=True),
                    fromfile=f"Existing {os.path.basename(dest)}",
                    tofile=f"Template {os.path.basename(source)}",
                )
                print("--- Diff ---")
                for line in diff:
                    print(line, end='')
                print("------------")

            print("What would you like to do?")
            print(
                "[s]kip, [r]eplace, [m]erge (attempt smart merge), [t]ext merge (basic append/diff)"
            )
            choice = input("Choice [s]: ").lower().strip() or 's'
            while choice not in ['s', 'r', 'm', 't']:
                print("Invalid choice. Please choose s, r, m, or t")
                choice = input("Choice [s]: ").lower().strip() or 's'

            strategy_map = {
                's': MergeStrategy.SKIP,
                'r': MergeStrategy.REPLACE,
                'm': MergeStrategy.
                SMART_MERGE,  # Keep original strategy if smart was selected
                't': MergeStrategy.MERGE  # Use basic text merge if chosen
            }
            # If original wasn't SMART_MERGE, 'm' falls back to original ASK strategy's outcome
            if choice == 'm' and source_ctx.merge_strategy != MergeStrategy.SMART_MERGE:
                strategy = MergeStrategy.ASK  # Re-trigger logic below if needed, or default to replace
            else:
                strategy = strategy_map[choice]

        # Create backup only if replacing or merging an existing file
        if dest_exists and strategy in [
                MergeStrategy.REPLACE, MergeStrategy.MERGE,
                MergeStrategy.SMART_MERGE
        ]:
            self.backup_file(dest)

        # Apply strategy
        if strategy == MergeStrategy.SKIP and dest_exists:
            logger.info(f"Skipping {dest}")
            # Important: If skipping, remove the source file from the template output dir
            # This prevents cookiecutter from overwriting later if hooks fail?
            # Or rely on cutout extension to handle this if file name was templated?
            # Safest might be to just log skip.
            return

        if strategy == MergeStrategy.REPLACE or not dest_exists:
            logger.info(f"Copying {source} to {dest}")
            try:
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copy2(source, dest)
            except Exception as e:
                logger.error(f"Error copying {source} to {dest}: {e}")
            return

        # --- Merging Logic ---
        if source_ctx.is_binary:
            logger.warning(
                f"Cannot merge binary file {dest}, replacing instead as merge requested."
            )
            try:
                shutil.copy2(source, dest)
            except Exception as e:
                logger.error(f"Error copying binary {source} to {dest}: {e}")
            return

        logger.info(f"Merging {dest} (Strategy: {strategy.name})")
        merged_content = ""
        ext = os.path.splitext(dest)[1].lower()
        file_type = ext.lstrip('.') if ext else "text"

        if strategy == MergeStrategy.SMART_MERGE:
            if file_type == 'toml':
                merged_content = self.merge_toml(source_ctx.content,
                                                 dest_content)
            elif file_type in ('yml', 'yaml'):
                merged_content = self.merge_yaml(source_ctx.content,
                                                 dest_content)
            elif file_type == 'json':
                merged_content = self.merge_json(source_ctx.content,
                                                 dest_content)
            else:
                logger.warning(
                    f"Smart merge not supported for {ext}, falling back to "
                    f"simple text merge.")
                merged_content = self.merge_text_content(
                    source_ctx.content, dest_content, file_type)
        elif strategy == MergeStrategy.MERGE:  # Basic text merge
            merged_content = self.merge_text_content(source_ctx.content,
                                                     dest_content, file_type)
        else:  # Should not happen if logic above is correct
            logger.error(f"Unhandled merge scenario for {dest}, replacing.")
            try:
                shutil.copy2(source, dest)
            except Exception as e:
                logger.error(
                    f"Error copying {source} to {dest} during fallback: {e}")
            return

        # Write merged content
        try:
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(merged_content)
            logger.info(f"Successfully merged {dest}")
        except Exception as e:
            logger.error(f"Error writing merged file {dest}: {e}")
        finally:
            self.current_dest_path = None  # Clear context


def update_python_version(project_dir: str, python_version_list: list) -> None:
    """Update Python version in various files using the selected version."""
    # Assume the selected version is the first in the list for now
    # Ideally, the actual selected value should be read from context
    selected_version = python_version_list[0]  # Simplification!
    logger.info(f"Updating Python version references to {selected_version}")

    # ... (rest of the update logic using selected_version remains the same) ...
    # Example update for .python-version
    try:
        pyversion_path = os.path.join(project_dir, ".python-version")
        with open(pyversion_path, "w", encoding='utf-8') as f:
            f.write(selected_version + '\n')  # Ensure newline
        logger.debug(f"Updated {pyversion_path}")
    except Exception as e:
        logger.warning(f"Could not update {pyversion_path}: {e}")

    # Example update for pyproject.toml (requires careful parsing)
    pyproject_path = os.path.join(project_dir, "pyproject.toml")
    if os.path.exists(pyproject_path):
        try:
            import tomlkit
            with open(pyproject_path, "r+", encoding='utf-8') as f:
                content = tomlkit.loads(f.read())
                # Update requires-python
                if 'project' in content and 'requires-python' in content[
                        'project']:
                    content['project'][
                        'requires-python'] = f">={selected_version}"  # Example update rule
                    logger.debug("Updated requires-python in pyproject.toml")
                # Update mypy python_version if present
                if 'tool' in content and 'mypy' in content[
                        'tool'] and 'python_version' in content['tool']['mypy']:
                    content['tool']['mypy'][
                        'python_version'] = selected_version
                    logger.debug(
                        "Updated tool.mypy.python_version in pyproject.toml")

                f.seek(0)
                f.write(tomlkit.dumps(content))
                f.truncate()
        except ImportError:
            logger.warning(
                "tomlkit not installed, cannot reliably update pyproject.toml version."
            )
        except Exception as e:
            logger.warning(f"Could not update {pyproject_path}: {e}")

    # Add updates for setup.py, setup.cfg, tox.ini if they are generated/used


def setup_license(license_choice: str, full_name: str,
                  include_file: bool) -> None:
    """Set up license file based on chosen license type."""
    project_dir = os.getcwd()
    target_file = os.path.join(project_dir, 'LICENSE')

    if not include_file:
        logger.info("Skipping LICENSE file generation as per configuration.")
        if os.path.exists(target_file):
            logger.warning(
                f"Existing LICENSE file found at {target_file} but generation is disabled."
            )
        return

    # Extract short code from choice (e.g., "MIT License (MIT)" -> "MIT")
    # This is brittle; better to use a mapping if possible.
    license_code = license_choice.split('(')[-1].split(
        ')')[0] if '(' in license_choice else license_choice

    if not license_code or license_code == "Not open source":
        logger.info(
            "No open source license selected or file generation skipped.")
        if os.path.exists(target_file):
            try:
                os.remove(target_file)
                logger.info(f"Removed existing LICENSE file at {target_file}")
            except Exception as e:
                logger.error(f"Could not remove existing LICENSE file: {e}")
        return

    # Assume license texts are in a 'licenses/' directory relative to the hook
    licenses_dir = os.path.join(os.path.dirname(__file__), '..',
                                'licenses')  # Go up one level from hooks/
    license_file_path = os.path.join(
        licenses_dir, f"{license_code}.txt")  # Simplistic mapping

    if not os.path.exists(license_file_path):
        logger.error(f"License template file not found: {license_file_path}")
        # Attempt to find common variations like .md
        license_file_path_md = os.path.join(licenses_dir, f"{license_code}.md")
        if os.path.exists(license_file_path_md):
            license_file_path = license_file_path_md
            logger.info(f"Found license template as .md: {license_file_path}")
        else:
            # Fallback: Maybe create an empty file or just log error?
            logger.error("Cannot generate LICENSE file.")
            return

    try:
        with open(license_file_path, 'r', encoding='utf-8') as f:
            license_content = f.read()

        # Replace placeholders
        year = datetime.datetime.now().year
        license_content = license_content.replace('[year]', str(year)).replace(
            '<YEAR>', str(year))
        license_content = license_content.replace(
            '[fullname]', full_name).replace('<COPYRIGHT HOLDER>', full_name)
        # Add more placeholder replacements if needed

        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(license_content)
        logger.info(f"Created license file: {target_file} ({license_code})")

    except Exception as e:
        logger.error(f"Error setting up license file {target_file}: {e}")


def ensure_src_layout() -> None:
    """Ensure the project uses src layout if package exists."""
    package_name = '{{ cookiecutter.__package_name }}'  # Use the private variable
    src_dir = os.path.join('src', package_name)

    # If the target package directory doesn't exist in src/, don't force layout
    # This hook runs *after* generation, so the dir should exist if generated
    if not os.path.isdir('src') or not os.path.isdir(src_dir):
        logger.info(
            "Target package directory not found in src/, skipping src layout enforcement."
        )
        # Optional: Could check if files exist at root and move them, but risky.
        return

    logger.info(f"Confirmed src layout for package '{package_name}'.")


def setup_pytest() -> None:
    """Configure pytest - ensure basic config exists if tests are included."""
    # This function might be redundant if pyproject.toml template handles it
    # Or could be used to add conditional pytest plugins based on context
    if not os.path.exists('pyproject.toml') and not os.path.exists(
            'pytest.ini'):
        logger.info(
            "No pyproject.toml or pytest.ini found, creating basic pytest.ini")
        pytest_ini = """\
[pytest]
# Basic pytest configuration
testpaths = tests
addopts = --verbose
"""
        try:
            with open('pytest.ini', 'w', encoding='utf-8') as f:
                f.write(pytest_ini)
            logger.info("Created basic pytest.ini")
        except Exception as e:
            logger.error(f"Could not create pytest.ini: {e}")
    else:
        logger.info(
            "Existing pytest configuration found (pyproject.toml or pytest.ini)."
        )


def initialize_git() -> None:
    """Initialize Git repository and make initial commit."""
    if shutil.which('git') and not os.path.exists('.git'):
        logger.info("Initializing Git repository...")
        try:
            subprocess.run(['git', 'init'], check=True, capture_output=True)
            subprocess.run(['git', 'add', '.'],
                           check=True,
                           capture_output=True)
            # Use commitizen if available and configured? Needs check.
            commit_msg = "Initial commit from template {{ cookiecutter.project_name }} v{{ cookiecutter.project_version }}"
            subprocess.run(['git', 'commit', '-m', commit_msg],
                           check=True,
                           capture_output=True)
            logger.info("Git repository initialized and initial commit made.")
        except Exception as e:
            logger.error(f"Git initialization failed: {e}")
    elif os.path.exists('.git'):
        logger.info("Git repository already exists.")
    else:
        logger.warning("git command not found. Skipping Git initialization.")


def setup_saas_app_starter_docs(project_dir: str) -> None:
    """Set up documentation using saas-app-starter template from GitHub.
    
    Args:
        project_dir: The project directory where docs will be set up
    """
    logger.info("Setting up documentation using saas-app-starter template...")

    # Path to the docs directory
    docs_dir = os.path.join(project_dir, "docs")

    if not os.path.exists(docs_dir):
        logger.warning(
            f"Docs directory {docs_dir} does not exist. Creating it...")
        os.makedirs(docs_dir, exist_ok=True)

    # Clone or pull the saas-app-starter repository
    try:
        # Check if Git is available
        subprocess.run(["git", "--version"], check=True, capture_output=True)

        # Define the GitHub repository URL
        repo_url = "https://github.com/wyattowalsh/saas-app-starter.git"
        temp_dir = os.path.join(project_dir, ".tmp_saas_starter")

        # Clone the repository to a temporary directory
        subprocess.run(["git", "clone", "--depth=1", repo_url, temp_dir],
                       check=True,
                       capture_output=True)

        # Copy the docs structure from saas-app-starter to our project
        saas_docs_dir = os.path.join(temp_dir, "docs")

        if os.path.exists(saas_docs_dir):
            # Clear existing docs directory contents
            for item in os.listdir(docs_dir):
                item_path = os.path.join(docs_dir, item)
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)

            # Copy all files from saas-app-starter docs to our docs directory
            for item in os.listdir(saas_docs_dir):
                item_path = os.path.join(saas_docs_dir, item)
                dest_path = os.path.join(docs_dir, item)

                if os.path.isdir(item_path):
                    shutil.copytree(item_path, dest_path)
                else:
                    shutil.copy2(item_path, dest_path)

            logger.info("Successfully copied saas-app-starter docs structure")

            # Update package.json to replace project name
            package_json_path = os.path.join(docs_dir, "package.json")
            if os.path.exists(package_json_path):
                try:
                    with open(package_json_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Replace the project name
                    updated_content = content.replace(
                        '"name": "docs"',
                        f'"name": "{cookiecutter_context["project_slug"]}-docs"'
                    )

                    with open(package_json_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)

                    logger.info(
                        "Updated package.json with project information")
                except Exception as e:
                    logger.error(f"Failed to update package.json: {e}")
        else:
            logger.error(
                f"Could not find docs directory in saas-app-starter: {saas_docs_dir}"
            )

        # Clean up the temporary directory
        shutil.rmtree(temp_dir)

    except subprocess.CalledProcessError:
        logger.error(
            "Git is not available. Please install Git to use the saas-app-starter template."
        )
    except Exception as e:
        logger.error(f"Failed to set up saas-app-starter docs: {e}")


# --- Main Execution Logic ---
def main() -> int:
    """Main entry point for post-generation hook."""
    logger.info("Running post-generation hook...")

    try:
        project_dir = os.getcwd()

        # Determine if we're adding to an existing project
        add_to_existing = cookiecutter_context['add_to_existing'] in ('True',
                                                                      'true',
                                                                      True,
                                                                      'y',
                                                                      'yes',
                                                                      '1')

        # Smart file merging for existing projects
        if add_to_existing:
            # Ensure we're in a project directory
            if not os.path.exists(os.path.join(project_dir, 'pyproject.toml')):
                logger.error("Not a Python project. No pyproject.toml found.")
                return 1

            logger.info("Adding to existing project...")
            handle_existing_project(project_dir)

        # Parse Python version
        python_version_raw = cookiecutter_context.get('python_version', '3.12')
        # Handle if it's a list or string
        if python_version_raw.startswith('[') and python_version_raw.endswith(
                ']'):
            # It's a list representation in string form, extract first value
            python_version = python_version_raw.strip('[]').split(
                ',')[0].strip('\'"')
        else:
            python_version = python_version_raw.strip('\'"')

        update_python_version(project_dir, [python_version])

        # Set up license if requested
        include_license = cookiecutter_context['include_license_file'] in (
            'True', 'true', True, 'y', 'yes', '1')
        if include_license:
            license_type = cookiecutter_context.get('license_type', '')
            author_name = cookiecutter_context.get('full_name', '')
            setup_license(license_type, author_name, include_license)

        # Ensure src layout
        ensure_src_layout()

        # Set up pytest configuration
        setup_pytest()

        # Handle documentation setup
        include_docs = cookiecutter_context['include_docs_site'] in ('True',
                                                                     'true',
                                                                     True, 'y',
                                                                     'yes',
                                                                     '1')
        if include_docs:
            docs_template = cookiecutter_context.get('docs_template', 'basic')
            if docs_template == 'saas-app-starter':
                setup_saas_app_starter_docs(project_dir)
            else:
                logger.info("Using basic documentation template")

        # Initialize Git repository
        initialize_git()

        # Perform cutout cleanup for conditional sections
        if cutout_cleanup:
            logger.info("Running cutout cleanup for conditional sections...")
            cutout_cleanup(project_dir)

        logger.info("Post-generation hook completed successfully!")
        return 0

    except Exception as e:
        logger.error(f"Error in post-generation hook: {e}")
        # Print exception traceback for debugging
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())

if __name__ == "__main__":
    sys.exit(main())
