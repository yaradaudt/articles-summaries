# 📰 AI Article Summarizer

An intelligent web application that uses Artificial Intelligence to generate concise and informative summaries of online articles. The project combines web scraping for content extraction and a local Large Language Model (LLM) for processing and generating summaries. Feel free to clone, fork, contribute or use it for learning. The "env" example file is made for you to include your own User Agent. 

## 🎯 Purpose

This project was developed to facilitate reading and understanding of long articles by transforming extensive content into clear and objective summaries. Perfect for:

- Researchers who need to review multiple articles quickly
- Students seeking to understand complex concepts in a summarized way
- Professionals who need to extract key information from reports and articles
- Anyone interested in optimizing their reading time

## 🛠️ Technologies Used

### Frontend & Interface
- **Streamlit**: Web framework for creating the user interface

### Backend & Processing
- **Python 3.13**: Main programming language
- **BeautifulSoup4**: Library for web scraping and HTML parsing
- **Requests**: For making HTTP requests and accessing URLs

### Artificial Intelligence
- **LangChain**: Framework for developing LLM applications
- **Ollama**: For local execution of language models
- **Gemma 3:1B**: Local language model used for summary generation

## 🤖 About Local LLM Usage

This project uses a **locally executed Large Language Model** through Ollama, ensuring:

- **Complete privacy**: Your data is not sent to external servers
- **No API costs**: No need for API keys or payments
- **Offline processing**: Works even without internet connection
- **Full control**: You have complete control over the model used

### Flexibility for External APIs

The environment is prepared for easy integration with external APIs (such as OpenAI, Anthropic, etc.) with few code modifications. Simply change the LLM configuration in the `main.py` file.

## 📋 Prerequisites

Before starting, make sure you have installed:

- **Python 3.13** or higher
- **Git** to clone the repository
- **Ollama** installed and configured locally

### Installing Ollama

1. Visit [ollama.ai](https://ollama.ai)
2. Download and install Ollama for your operating system
3. After installation, run in terminal:
   ```bash
   ollama pull gemma3:1b
   ```

## 🚀 How to Clone and Run the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/yaradaudt/articles-summaries.git
cd articles-summaries
```

### Step 2: Create and Activate Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

The application will automatically open in your default browser, usually at `http://localhost:8501`.

## 📖 How to Use

1. **Paste the URL**: Insert the URL of the article you want to summarize in the text field
2. **Click "Generate summary"**: The system will:
   - Extract the article content
   - Process the text through AI
   - Generate a concise and informative summary
3. **Read the summary**: The result will be displayed on screen

## 🔧 Project Structure

```
articles-summaries/
├── app.py              # Main Streamlit interface
├── main.py             # Processing and AI logic
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── LICENSE             # MIT License
```

## 🐛 Troubleshooting

### Error accessing URLs
- Check if the URL is correct and accessible
- Some sites may block web scraping
- Try URLs from different sources

### Ollama error
- Make sure Ollama is running: `ollama serve`
- Check if the model is downloaded: `ollama list`
- Download the model again if necessary: `ollama pull gemma3:1b`

### Dependency issues
- Make sure the virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version`

---

**Developed with ❤️ using Python and local AI**
