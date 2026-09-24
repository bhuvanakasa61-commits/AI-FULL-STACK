import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
          "content": "imagine your'e a my friend bhuvanakruthi and explain about the content in 2-3lines"
        },

        {
            "role": "user",
            "content": "what is AI "
        }
    ]
)
print(response["message"]["content"])
