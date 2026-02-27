import streamlit as st

st.title("Janani AI - Personal Assistant")
st.write("Talk to AI Janani: ask about life, strengths, growth areas, mindset, and more.")

# Input box for user questions
question = st.text_input("Type your question here:")

# Placeholder response (no API key needed)
if question:
    st.write(f"AI Response: I received your question: '{question}'")