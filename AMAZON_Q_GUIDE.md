# Amazon Q CLI Integration Guide

This guide shows how to use `tsaol-pdf-reader-mcp` with Amazon Q CLI for optimal PDF processing experience.

## Quick Setup

1. **Install Dependencies**
   ```bash
   cd tsaol-pdf-reader-mcp
   pip install -r requirements.txt
   ```

2. **Configure Amazon Q CLI**
   Add to your MCP configuration file:

   ```json
   {
     "mcpServers": {
       "tsaol-pdf-reader": {
         "command": "python",
         "args": ["-m", "src.main"],
         "name": "PDF Reader (tsaol)",
         "cwd": "/path/to/tsaol-pdf-reader-mcp"
       }
     }
   }
   ```

3. **Test Connection**
   ```bash
   # Test if the server starts correctly
   python src/main.py
   ```

## Optimizations for Amazon Q CLI

### 🎯 Concise Output Format
- **Single PDF**: Clean, structured display with emojis for easy scanning
- **Multiple PDFs**: Tabular summary with expandable details
- **Error Messages**: Clear, actionable error descriptions with context

### ⚡ Performance Features
- **Page-specific extraction**: Only process requested pages
- **Text truncation**: Automatic text limiting for Q CLI display
- **Metadata filtering**: Show only relevant metadata fields
- **Clean text formatting**: Normalized whitespace and line breaks

### 🛡️ Security Features
- **Path confinement**: All file access restricted to project root
- **Input validation**: Comprehensive argument checking
- **Error isolation**: Single PDF failures don't affect batch processing

## Usage Examples

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

**Amazon Q CLI Output:**
```
📄 ./document.pdf
📊 Pages: 5
📝 Title: Sample Document | Author: John Doe
📖 Full Text:
This is the content of the PDF document...
```

### Specific Pages
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

### Multiple PDFs
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

### Error Handling
When a PDF cannot be processed:

```
❌ Failed to process ./missing.pdf:
📁 File Not Found: File not found: ./missing.pdf
```

## Best Practices for Amazon Q CLI

### 1. **Batch Processing**
Process multiple related PDFs in a single request for efficiency:
```json
{
  "sources": [
    {"path": "./chapter1.pdf"},
    {"path": "./chapter2.pdf"},
    {"path": "./chapter3.pdf"}
  ]
}
```

### 2. **Selective Content**
Only request what you need:
- Use `include_full_text: false` if you only need metadata
- Specify `pages` for large documents to avoid overwhelming output
- Set `include_metadata: false` for simple text extraction

### 3. **Error Recovery**
The server is designed to continue processing even if individual PDFs fail:
```json
{
  "sources": [
    {"path": "./good.pdf"},
    {"path": "./missing.pdf"},
    {"path": "./another-good.pdf"}
  ]
}
```
Results will show success/failure for each source independently.

## Troubleshooting

### Common Issues

**1. Module Import Errors**
```bash
# Ensure Python path is correct
export PYTHONPATH=/path/to/tsaol-pdf-reader-mcp:$PYTHONPATH
```

**2. PDF Processing Errors**
- Check file permissions
- Verify PDF is not corrupted
- Ensure sufficient memory for large PDFs

**3. URL Access Issues**
- Check network connectivity
- Verify URL returns PDF content
- Some URLs may require authentication

### Debug Mode
Set environment variable for detailed logging:
```bash
export DEBUG=1
python src/main.py
```

## Performance Tips

1. **Local Files**: Faster than URLs, use when possible
2. **Page Ranges**: More efficient than full text for large PDFs
3. **Metadata Only**: Use for quick PDF inspection
4. **Batch Requests**: Process related PDFs together

## Integration Examples

### Research Workflow
```bash
# Process academic papers
q: "Use read_pdf to extract abstracts from papers/*.pdf, pages 1 only"
```

### Document Analysis
```bash
# Analyze contract terms
q: "Read contract.pdf and extract key terms from pages 5-10"
```

### Report Generation
```bash
# Combine multiple report sections
q: "Extract executive summaries from quarterly-reports/*.pdf"
```