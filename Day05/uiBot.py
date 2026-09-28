import ollama
import streamlit as st
st.title(":orange[CHATBOT👽] \:tulip:")



with st.sidebar:
    personalities={
        "toddler":"generate answer as considering the user as todd,er.give answer in 2-3 lines only.",
        "lion":"generate answer as considering the user as lion.give answer in 2-3 lines only."}
    personality=st.selectbox("select a personality",personalities.keys())

    if st.button("clear chat🚮"):
        st.session_state.messages=[]
        st.success("chat cleared successfully...")
    st.header("Chat Settings")
    uploaded_file=st.file_uploader("upload a file..")
    if uploaded_file is not None:
        st.write("File uploaded successfully")
        with st.expander("Preview"):
            context=uploaded_file.read().decode("utf-8")
            st.text(context)
         
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
            messages=[{
                "role":"system","content":"Give answer in 2 lines only"
            }]+st.session_state.messages
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

st.balloons()
st.snow()