import requests
from bs4 import BeautifulSoup
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate


# Web scraping function
def extract_text_from_url(url):
    """
    Extrai o texto principal de um artigo a partir de uma URL.
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
    }

    try:
        # URL request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Levanta um erro para códigos HTTP ruins

        # Parses the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Tries to find the main text in common article tags
        main_content = (
            soup.find("div", class_="content")
            or soup.find("article")
            or soup.find("main")
        )

        if not main_content:
            # If not found, assume that the text is in all paragraphs
            paragraphs = soup.find_all("p")
            whole_text = " ".join([p.get_text() for p in paragraphs])
        else:
            paragraphs = main_content.find_all("p")
            whole_text = " ".join([p.get_text() for p in paragraphs])

        return whole_text.strip()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return None
    except Exception as e:
        print(f"Erro ao processar o HTML: {e}")
        return None


# --- LLM logic (copied from test script) ---
# Instances the Ollama LLM model
llm = OllamaLLM(model="gemma3:1b")

# Defines the prompt for the summary
prompt_template_summary = PromptTemplate(
    input_variables=["text"],
    template="""
    Você é um assistente de resumo. Sua tarefa é criar um resumo conciso e
    informativo do texto a seguir. O resumo deve capturar as ideias principais
    e ser de fácil leitura.

    TEXTO:
    {text}
    """,
)

# Creates the chain that joins the prompt and the LLM together
chain = prompt_template_summary | llm


# --- Main Logics ---
def generate_url_summary(url):
    extracted_text = extract_text_from_url(url)
    if extracted_text:
        summary = chain.invoke({"text": extracted_text})
        return summary
    return None
