# 🤖 Multi-Agent Customer Support Automation

A cutting-edge customer support system powered by AI agents using CrewAI and Streamlit. This application leverages multiple AI agents to provide intelligent, comprehensive, and high-quality responses to customer inquiries.

## 🌟 Features

- **🧠 Multi-Agent System**: Utilizes multiple AI agents working together for optimal customer support
  - **Senior Support Representative**: Handles initial inquiry resolution with comprehensive answers
  - **Quality Assurance Specialist**: Reviews and ensures high-quality support responses
  
- **🌐 Web Scraping Capabilities**: Automatically gathers relevant information from knowledge bases
- **💬 Interactive Chat Interface**: User-friendly Streamlit-based interface for seamless customer interactions
- **📝 Chat History**: Maintains conversation history for context and reference
- **⚡ Real-time Processing**: Quick response generation with OpenAI's GPT-4 models

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/fahamgeer177/Multi-Agent-Customer-Support-Automation.git
   cd Multi-Agent-Customer-Support-Automation
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   ```

    Activate it:

    - On Windows (PowerShell):
       ```powershell
       .\venv\Scripts\Activate.ps1
       ```
    - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root (or copy `.env.example`):
   ```
   OPENAI_API_KEY=your_api_key_here
   OPENAI_MODEL_NAME=gpt-4o-mini
   ```
   
   ⚠️ **Important**: Never hardcode your API key in the source code. Always use environment variables or `.env` files.

## 🎯 Usage

Run the Streamlit application:
```bash
streamlit run Multi_Agent_Customer_Support_Automation_Frontend.py
```

Then:
1. Open your browser (typically `http://localhost:8501`)
2. Enter the **Customer Name** (e.g., "GenWizz")
3. Enter the **Person Name** (e.g., "Fahamgeer")
4. Type your support inquiry in the message box
5. Click **Send** and wait for the AI agents to process your request
6. View the response and conversation history

## 🏗️ Project Structure

```
Multi-Agent-Customer-Support-Automation/
├── Multi_Agent_Customer_Support_Automation_Frontend.py  # Main Streamlit app
├── requirements.txt                                      # Python dependencies
├── README.md                                             # Project documentation
├── .gitignore                                            # Ignored local/secrets files
└── .env                                                  # Local environment variables (not committed)
```

## 🔧 How It Works

1. **User Input**: Customer provides their inquiry along with company and person name
2. **Support Agent Processing**: The Senior Support Representative analyzes the inquiry and provides a detailed response
3. **Quality Assurance Review**: The QA Specialist reviews the response for accuracy and completeness
4. **Response Delivery**: The final refined response is displayed to the user
5. **History Management**: Conversations are stored for future reference

## 📦 Dependencies

- **streamlit**: Interactive web application framework
- **crewai**: Multi-agent orchestration framework
- **crewai-tools**: Tools and utilities for CrewAI agents
- **openai**: OpenAI API client
- **python-dotenv**: Environment variable management
- **requests**: HTTP library for web requests

## 🔐 Security

⚠️ **Important Security Notes:**
- Never commit your `.env` file with API keys
- Use environment variables for all sensitive information
- Rotate your API keys periodically

### .gitignore Template
```
venv/
__pycache__/
.env
.DS_Store
*.pyc
.streamlit/
```

## 🛠️ Customization

### Change the Knowledge Base URL
Edit line 47 in `Multi_Agent_Customer_Support_Automation_Frontend.py`:
```python
docs_scrape_tool = ScrapeWebsiteTool(
    website_url="your_website_url_here"
)
```

### Modify Agent Behavior
Customize the agent roles, goals, and backstories in the "Define agents" section to match your business needs.

## 📝 Example Use Cases

- Troubleshooting product issues
- Feature inquiries and product information
- Account and billing support
- Technical assistance
- General customer support

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT

## 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub or contact the author.

---

**Made with ❤️ | © 2026 Customer Support Automation**
