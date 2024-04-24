from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

response = llm.invoke("tell me a joke")


print(response)


# pip install langchain langchain_community