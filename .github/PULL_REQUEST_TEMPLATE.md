# Pull Request

## Description
Provide a clear and concise description of what this PR does.

## Type of Change
- [ ] 🐛 Bug fix (non-breaking change which fixes an issue)
- [ ] ✨ New feature (non-breaking change which adds functionality)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📚 Documentation update
- [ ] 🔧 Maintenance (refactoring, code cleanup, dependency updates)
- [ ] 🧪 Test improvements
- [ ] 🚀 Performance improvement

## Related Issues
Fixes #(issue_number)
Closes #(issue_number)
Related to #(issue_number)

## Changes Made
- List the specific changes made in this PR
- Be as detailed as necessary
- Include any new dependencies or configuration changes

## Testing
Describe the tests you ran to verify your changes:

### Test Environment
- **OS**: [e.g. Ubuntu 22.04]
- **Python version**: [e.g. 3.10.12]
- **Testing method**: [e.g. local testing, CI/CD]

### Test Cases
- [ ] All existing tests pass
- [ ] New tests added for new functionality
- [ ] Manual testing completed
- [ ] Edge cases considered and tested

### Test Commands
```bash
# Commands used to test the changes
uv run python tests/simple_test.py
uv run python tests/test_server.py
# Add any specific test commands used
```

## Screenshots/Output
If applicable, add screenshots or command output to help explain your changes.

```
Paste any relevant command output here
```

## Breaking Changes
If this PR introduces breaking changes, describe:
- What breaks
- How to migrate from the old behavior
- Why the breaking change is necessary

## Documentation
- [ ] Code is self-documenting with clear variable names and comments
- [ ] Docstrings updated for new/modified functions
- [ ] README.md updated (if applicable)
- [ ] CHANGELOG.md updated
- [ ] Type hints added/updated

## Performance Impact
- [ ] No performance impact
- [ ] Performance improved
- [ ] Performance may be affected (explain below)

If performance is affected, describe:
- What might be slower/faster
- Benchmarks or measurements (if available)
- Mitigation strategies

## Security Considerations
- [ ] No security impact
- [ ] Security improved
- [ ] Potential security implications (explain below)

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published

## Additional Notes
Add any additional notes for reviewers here.

---

**For Reviewers:**
- [ ] Code quality and style
- [ ] Test coverage
- [ ] Documentation completeness
- [ ] Security implications
- [ ] Performance impact
- [ ] Breaking changes properly documented