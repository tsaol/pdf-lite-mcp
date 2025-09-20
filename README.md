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

```bash
# Install dependencies
pip install -r requirements.txt

# Or install as a package
pip install -e .
```

### Usage with MCP Client

The server provides a single `read_pdf` tool:

```json
{
  "tool_name": "read_pdf",
  "arguments": {
    "sources": [
      {
        "path": "./document.pdf",
        "pages": [1, 2, 3]
      }
    ],
    "include_metadata": true,
    "include_page_count": true
  }
}
```

### Amazon Q CLI Configuration

Add to your MCP configuration:

```json
{
  "mcpServers": {
    "pdf-reader": {
      "command": "python",
      "args": ["/path/to/tsaol-pdf-reader-mcp/src/main.py"],
      "name": "PDF Reader (Python)"
    }
  }
}
```

## API

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

## Security

- All file access is restricted to the project root directory
- Path traversal protection
- Input validation with Pydantic models

## License

MIT