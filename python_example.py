import ollama

response = ollama.generate(
    model="llama3", 
    prompt="Write a poem about nature."
    )

print(response)



# pip install ollama