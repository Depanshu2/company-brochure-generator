# 🏢 Company Brochure Generator (LLM + Web Scraper)

The **Company Brochure Generator** is a lightweight and intelligent project that automatically creates a professional company brochure using **Large Language Models (LLMs)**.  
It scrapes a company’s website to extract relevant information (like *About Us*, *Careers*, *Products*, etc.), generates a well-structured brochure, and finally translates it into any language you choose.

---

## ✨ Features

- 🔗 **Smart Link Filtering:** Identifies relevant links such as About, Careers, and Product pages.
- 🧠 **LLM-Powered Summarization:** Uses Groq-hosted LLMs (`gpt-oss-120b`, `llama-3.1-8b-instant`) to write a clear, concise company brochure.
- 🌐 **Language Translation:** Translates the final brochure into any desired language.
- ⚙️ **Fully Automated:** Input the company name and homepage URL — get a complete Markdown brochure instantly.
- 💡 **Customizable Prompts:** Easy to modify system and user prompts for different tone or brochure types.

---

## 🧰 Tech Stack

| Tool / Library | Purpose |
|----------------|----------|
| **Python 3.10+** | Core programming language |
| **Groq API** | LLM inference for text generation |
| **Requests** | Fetches webpage HTML |
| **BeautifulSoup** *(optional)* | Extracts clean text from HTML pages |
| **dotenv** | Manages API keys securely |
| **IPython Markdown** | Displays formatted output in notebooks |

---

## 🚀 How It Works

1. **Extracts all links** from a company’s homepage using `scraper.py`
2. **Filters relevant links** (About, Careers, etc.) using Groq LLM (`gpt-oss-120b`)
3. **Scrapes content** from the selected pages
4. **Generates brochure content** using LLM (`llama-3.1-8b-instant`)
5. **Translates the brochure** into a target language (e.g., Hindi, Spanish, French, etc.)

---

## 📁 Project Structure


## 🚀 Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.10+
- `pip` (Python package manager)
- Groq API key

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/company-brochure-generator.git

# Navigate to project folder
cd company-brochure-generator

# Install dependencies
pip install -r requirements.txt


