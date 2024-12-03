import sys
from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError, constr, validator
from enum import Enum


class OpenSourceLicense(str, Enum):
    MIT = "MIT"
    BSD_3 = "BSD-3"
    GPL_3_0 = "GNU GPL v3.0"
    APACHE_2_0 = "Apache Software License 2.0"


class CookiecutterConfig(BaseModel):
    project_name: constr(strip_whitespace=True,
                         min_length=1,
                         regex=r"^[A-Za-z ]+$")
    project_slug: constr(strip_whitespace=True,
                         regex=r"^[_a-zA-Z][_a-zA-Z0-9\-]+$")
    use_docker: bool
    license: OpenSourceLicense

    @validator("use_docker", pre=True)
    def validate_use_docker(cls, v):
        truthy = {"y", "yes", "true", "1"}
        falsy = {"n", "no", "false", "0"}
        v_lower = v.strip().lower()
        if v_lower in truthy:
            return True
        elif v_lower in falsy:
            return False
        else:
            raise ValueError("Please enter 'yes' or 'no' for use_docker.")


def validate_config():
    try:
        config_data = {
            "project_name": "{{ cookiecutter.project_name }}",
            "project_slug": "{{ cookiecutter.project_slug }}",
            "use_docker": "{{ cookiecutter.use_docker }}",
            "license": "{{ cookiecutter.license }}",
        }
        config = CookiecutterConfig(**config_data)
    except ValidationError as e:
        print("ERROR: Invalid configuration:")
        for error in e.errors():
            loc = ".".join(str(loc) for loc in error["loc"])
            print(f" - {loc}: {error['msg']}")
        sys.exit(1)

    # Check if the project directory already exists
    import os
    if os.path.exists(config.project_slug):
        print(
            f"ERROR: The directory '{config.project_slug}' already exists. Please choose a different project slug."
        )
        sys.exit(1)


if __name__ == "__main__":
    validate_config()
