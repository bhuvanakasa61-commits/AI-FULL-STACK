import ollama
import streamlit as st
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("You: ")
if question:
    with st.chat_message("user"):
        st.write("User:",question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )
    with st.spinner("Thinking.."):
        response = ollama.chat(
            model="llama3.2:3b",
            messages=st.session_state.messages
    )
    with st.chat_message("assistant"):
        st.write(response["message"]["content"])
        st.session_state.messages.append(

        {
            "role": "assistant",
            "content": response["message"]["content"]
        }
    )
    st.write("AI:", response["message"]["content"])
uploaded_file=st.file_uploader("upload a file..")
if uploaded_file is not None:
    st.write("File uploaded successfully")
    context=uploaded_file.read().decode("utf-8")
    st.text(context)