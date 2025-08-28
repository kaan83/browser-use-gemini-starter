#!/usr/bin/env python3
"""Simple demo to test browser automation with Gemini AI."""

import asyncio
from utils.gemini_helpers import GeminiHelper

async def login_test_demo():
    """Login test automation using the-internet.herokuapp.com."""
    print("Starting login test demo...")
    
    helper = GeminiHelper()
    
    # Task with specific steps for login automation
    task = """Go to 'https://the-internet.herokuapp.com/login'. On the page username and password for login is written, enter the credentials you get from page to username and password textboxes, click login button, verify that you logged in"""
    
    try:
        print(f"Task: {task}")
        result = await helper.run_automation_task(task)
        print("PASS: Login test completed successfully")
        return True
    except Exception as e:
        print(f"FAIL: Login test failed: {e}")
        return False

async def main():
    """Run the simple demo."""
    print("Browser-Use Gemini Login Demo Test")
    print("==================================")
    
    # Run login test
    success = await login_test_demo()
    
    if success:
        print("\nSUCCESS: Demo completed successfully!")
    else:
        print("\nFAIL: Demo encountered issues")

if __name__ == "__main__":
    asyncio.run(main())