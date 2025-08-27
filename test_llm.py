from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Instanced Ollama LLM model of choice
llm = OllamaLLM(model="gemma3:1b")

# Define the prompt using a template
prompt_template = PromptTemplate(
    input_variables=["topic"], template="Me dê uma breve descrição sobre {topic}."
)

# Create the chain that combines the prompt and the LLM
chain = prompt_template | llm

# Call the chain with the topic you want
response = chain.invoke({"topic": "Inteligência Artificial"})

# Print the result
print(response)
