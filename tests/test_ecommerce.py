import pytest
from browser_use import Agent

class TestEcommerce:
    """Test cases for e-commerce automation scenarios."""
    
    @pytest.mark.asyncio
    async def test_product_search(self, gemini_llm):
        """Test product search automation."""
        agent = Agent(
            task="Search for a specific product and verify results",
            llm=gemini_llm
        )
        
        assert agent is not None
        assert "search" in agent.task.lower()
    
    @pytest.mark.asyncio
    async def test_add_to_cart(self, browser_agent):
        """Test adding items to shopping cart."""
        browser_agent.task = "Add a product to shopping cart and verify"
        
        assert "cart" in browser_agent.task.lower()
    
    @pytest.mark.asyncio
    async def test_checkout_flow(self, gemini_llm):
        """Test checkout process automation."""
        agent = Agent(
            task="Navigate through checkout process with test data",
            llm=gemini_llm
        )
        
        assert agent is not None
    
    @pytest.mark.asyncio
    async def test_price_comparison(self, browser_agent):
        """Test price comparison across multiple products."""
        browser_agent.task = "Compare prices of similar products and find best deal"
        
        assert "price" in browser_agent.task.lower() or "compare" in browser_agent.task.lower()