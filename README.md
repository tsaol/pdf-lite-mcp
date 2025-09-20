# tsaol-pdf-reader-mcp

A **simplified Python MCP server** for reading PDF files, specifically optimized for **Amazon Q CLI** usage. Built as a streamlined alternative to complex PDF processing tools, focusing on clean output and reliable performance.

## ✨ Key Features

- 📄 **Multi-source PDF reading** - Local files and URLs
- 🎯 **Page-specific extraction** - Get exactly what you need
- 📊 **Rich metadata support** - Title, author, page count, and more
- 🛡️ **Security-first design** - Path traversal protection and input validation
- ⚡ **Amazon Q CLI optimized** - Clean, structured output with emojis
- 🐍 **Pure Python** - Minimal dependencies, easy deployment
- 🔄 **Batch processing** - Handle multiple PDFs in one request
- 🚨 **Robust error handling** - Graceful failure recovery

## 🚀 Why Choose tsaol-pdf-reader-mcp?

Unlike heavy-weight PDF processors, this server is designed specifically for AI assistants like Amazon Q CLI:

- **Clean Output**: Structured, emoji-enhanced responses perfect for CLI display
- **Smart Truncation**: Automatic text limiting prevents overwhelming output
- **Batch-friendly**: Process multiple PDFs without complex scripting
- **Error Resilient**: One bad PDF won't stop your entire workflow
- **Security Focused**: Safe file access with comprehensive validation

## Quick Start

### Installation

This project uses `uv` for Python environment and dependency management.

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies and create virtual environment
uv sync

# Or install as a package (if needed)
uv pip install -e .
```

## Amazon Q CLI Integration

### Configuration

Create your MCP configuration file with the following settings:

```json
{
  "mcpServers": {
    "tsaol-pdf-reader": {
      "command": "uv",
      "args": ["run", "python", "src/main.py"],
      "name": "PDF Reader (tsaol)",
      "description": "Simplified Python PDF reader optimized for Amazon Q CLI",
      "cwd": "/path/to/tsaol-pdf-reader-mcp",
      "env": {
        "PYTHONPATH": ".",
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}
```

**Alternative configuration** (if uv is not available in the MCP client environment):
```json
{
  "mcpServers": {
    "tsaol-pdf-reader": {
      "command": "python",
      "args": ["-m", "src.main"],
      "name": "PDF Reader (tsaol)",
      "description": "Simplified Python PDF reader optimized for Amazon Q CLI",
      "cwd": "/path/to/tsaol-pdf-reader-mcp",
      "env": {
        "PYTHONPATH": ".",
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}
```

### Usage Examples

#### Basic PDF Reading
```json
{
  "tool_name": "read_pdf",
  "arguments": {
    "sources": [{"path": "./document.pdf"}],
    "include_full_text": true
  }
}
```

**Amazon Q CLI Output:**
```
📄 ./document.pdf
📊 Pages: 5
📝 Title: Sample Document | Author: John Doe
📖 Full Text:
This is the content of the PDF document...
```

#### Specific Pages
```json
{
  "tool_name": "read_pdf",
  "arguments": {
    "sources": [
      {
        "path": "./report.pdf",
        "pages": [1, 3, 5]
      }
    ]
  }
}
```

**Amazon Q CLI Output:**
```
📄 ./report.pdf
📊 Pages: 10
📄 Page 1:
Executive Summary content...

📄 Page 3:
Analysis section content...

📄 Page 5:
Conclusion content...
```

#### Multiple PDFs
```json
{
  "tool_name": "read_pdf",
  "arguments": {
    "sources": [
      {"path": "./doc1.pdf"},
      {"url": "https://example.com/doc2.pdf"}
    ],
    "include_page_count": true
  }
}
```

**Amazon Q CLI Output:**
```
📄 Processed 2 PDF sources:

--- Source 1: ./doc1.pdf ---
✅ Success
📊 Pages: 3

--- Source 2: https://example.com/doc2.pdf ---
✅ Success
📊 Pages: 8
```

### Best Practices

1. **Batch Processing**: Process multiple related PDFs in a single request
2. **Selective Content**: Only request what you need - use `include_full_text: false` if you only need metadata
3. **Page Selection**: Specify `pages` for large documents to avoid overwhelming output
4. **Error Recovery**: The server continues processing even if individual PDFs fail

## API Reference

### read_pdf Tool

**Parameters:**
- `sources`: Array of PDF sources with optional page specifications
- `include_metadata`: Include PDF metadata (default: true)
- `include_page_count`: Include total page count (default: true)
- `include_full_text`: Include full text if no specific pages requested (default: false)

**Response:**
```json
{
  "results": [
    {
      "source": "./document.pdf",
      "success": true,
      "data": {
        "page_texts": [
          {"page": 1, "text": "Page 1 content..."}
        ],
        "metadata": {...},
        "num_pages": 10
      }
    }
  ]
}
```

## Testing Guide

### Test Levels

#### 1. Basic Functionality Tests (Recommended First)

```bash
uv run python tests/simple_test.py
```

**Tests:**
- ✅ Module imports
- ✅ Path security checks
- ✅ Data model validation
- ✅ Utility functions

**Expected Output:**
```
🧪 Running simple tests for tsaol-pdf-reader-mcp
✅ Models imported successfully
✅ Utils imported successfully
✅ Safe path resolved
✅ Path traversal prevented
✅ Valid request created
✅ Invalid request caught
✅ Error formatting
✅ Text cleaning
✅ Text truncation
✨ Simple tests completed!
```

#### 2. MCP Server Tests

```bash
uv run python tests/test_server.py
```

**Tests:**
- ✅ MCP server component imports
- ✅ Tool listing functionality
- ✅ Tool calling functionality
- ✅ Parameter validation
- 🔒 Security path checks

#### 3. PDF Processing Tests (Requires Network)

```bash
uv run python tests/test_with_pdf.py
```

**Tests:**
- 📡 URL PDF download and processing
- 📄 Multi-source PDF processing
- 🎯 Page selection functionality

#### 4. Interactive Testing

```bash
uv run python tests/manual_test.py
```

**Menu Options:**
1. Test invalid parameters
2. Test file not found
3. Test URL PDF
4. Test custom PDF file
5. Exit

#### 5. MCP Protocol Testing

```bash
# Start MCP server
uv run python src/main.py
```

The server will wait for MCP client connections.

### Troubleshooting

#### Common Issues

**1. Import Errors**
```bash
# Ensure dependencies are installed
uv sync

# Check Python version
uv run python --version  # Requires >=3.10
```

**2. Path Errors**
- All file paths must be relative to project root
- Absolute paths or path traversal (`../`) are not allowed

**3. PDF Processing Errors**
- Check if PDF file is corrupted
- Verify file permissions
- For URLs, check network connectivity

**4. MCP Connection Issues**
- Ensure MCP package is correctly installed
- Check stdio input/output

### Acceptance Criteria

Project passes tests when:

1. **Basic functionality tests** - All pass
2. **MCP server tests** - At least 3/4 pass
3. **Parameter validation** - Correctly catches and handles invalid input
4. **Error handling** - Friendly error messages
5. **Security checks** - Path traversal protection works

## Security

- All file access is restricted to the project root directory
- Path traversal protection prevents access to sensitive files
- Input validation with Pydantic models
- Error isolation - single PDF failures don't affect batch processing

## Performance

### Expected Performance (Reference Values)
- **Small PDF (<1MB)**: <2 seconds processing
- **Medium PDF (1-10MB)**: <5 seconds processing
- **Large PDF (>10MB)**: <10 seconds processing
- **URL downloads**: Depends on network speed
- **Memory usage**: <100MB for typical PDFs

## License

MIT