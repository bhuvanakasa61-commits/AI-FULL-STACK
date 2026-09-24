import ollama
while True:
    question=input("Ask a question?:")
    if question.lower()=="exit":
        break
    response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
          "content": "GIVE IN 2-3 LINES"
        },

        {
            "role": "user",
            "content": question
        }
    ]
)
print(response["message"]["content"])
