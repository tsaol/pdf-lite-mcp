#!/usr/bin/env python3
"""
Manual test script - step by step testing
"""

import sys
import asyncio
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

async def manual_test():
    """Interactive manual testing."""
    print("🧪 Manual Testing Mode")
    print("=" * 50)

    from src.main import call_tool

    while True:
        print("\n📋 Choose a test:")
        print("1. Test invalid arguments")
        print("2. Test file not found")
        print("3. Test URL PDF (requires internet)")
        print("4. Test with your own PDF file")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            print("\n🔍 Testing invalid arguments...")
            result = await call_tool("read_pdf", {})
            print("Response:", result[0].text if result else "No response")

        elif choice == "2":
            print("\n🔍 Testing file not found...")
            args = {"sources": [{"path": "missing.pdf"}]}
            result = await call_tool("read_pdf", args)
            print("Response:", result[0].text if result else "No response")

        elif choice == "3":
            print("\n🔍 Testing URL PDF...")
            args = {
                "sources": [{"url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"}],
                "include_full_text": True
            }
            result = await call_tool("read_pdf", args)
            print("Response:", result[0].text if result else "No response")

        elif choice == "4":
            pdf_path = input("Enter PDF file path: ").strip()
            if pdf_path:
                print(f"\n🔍 Testing with {pdf_path}...")
                args = {
                    "sources": [{"path": pdf_path}],
                    "include_metadata": True,
                    "include_page_count": True,
                    "include_full_text": True
                }
                result = await call_tool("read_pdf", args)
                print("Response:", result[0].text if result else "No response")

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    asyncio.run(manual_test())