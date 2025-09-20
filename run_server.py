#!/usr/bin/env python3
"""
Standalone entry point for the pdf-reader-mcp server.
This script properly sets up the Python path and starts the MCP server.
"""

import sys
from pathlib import Path

# Add the src directory to Python path
src_dir = Path(__file__).parent / "src"
sys.path.insert(0, str(src_dir))

# Now import and run the main server
if __name__ == "__main__":
    from main import main
    import asyncio
    asyncio.run(main())