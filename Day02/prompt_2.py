import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
         {
           "role":"user",
 	   "content": "Act as lecturer exlpain about ai in 2lines.give me the bullet points about three main types of AI"
	  }
        ]
)
print(response["message"]["content"])