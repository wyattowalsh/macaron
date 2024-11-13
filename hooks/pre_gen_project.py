from pydantic import (BaseModel, EmailStr, HttpUrl, ValidationError, StrictStr,
                      StrictBool, constr)
from enum import Enum
import sys


class OpenSourceLicense(str, Enum):
    AGPL_3_0 = "GNU Affero General Public License v3.0 (AGPL-3.0)"
    GPL_3_0 = "GNU General Public License v3.0 (GPL-3.0)"
    LGPL_3_0 = "GNU Lesser General Public License v3.0 (LGPL-3.0)"
    MPL_2_0 = "Mozilla Public License 2.0 (MPL-2.0)"
    APACHE_2_0 = "Apache License 2.0 (Apache-2.0)"
    MIT = "MIT License (MIT)"
    BSL_1_0 = "Boost Software License 1.0 (BSL-1.0)"
    UNLICENSE = "The Unlicense"
    NOT_OPEN_SOURCE = "Not open source"


YES_NO_VALUES = {'yes': True, 'no': False}


class CookiecutterConfig(BaseModel):
    full_name: StrictStr
    email: EmailStr
    github_username: StrictStr
    project_name: StrictStr
    project_slug: constr(regex=r'^[_a-zA-Z][_a-zA-Z0-9]+$',
                         strip_whitespace=True)
    project_description: StrictStr
    project_version: constr(regex=r'^\d+\.\d+\.\d+$', strip_whitespace=True)
    python_version: constr(regex=r'^\d+\.\d+(\.\d+)?$', strip_whitespace=True)
    github_url: HttpUrl
    project_url: HttpUrl
    pypi_username: StrictStr
    open_source_license: OpenSourceLicense
    pytest: StrictBool
    documentation: StrictBool

    @validator('pytest', 'documentation', pre=True)
    def validate_yes_no(cls, v):
        if isinstance(v, str):
            v_lower = v.strip().lower()
            if v_lower in YES_NO_VALUES:
                return YES_NO_VALUES[v_lower]
        raise ValueError('Value must be "yes" or "no".')


try:
    config = CookiecutterConfig(**cookiecutter)
except ValidationError as e:
    print('ERROR: Invalid configuration:')
    for error in e.errors():
        loc = ".".join(str(loc) for loc in error['loc'])
        print(f" - {loc}: {error['msg']}")
    sys.exit(1)
