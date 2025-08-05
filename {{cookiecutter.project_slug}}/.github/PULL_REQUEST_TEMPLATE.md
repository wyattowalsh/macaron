# Pull Request Template for {{ cookiecutter.project_name }}

## 📋 Description

Brief description of the changes in this PR.

## 🔗 Related Issues

Fixes #(issue_number)
Closes #(issue_number)
Related to #(issue_number)

## 🚀 Type of Change

Please check the relevant option:

- [ ] 🐛 Bug fix (non-breaking change which fixes an issue)
- [ ] ✨ New feature (non-breaking change which adds functionality)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📝 Documentation update
- [ ] 🔧 Configuration change
- [ ] 🎨 Code style/formatting change
- [ ] ♻️ Refactoring (no functional changes)
- [ ] ⚡ Performance improvement
- [ ] 🧪 Test additions or modifications
- [ ] 🔒 Security improvement
- [ ] 📦 Dependency update
- [ ] 🚀 Release preparation

## 🧪 Testing

Describe the tests that you ran to verify your changes:

- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed
- [ ] Added new tests for the changes
- [ ] All existing tests still pass

### Test Configuration
- Python version: [e.g. {{ cookiecutter.python_version }}]
- OS: [e.g. Ubuntu 20.04]
- Package manager: [e.g. {{ cookiecutter.package_manager }}]

### Test Evidence
```bash
# Paste test results here
```

## 📝 Checklist

Please ensure your PR meets the following requirements:

### Code Quality
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes

### Security & Performance
- [ ] I have checked for security vulnerabilities
- [ ] I have considered the performance impact of my changes
- [ ] I have not introduced any secrets or sensitive data

### Documentation
- [ ] I have updated the README.md if needed
- [ ] I have updated the CHANGELOG.md
- [ ] I have updated docstrings/comments where applicable
- [ ] {% if cookiecutter.include_api %}I have updated API documentation if needed{% endif %}
- [ ] {% if cookiecutter.include_cli_example %}I have updated CLI help text if needed{% endif %}

### Dependencies
- [ ] I have not added unnecessary dependencies
- [ ] New dependencies are properly documented
- [ ] All dependencies are compatible with project requirements

## 📸 Screenshots (if applicable)

If your changes include UI modifications, please include before/after screenshots.

## 🔄 Migration Guide (for breaking changes)

If this is a breaking change, please describe:

1. What breaks
2. How users should migrate their code
3. Any automation or scripts that can help with migration

## 🎯 Performance Impact

Describe any performance implications:

- [ ] No performance impact
- [ ] Improves performance
- [ ] May impact performance (explain below)

**Performance details:**
[Describe any performance testing done, benchmarks, or considerations]

## 🔒 Security Considerations

- [ ] No security implications
- [ ] Improves security
- [ ] May have security implications (explain below)

**Security details:**
[Describe any security considerations, threat model changes, etc.]

## 📋 Deployment Notes

Any special deployment considerations:

- [ ] No special deployment needed
- [ ] Database migrations required
- [ ] Configuration changes required
- [ ] Environment variables need updating
- [ ] Other: [Specify]

## 🤝 Reviewer Guidelines

For reviewers, please check:

- [ ] Code style and conventions
- [ ] Test coverage and quality
- [ ] Documentation completeness
- [ ] Security considerations
- [ ] Performance implications
- [ ] Backward compatibility
- [ ] Error handling

## 📚 Additional Notes

Any additional information that reviewers should know:

[Add any additional context, design decisions, trade-offs, or other information that would be helpful for reviewers]