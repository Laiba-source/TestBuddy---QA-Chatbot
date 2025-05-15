import streamlit as st
from chatbot import get_answer

st.set_page_config(page_title="TestBuddy - QA Chatbot", layout="centered")
st.title("🧪 TestBuddy - Your QA Assistant")

user_input = st.text_input("Ask a question related to software testing:")

if user_input:
    st.write(f"Input received: {user_input}")  # Debug: confirm input
    answer = get_answer(user_input)
    st.write(f"Answer returned: {answer}")  # Debug: confirm output
    if answer:
        st.success(answer)
    else:
        st.error("Sorry, no answer found.")
