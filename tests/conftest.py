import pytest
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent

load_dotenv()

@pytest.fixture
def gemini_llm():
    """Fixture to provide Gemini LLM instance for testing."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        pytest.skip("GOOGLE_API_KEY not set")
    
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp",
        google_api_key=api_key
    )

@pytest.fixture
def browser_agent(gemini_llm):
    """Fixture to provide browser agent with Gemini integration."""
    return Agent(
        task="Test automation task",
        llm=gemini_llm
    )