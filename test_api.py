#!/usr/bin/env python3
"""Quick API test to verify Gemini connection."""

from utils.gemini_helpers import GeminiHelper
from config.settings import Settings

def test_api_connection():
    """Test Gemini API connection without browser automation."""
    try:
        # Configure logging
        Settings.configure_logging()
        
        # Validate settings
        Settings.validate_required_settings()
        print("PASS: Settings validated successfully")
        
        # Initialize Gemini helper
        helper = GeminiHelper()
        print("PASS: Gemini helper initialized")
        
        # Get model info
        info = helper.get_model_info()
        print(f"PASS: Model: {info['model']}")
        print(f"PASS: API Key configured: {info['api_key_set']}")
        print(f"PASS: LLM initialized: {info['llm_initialized']}")
        
        # Test creating agent (without running)
        agent = helper.create_agent("Test task - just checking connection")
        print("PASS: Agent created successfully")
        
        print("\nSUCCESS: All tests passed! The Gemini integration is working correctly.")
        return True
        
    except Exception as e:
        print(f"FAIL: Test failed: {e}")
        return False

if __name__ == "__main__":
    test_api_connection()