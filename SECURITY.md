# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible for receiving such patches depends on the CVSS v3.0 Rating:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

The pdf-reader-mcp team and community take security bugs seriously. We appreciate your efforts to responsibly disclose your findings, and will make every effort to acknowledge your contributions.

### How to Report a Security Vulnerability?

If you believe you have found a security vulnerability in pdf-reader-mcp, please report it to us through coordinated disclosure.

**Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**

Instead, please send an email to tsaol@outlook.com with the following information:

- **Type of issue** (e.g. buffer overflow, SQL injection, cross-site scripting, etc.)
- **Full paths of source file(s) related to the manifestation of the issue**
- **The location of the affected source code** (tag/branch/commit or direct URL)
- **Any special configuration required to reproduce the issue**
- **Step-by-step instructions to reproduce the issue**
- **Proof-of-concept or exploit code** (if possible)
- **Impact of the issue**, including how an attacker might exploit the issue

This information will help us triage your report more quickly.

### What to expect

- We will acknowledge receipt of your vulnerability report within 48 hours.
- We will provide an estimated timeline for addressing the vulnerability within 7 days.
- We will notify you when the vulnerability has been fixed.
- We will publicly disclose the vulnerability in a responsible manner after a fix is available.

## Security Features

pdf-reader-mcp includes several security features designed to protect against common attack vectors:

### Path Traversal Protection
- All file access is restricted to the project root directory
- Path traversal attempts (e.g., `../../../etc/passwd`) are blocked
- Only relative paths within the project boundaries are allowed

### Input Validation
- All input is validated using Pydantic models
- PDF sources are limited to prevent resource exhaustion
- Page numbers are validated to be positive integers
- URLs are validated to use HTTP/HTTPS protocols only

### Resource Limits
- Maximum 10 PDF sources per request
- Maximum 100 pages per PDF source
- 30-second timeout for URL downloads
- Automatic cleanup of temporary files

### Error Handling
- Error messages are sanitized to prevent information disclosure
- Stack traces are not exposed to end users
- Failed PDF processing doesn't affect other PDFs in batch operations

## Security Best Practices

When using pdf-reader-mcp:

1. **File System Security**
   - Run the service with minimal required permissions
   - Use a dedicated user account for the service
   - Ensure the project root directory has appropriate permissions

2. **Network Security**
   - Be cautious when processing PDFs from untrusted URLs
   - Consider implementing URL allowlists in production
   - Monitor network traffic for suspicious patterns

3. **PDF Processing**
   - Be aware that malicious PDFs could potentially exploit PDF processing libraries
   - Consider sandboxing the service in production environments
   - Monitor resource usage to detect potential DoS attacks

4. **Logging and Monitoring**
   - Enable logging to detect suspicious activities
   - Monitor for excessive resource usage
   - Set up alerts for security-related events

## Vulnerability Disclosure Policy

When we receive a security bug report, we will:

1. Confirm the problem and determine the affected versions
2. Audit code to find any potential similar problems
3. Prepare fixes for all releases still under support
4. Release new versions as quickly as possible
5. Prominently feature the problem in the release notes

## Security Updates

Security updates will be released as patch versions and announced through:

- GitHub Security Advisories
- Release notes on GitHub
- Email notifications to maintainers

## Attribution

We will acknowledge security researchers who responsibly disclose vulnerabilities to us. If you would like to be credited, please let us know in your initial report.

## Comments on this Policy

If you have suggestions on how this process could be improved, please submit a pull request or open an issue to discuss.