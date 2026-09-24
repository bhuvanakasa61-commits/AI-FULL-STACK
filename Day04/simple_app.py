import streamlit as st
st.title("Welcome to my first App")
name=st.text_input("Enter your name:")
email=st.chat_input("Enter your email:")
st.sidebar.title("About")
st.sidebar.info("This is my first app using streamlit and ollama")
st.subheader("This is a simple app to demonstrate the use of streamlit and ollama")
st.chat_message("Hello, welcome to my app! How can I help you today?")
