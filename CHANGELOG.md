# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Open source project structure and governance files
- MIT License
- Contributing guidelines
- Code of conduct
- Security policy

## [0.1.0] - 2024-09-20

### Added
- Initial release of pdf-reader-mcp
- Single `read_pdf` tool for PDF processing
- Support for local files and URLs
- Page-specific extraction with array format
- Rich metadata extraction (title, author, page count)
- Amazon Q CLI optimized output with emojis
- Security-first design with path traversal protection
- Modern Python packaging with uv support
- Comprehensive test suite with multiple test levels
- Performance monitoring with request timing
- Configurable logging system
- Input validation with limits (max 10 sources, 100 pages)
- URL download timeout protection (30 seconds)
- Batch processing support for multiple PDFs
- Error isolation - single PDF failures don't affect batch processing

### Technical Details
- **Language**: Python 3.10+
- **Dependencies**: mcp>=1.1.0, pydantic>=2.0.0, pypdf>=4.0.0, requests>=2.31.0
- **Package Management**: uv for fast, reliable dependency management
- **Architecture**: Async MCP server with modular design
- **Security**: Path traversal protection, input validation, sandboxed file access
- **Testing**: 4-level test suite (simple, server, PDF processing, interactive)
- **Documentation**: Comprehensive README with usage examples and troubleshooting

### Performance
- **Small PDFs (<1MB)**: <2 seconds processing
- **Medium PDFs (1-10MB)**: <5 seconds processing
- **Large PDFs (>10MB)**: <10 seconds processing
- **Memory usage**: <100MB for typical PDFs
- **URL downloads**: Configurable timeout with cleanup

### Security Features
- All file access restricted to project root directory
- Path traversal attack prevention
- Input validation using Pydantic models
- URL validation for remote PDF sources
- Automatic temporary file cleanup
- Error message sanitization

[Unreleased]: https://github.com/tsaol/pdf-reader-mcp/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/tsaol/pdf-reader-mcp/releases/tag/v0.1.0