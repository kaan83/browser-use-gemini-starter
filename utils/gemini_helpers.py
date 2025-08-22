import os
import logging
from typing import Optional, Dict, Any
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class GeminiHelper:
    """Helper class for Gemini AI integration with browser automation."""
    
    def __init__(self, model: str = "gemini-2.0-flash-exp"):
        """Initialize Gemini helper with specified model."""
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.model = model
        self.llm = None
        
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY environment variable is required")
        
        self._initialize_llm()
    
    def _initialize_llm(self):
        """Initialize the Gemini language model."""
        try:
            self.llm = ChatGoogleGenerativeAI(
                model=self.model,
                google_api_key=self.api_key
            )
            logger.info(f"Initialized Gemini model: {self.model}")
        except Exception as e:
            logger.error(f"Failed to initialize Gemini model: {e}")
            raise
    
    def create_agent(self, task: str, **kwargs) -> Agent:
        """Create a browser automation agent with Gemini AI."""
        if not self.llm:
            raise RuntimeError("Gemini LLM not initialized")
        
        return Agent(
            task=task,
            llm=self.llm,
            **kwargs
        )
    
    async def run_automation_task(self, task: str, **kwargs) -> Any:
        """Run a browser automation task using Gemini AI."""
        agent = self.create_agent(task, **kwargs)
        
        try:
            logger.info(f"Starting automation task: {task}")
            result = await agent.run()
            logger.info("Automation task completed successfully")
            return result
        except Exception as e:
            logger.error(f"Automation task failed: {e}")
            raise
    
    def get_model_info(self) -> Dict[str, str]:
        """Get information about the current Gemini model."""
        return {
            "model": self.model,
            "api_key_set": bool(self.api_key),
            "llm_initialized": self.llm is not None
        }