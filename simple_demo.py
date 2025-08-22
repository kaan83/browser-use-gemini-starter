#!/usr/bin/env python3
"""Simple demo to test browser automation with Gemini AI."""

import asyncio
from utils.gemini_helpers import GeminiHelper

async def simple_google_search():
    """Simple test: Google search automation."""
    print("Starting Google search test...")
    
    helper = GeminiHelper()
    
    # Simple task that should complete quickly
    task = "Go to google.com and search for 'Python programming'"
    
    try:
        print(f"Task: {task}")
        result = await helper.run_automation_task(task)
        print("PASS: Google search completed successfully")
        return True
    except Exception as e:
        print(f"FAIL: Google search failed: {e}")
        return False

async def main():
    """Run the simple demo."""
    print("Browser-Use Gemini Demo Test")
    print("============================")
    
    # Run simple test
    success = await simple_google_search()
    
    if success:
        print("\nSUCCESS: Demo completed successfully!")
    else:
        print("\nFAIL: Demo encountered issues")

if __name__ == "__main__":
    asyncio.run(main())