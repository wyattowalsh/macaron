# Changelog

All notable changes to {{ cookiecutter.project_name }} will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup
- Core functionality implementation
{% if cookiecutter.include_cli_example %}- Command-line interface with Typer{% endif %}
{% if cookiecutter.include_api %}- REST API with FastAPI{% endif %}
{% if cookiecutter.include_async %}- Async/await support{% endif %}
{% if cookiecutter.include_database %}- {{ cookiecutter.database_type.title() }} database integration{% endif %}
- Comprehensive test suite with pytest
- Code quality tools ({{ cookiecutter.linter }}, {{ cookiecutter.code_style }}, {{ cookiecutter.type_checker }})
{% if cookiecutter.include_pre_commit %}- Pre-commit hooks for automated quality checks{% endif %}
{% if cookiecutter.include_docker %}- Docker support with multi-stage builds{% endif %}
{% if cookiecutter.include_docs_site %}- Documentation site with modern tooling{% endif %}
{% if cookiecutter.include_ci_workflow %}- CI/CD pipeline with GitHub Actions{% endif %}
{% if cookiecutter.include_monitoring %}- Monitoring with Prometheus and Grafana{% endif %}
{% if cookiecutter.include_security %}- Security scanning with Bandit and Safety{% endif %}

### Changed
- Updated dependencies to latest versions
- Improved error handling and logging
- Enhanced configuration management

### Deprecated
- Nothing deprecated in initial release

### Removed
- Nothing removed in initial release

### Fixed
- Initial setup and configuration issues

### Security
{% if cookiecutter.include_security %}- Implemented security scanning in CI/CD
- Added dependency vulnerability checking{% else %}- No security updates in initial release{% endif %}

## [{{ cookiecutter.project_version }}] - {{ "now" | strftime("%Y-%m-%d") }}

### Added
- Initial release of {{ cookiecutter.project_name }}
- Core functionality and APIs
- Comprehensive documentation
- Testing infrastructure
- Development tooling and automation

---

## Contributing to the Changelog

When contributing to this project, please update this changelog according to the following guidelines:

### Types of Changes

- **Added** for new features
- **Changed** for changes in existing functionality
- **Deprecated** for soon-to-be removed features
- **Removed** for now removed features
- **Fixed** for any bug fixes
- **Security** for vulnerability fixes

### Format Guidelines

- Keep entries in reverse chronological order (newest first)
- Use present tense ("Add feature" not "Added feature")
- Be specific about what changed
- Include issue/PR references when applicable
- Group related changes together

### Example Entry

```markdown
## [1.2.0] - 2024-01-15

### Added
- New authentication system (#123)
- Support for configuration files (#124)
- Batch processing functionality (#125)

### Changed
- Improved error messages for validation failures (#126)
- Updated CLI help text for better clarity (#127)

### Fixed
- Fixed memory leak in data processing (#128)
- Resolved race condition in async operations (#129)

### Security
- Updated dependencies to fix security vulnerabilities (#130)
```

### Automatic Updates

{% if cookiecutter.include_commitizen %}
This changelog is automatically updated using [Commitizen](https://commitizen-tools.github.io/commitizen/) when versions are bumped:

```bash
cz bump
```

The changelog generation follows conventional commit standards and will automatically categorize changes based on commit message prefixes.
{% else %}
This changelog should be manually updated with each release. Consider using conventional commits and automation tools like Commitizen for automatic changelog generation.
{% endif %}

---

For the full diff of any release, see the [releases page]({{ cookiecutter.project_repository }}/releases).