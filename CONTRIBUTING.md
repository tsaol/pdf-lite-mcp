# Contributing to pdf-reader-mcp

We love your input! We want to make contributing to pdf-reader-mcp as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

## Pull Requests

Pull requests are the best way to propose changes to the codebase. We actively welcome your pull requests:

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Development Setup

### Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/) for dependency management

### Installation

1. Clone the repository:
```bash
git clone https://github.com/tsaol/pdf-reader-mcp.git
cd pdf-reader-mcp
```

2. Install dependencies:
```bash
uv sync
```

3. Run tests:
```bash
uv run python tests/simple_test.py
uv run python tests/test_server.py
```

### Running the Server

```bash
uv run python src/main.py
```

## Code Style

We use Python's standard style guidelines:

- Follow PEP 8
- Use type hints where possible
- Write descriptive docstrings
- Keep functions focused and small
- Use meaningful variable names

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Test with different PDF files and edge cases
- Include both unit tests and integration tests

## Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for formatting changes
- `refactor:` for code refactoring
- `test:` for adding tests
- `chore:` for maintenance tasks

Examples:
```
feat: add support for password-protected PDFs
fix: handle corrupted PDF files gracefully
docs: update installation instructions
```

## Issues

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/tsaol/pdf-reader-mcp/issues).

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## Feature Requests

We welcome feature requests! Please provide:

- **Use case**: Why would this feature be useful?
- **Description**: What should the feature do?
- **Alternative solutions**: Have you considered any alternatives?

## Security

If you discover a security vulnerability, please send an email to tsaol@outlook.com instead of using the issue tracker.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## Questions?

Feel free to contact the maintainers if you have any questions:

- Email: tsaol@outlook.com
- GitHub: [@tsaol](https://github.com/tsaol)

Thank you for contributing! 🎉