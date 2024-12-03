import sys
import subprocess
import platform
from pathlib import Path


def init_git() -> None:
    """Initializes a git repository and makes the initial commit."""
    try:
        subprocess.check_call(["git", "init"])
        subprocess.check_call(["git", "add", "."])
        subprocess.check_call(["git", "commit", "-m", "Initial commit"])
    except subprocess.CalledProcessError:
        print(
            "ERROR: Git command failed. Ensure Git is installed and configured correctly."
        )
        sys.exit(1)


def create_venv() -> None:
    """Creates a virtual environment and installs dependencies."""
    venv_dir = Path("venv")
    try:
        subprocess.check_call([sys.executable, "-m", "venv", str(venv_dir)])
    except subprocess.CalledProcessError:
        print("ERROR: Failed to create virtual environment.")
        sys.exit(1)

    # Install dependencies
    pip_executable = venv_dir / ("Scripts" if platform.system() == "Windows"
                                 else "bin") / "pip"
    requirements_file = Path("requirements.txt")

    if requirements_file.exists():
        try:
            subprocess.check_call(
                [str(pip_executable), "install", "-r",
                 str(requirements_file)])
        except subprocess.CalledProcessError:
            print("ERROR: Failed to install dependencies.")
            sys.exit(1)


def adjust_line_endings() -> None:
    """Adjusts line endings based on user's settings."""
    new_lines = "{{ cookiecutter._new_lines }}"
    if new_lines:
        line_ending = "\r\n" if new_lines == "\\r\\n" else "\n"
        for file_path in Path(".").rglob("*"):
            if file_path.is_file() and file_path.suffix in (".py", ".txt",
                                                            ".md"):
                with file_path.open("rb") as f:
                    content = f.read()
                content = content.replace(b"\r\n", b"\n").replace(
                    b"\n", line_ending.encode())
                with file_path.open("wb") as f:
                    f.write(content)


def main():
    project_slug = "{{ cookiecutter.project_slug }}"
    use_git = "{{ cookiecutter.use_git }}".lower() in ["y", "yes", "true", "1"]
    use_venv = "{{ cookiecutter.use_venv }}".lower() in [
        "y", "yes", "true", "1"
    ]

    try:
        Path(project_slug).resolve(strict=True)
    except FileNotFoundError:
        print(f"ERROR: Cannot find the project directory '{project_slug}'.")
        sys.exit(1)

    # Change to the project directory
    os.chdir(project_slug)

    if use_git:
        init_git()
    if use_venv:
        create_venv()
    adjust_line_endings()


if __name__ == "__main__":
    main()
