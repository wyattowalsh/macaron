# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Installation

<!-- Instructions for installation -->

## Usage

<!-- Instructions for usage -->

## Supported File Types

{% for extension, details in cookiecutter.file_types|dictsort %}
### {{ details.name }} ({{ extension }})

- Library: {{ details.library }}
- Applications: 
  {% for app in details.apps %}
  - {{ app }}
  {% endfor %}
{% endfor %}

## Docker Support

{% if cookiecutter.run_as_docker %}
This project supports running as a Docker container.
{% else %}
This project does not support running as a Docker container.
{% endif %}

## Contributing

<!-- Guidelines for contributing -->

## License

This project is licensed under the {{ cookiecutter.license }} license.

## Author

{{ cookiecutter.author_name }} (<{{ cookiecutter.author_email }}>)
