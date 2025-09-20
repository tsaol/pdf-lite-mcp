#!/usr/bin/env python3
"""
Simple test script for tsaol-pdf-reader-mcp.
Tests basic imports and model validation.
"""

import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

def test_imports():
    """Test that all modules can be imported."""
    print("🔍 Testing imports...")

    try:
        from src.models import ReadPdfRequest, PdfSource
        print("✅ Models imported successfully")
    except Exception as e:
        print(f"❌ Models import failed: {e}")
        return False

    try:
        from src.utils import PathUtils
        print("✅ Utils imported successfully")
    except Exception as e:
        print(f"❌ Utils import failed: {e}")
        return False

    return True

def test_path_utils():
    """Test path utilities."""
    print("\n🔍 Testing path utilities...")

    try:
        from src.utils import PathUtils
        path_utils = PathUtils()

        # Test safe path
        safe_path = path_utils.resolve_path("test.txt")
        print(f"✅ Safe path resolved: {safe_path}")

        # Test path traversal prevention
        try:
            path_utils.resolve_path("../../../etc/passwd")
            print("❌ Path traversal not prevented!")
        except Exception as e:
            print(f"✅ Path traversal prevented: {type(e).__name__}")

    except Exception as e:
        print(f"❌ Path utils test failed: {e}")

def test_models():
    """Test model validation."""
    print("\n🔍 Testing model validation...")

    try:
        from src.models import ReadPdfRequest, PdfSource

        # Test valid request
        request = ReadPdfRequest(
            sources=[PdfSource(path="test.pdf")]
        )
        print(f"✅ Valid request created")

        # Test invalid request (both path and url)
        try:
            invalid_request = ReadPdfRequest(
                sources=[PdfSource(path="test.pdf", url="http://example.com/test.pdf")]
            )
            print("❌ Invalid request not caught!")
        except Exception as e:
            print(f"✅ Invalid request caught: {type(e).__name__}")

    except Exception as e:
        print(f"❌ Model test failed: {e}")

def test_formatting():
    """Test formatting functions."""
    print("\n🔍 Testing formatting functions...")

    try:
        from src.utils import format_error_for_amazon_q, clean_pdf_text, truncate_text

        # Test error formatting
        error = FileNotFoundError("test file not found")
        formatted = format_error_for_amazon_q(error)
        print(f"✅ Error formatting: {formatted}")

        # Test text cleaning
        dirty_text = "  Multiple   spaces\n\n\n\nand lines  "
        clean = clean_pdf_text(dirty_text)
        print(f"✅ Text cleaning: '{clean}'")

        # Test truncation
        long_text = "A" * 100
        truncated = truncate_text(long_text, 50)
        print(f"✅ Text truncation: {len(truncated)} chars")

    except Exception as e:
        print(f"❌ Formatting test failed: {e}")

def main():
    """Run all tests."""
    print("🧪 Running simple tests for tsaol-pdf-reader-mcp\n")

    success = test_imports()
    if not success:
        print("\n❌ Import tests failed, stopping.")
        return

    test_path_utils()
    test_models()
    test_formatting()

    print("\n✨ Simple tests completed!")

if __name__ == "__main__":
    main()