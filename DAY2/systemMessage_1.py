import ollama
response=ollama.chat(
    model="llama.3.2:3b",
    messages=[
        {
            "role":"system",
            "content":"You are a helpful assistant."
        }
    ]
)




