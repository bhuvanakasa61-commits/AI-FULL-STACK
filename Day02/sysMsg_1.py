import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
          "content": "Give the answer in 2-3 lines"
        },

        {
            "role": "user",
            "content": "what is AI "
        }
    ]
)
print(response["message"]["content"])
