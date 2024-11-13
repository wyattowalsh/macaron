"""macaron/hooks/pre_prompt.py

Ensures proper libraries are installed if possible:
- pyenv
- poetry
- make
"""

import sys
import subprocess
from enum import Enum
from loguru import logger
from rich.console import Console
import threading
from typing import Tuple

console = Console()


class Prerequisite(Enum):
    PYENV = ('pyenv', '1.2.0')
    POETRY = ('poetry', '1.1.0')
    MAKE = ('make', '4.0')


def parse_version(version_str: str) -> str:
    # Implement logic to parse version from version_str
    # Example placeholder implementation
    return version_str.strip().split()[-1]


def check_prereq(prereq: Prerequisite) -> bool:
    name, min_version = prereq.value
    try:
        result = subprocess.run([name, '--version'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True,
                                check=True)
        version_info = result.stdout.strip()
        version = parse_version(version_info)
        if version < min_version:
            logger.error(
                f"{name} version {version} is less than required {min_version}."
            )
            return False
        logger.info(f"{name} is installed: {version_info}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Error checking {name}: {e.stderr.strip()}")
        return False
    except FileNotFoundError:
        logger.error(f"{name} is not installed.")
        return False


def check_pyenv():
    return check_prereq(Prerequisite.PYENV)


def check_poetry():
    return check_prereq(Prerequisite.POETRY)


def check_make():
    return check_prereq(Prerequisite.MAKE)


def check_prereqs():
    threads = []
    results = {}

    def run_check(prereq):
        results[prereq] = check_prereq(prereq)

    for prereq in Prerequisite:
        thread = threading.Thread(target=run_check, args=(prereq, ))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    all_installed = all(results.values())
    if not all_installed:
        for prereq, installed in results.items():
            if not installed:
                console.print(
                    f"[bold red]{prereq.value[0]} is not installed or does not meet the required version.[/bold red]"
                )
        console.print(
            "[bold yellow]Please install the missing prerequisites and try again.[/bold yellow]"
        )
        sys.exit(1)
    else:
        console.print(
            "[bold green]All prerequisites are installed.[/bold green]")


if __name__ == "__main__":
    check_prereqs()
