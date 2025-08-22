# Browser-Use Gemini Starter Kit

A comprehensive starter kit for building browser automation applications using Google's Gemini AI and the browser-use Python library. Perfect for conference workshops and learning browser automation with AI.

## 🚀 Features

- **AI-Powered Automation**: Leverage Google's Gemini AI for intelligent browser control
- **Natural Language Tasks**: Define automation tasks in plain English
- **Multi-Browser Support**: Works with Chromium, Firefox, and WebKit via Playwright
- **Test Suite Included**: Complete test examples for login and e-commerce scenarios
- **Docker Ready**: Containerized setup for easy deployment
- **CI/CD Pipeline**: GitHub Actions workflow for automated testing

## 📋 Prerequisites

- Python 3.11 or higher
- Google Gemini API key
- Git (for version control)

## 🛠️ Quick Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/testconf/browser-use-gemini-starter.git
   cd browser-use-gemini-starter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your GOOGLE_API_KEY
   ```

4. **Run the demo**
   ```bash
   python main.py
   ```

## 🔧 Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

- `GOOGLE_API_KEY`: Your Google Gemini API key (required)
- `BROWSER_TYPE`: Browser to use (chromium, firefox, webkit)
- `HEADLESS`: Run browser in headless mode (true/false)
- `VIEWPORT_WIDTH/HEIGHT`: Browser window dimensions

### Getting a Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file

## 📖 Usage Examples

### Basic Search Automation

```python
from utils.gemini_helpers import GeminiHelper

async def search_example():
    helper = GeminiHelper()
    task = "Go to Google and search for 'Python automation'"
    result = await helper.run_automation_task(task)
    return result
```

### E-commerce Automation

```python
async def shopping_example():
    helper = GeminiHelper()
    task = "Find the cheapest laptop under $1000 on an e-commerce site"
    result = await helper.run_automation_task(task)
    return result
```

### Form Automation

```python
async def form_example():
    helper = GeminiHelper()
    task = "Fill out a contact form with sample data"
    result = await helper.run_automation_task(task)
    return result
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest tests/ -v

# Run specific test categories
pytest tests/test_login.py -v
pytest tests/test_ecommerce.py -v
```

## 📁 Project Structure

```
browser-use-gemini-starter/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── main.py               # Demo script
├── Dockerfile           # Container configuration
├── .github/
│   └── workflows/
│       └── test.yml     # CI/CD pipeline
├── tests/               # Test suite
│   ├── __init__.py
│   ├── conftest.py     # Test configuration
│   ├── test_login.py   # Login automation tests
│   └── test_ecommerce.py # E-commerce tests
├── utils/               # Utility modules
│   ├── __init__.py
│   ├── browser_config.py # Browser settings
│   └── gemini_helpers.py # Gemini AI integration
└── config/
    └── settings.py      # Global configuration
```

## 🐳 Docker Usage

Build and run with Docker:

```bash
# Build the image
docker build -t browser-use-gemini .

# Run the container
docker run -e GOOGLE_API_KEY=your_key_here browser-use-gemini
```

## 🎯 Workshop Activities

### Activity 1: Basic Automation
Create a script that:
1. Opens a news website
2. Searches for today's top story
3. Takes a screenshot of the results

### Activity 2: Data Extraction
Build an automation that:
1. Visits a job board
2. Searches for Python developer positions
3. Extracts job titles and companies

### Activity 3: Form Testing
Develop a test that:
1. Finds a registration form
2. Tests form validation
3. Submits valid data

## 🔍 Common Use Cases

- **Web Scraping**: Extract data from dynamic websites
- **Testing**: Automated UI testing with AI guidance
- **Monitoring**: Monitor websites for changes
- **Lead Generation**: Automate data collection
- **Social Media**: Automate social media interactions

## 🚨 Best Practices

1. **Rate Limiting**: Always respect website rate limits
2. **Error Handling**: Implement robust error handling
3. **Logging**: Use proper logging for debugging
4. **Security**: Never commit API keys to version control
5. **Testing**: Write tests for your automation scripts

## 🛡️ Ethical Considerations

- Always check robots.txt before automating
- Respect website terms of service
- Don't overload servers with requests
- Use automation responsibly

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📚 Additional Resources

- [Browser-Use Documentation](https://github.com/browser-use/browser-use)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Playwright Documentation](https://playwright.dev/python/)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

- Create an issue for bugs or feature requests
- Join our community discussions
- Check out the examples in the `tests/` directory

## 🎉 Conference Notes

This starter kit is designed for hands-on learning in conference workshops. Each section builds upon the previous one, making it easy to follow along and experiment with browser automation and AI integration.

Happy automating! 🤖