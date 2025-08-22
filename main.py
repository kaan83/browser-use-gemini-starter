#!/usr/bin/env python3
"""
Browser-Use Gemini Starter Kit
Main demonstration script for browser automation with Gemini AI.
"""

import asyncio
import logging
from utils.gemini_helpers import GeminiHelper
from config.settings import Settings

async def demo_search_automation():
    """Demonstrate basic search automation."""
    helper = GeminiHelper()
    
    task = "Go to Google, search for 'browser automation with AI', and take a screenshot of the results"
    
    try:
        result = await helper.run_automation_task(task)
        print(f"Search automation completed: {result}")
    except Exception as e:
        print(f"Search automation failed: {e}")

async def demo_ecommerce_automation():
    """Demonstrate e-commerce site automation."""
    helper = GeminiHelper()
    
    task = "Go to an e-commerce site, search for 'laptop', and compare prices of the first 3 results"
    
    try:
        result = await helper.run_automation_task(task)
        print(f"E-commerce automation completed: {result}")
    except Exception as e:
        print(f"E-commerce automation failed: {e}")

async def demo_form_automation():
    """Demonstrate form filling automation."""
    helper = GeminiHelper()
    
    task = "Find a contact form on a website and fill it with sample data"
    
    try:
        result = await helper.run_automation_task(task)
        print(f"Form automation completed: {result}")
    except Exception as e:
        print(f"Form automation failed: {e}")

async def main():
    """Main function to run demonstrations."""
    # Configure logging
    Settings.configure_logging()
    
    # Validate settings
    try:
        Settings.validate_required_settings()
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please check your .env file and ensure GOOGLE_API_KEY is set")
        return
    
    print("Browser-Use Gemini Starter Kit")
    print("==============================")
    print()
    
    # Show configuration info
    helper = GeminiHelper()
    info = helper.get_model_info()
    print(f"Model: {info['model']}")
    print(f"API Key configured: {info['api_key_set']}")
    print(f"LLM initialized: {info['llm_initialized']}")
    print()
    
    # Run demonstrations
    demos = [
        ("Search Automation", demo_search_automation),
        ("E-commerce Automation", demo_ecommerce_automation),
        ("Form Automation", demo_form_automation)
    ]
    
    for name, demo_func in demos:
        print(f"Running {name}...")
        try:
            await demo_func()
        except Exception as e:
            print(f"{name} failed: {e}")
        print("-" * 40)

if __name__ == "__main__":
    asyncio.run(main())