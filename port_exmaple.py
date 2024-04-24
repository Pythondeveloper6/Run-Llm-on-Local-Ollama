import os

# Define the Ollama base URL with your desired port (replace 11435 with the actual port)
os.environ['OLLAMA_BASE_URL'] = 'http://localhost:11435'

from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

response = llm.invoke("tell me a joke")

print(response)
