import os
import logging
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Global settings configuration for the browser-use-gemini application."""
    
    # API Configuration
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash-exp")
    
    # Browser Configuration
    BROWSER_TYPE = os.getenv("BROWSER_TYPE", "chromium")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    VIEWPORT_WIDTH = int(os.getenv("VIEWPORT_WIDTH", "1280"))
    VIEWPORT_HEIGHT = int(os.getenv("VIEWPORT_HEIGHT", "720"))
    
    # Timeouts and Performance
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "30000"))
    SLOW_MO = int(os.getenv("SLOW_MO", "0"))
    
    # Logging Configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # Environment
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    
    @classmethod
    def configure_logging(cls):
        """Configure logging based on settings."""
        logging.basicConfig(
            level=getattr(logging, cls.LOG_LEVEL),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    @classmethod
    def validate_required_settings(cls) -> bool:
        """Validate that all required settings are present."""
        if not cls.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY is required")
        return True
    
    @classmethod
    def get_browser_config(cls) -> Dict[str, Any]:
        """Get browser configuration as dictionary."""
        return {
            "browser_type": cls.BROWSER_TYPE,
            "headless": cls.HEADLESS,
            "viewport": {
                "width": cls.VIEWPORT_WIDTH,
                "height": cls.VIEWPORT_HEIGHT
            },
            "timeout": cls.DEFAULT_TIMEOUT,
            "slow_mo": cls.SLOW_MO
        }
    
    @classmethod
    def is_development(cls) -> bool:
        """Check if running in development environment."""
        return cls.ENVIRONMENT == "development"