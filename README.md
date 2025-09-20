# pdf-reader-mcp

A Python MCP server for reading PDF files, optimized for Amazon Q CLI usage.

## Features

- Read PDFs from local files or URLs
- Extract specific pages or full content
- Metadata extraction (title, author, page count)
- Batch processing support
- Security-focused with path validation

## Installation

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

## Amazon Q CLI Configuration

```json
{
  "mcpServers": {
    "pdf-reader": {
      "command": "uv",
      "args": ["run", "python", "src/main.py"],
      "cwd": "/path/to/pdf-reader-mcp",
      "env": {
        "PYTHONPATH": "."
      }
    }
  }
}
```

## Usage

### Basic PDF Reading
```json
{
  "tool_name": "read_pdf",
  "arguments": {
    "sources": [{"path": "./document.pdf"}],
    "include_full_text": true
  }
}
```

### Specific Pages
```json
{
  "tool_name": "read_pdf",
  "arguments": {
    "sources": [{"path": "./report.pdf", "pages": [1, 3, 5]}]
  }
}
```

### Multiple PDFs
```json
{
  "tool_name": "read_pdf",
  "arguments": {
    "sources": [
      {"path": "./doc1.pdf"},
      {"url": "https://example.com/doc2.pdf"}
    ]
  }
}
```

## Testing

```bash
# Basic tests
uv run python tests/simple_test.py

# Server tests
uv run python tests/test_server.py

# PDF processing tests (requires network)
uv run python tests/test_with_pdf.py
```

## License

MIT License - see [LICENSE](LICENSE) file for details.