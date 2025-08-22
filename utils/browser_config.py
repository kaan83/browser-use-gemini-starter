import os
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class BrowserConfig:
    """Configuration class for browser automation settings."""
    
    @staticmethod
    def get_browser_settings() -> Dict[str, Any]:
        """Get browser configuration from environment variables."""
        return {
            "browser_type": os.getenv("BROWSER_TYPE", "chromium"),
            "headless": os.getenv("HEADLESS", "false").lower() == "true",
            "viewport": {
                "width": int(os.getenv("VIEWPORT_WIDTH", "1280")),
                "height": int(os.getenv("VIEWPORT_HEIGHT", "720"))
            },
            "timeout": int(os.getenv("TIMEOUT", "30000")),
            "slow_mo": int(os.getenv("SLOW_MO", "0"))
        }
    
    @staticmethod
    def get_playwright_config() -> Dict[str, Any]:
        """Get Playwright-specific configuration."""
        settings = BrowserConfig.get_browser_settings()
        
        return {
            "headless": settings["headless"],
            "viewport": settings["viewport"],
            "timeout": settings["timeout"],
            "slow_mo": settings["slow_mo"]
        }
    
    @staticmethod
    def is_development_mode() -> bool:
        """Check if running in development mode."""
        return os.getenv("ENVIRONMENT", "development") == "development"