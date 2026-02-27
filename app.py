# app.py
import streamlit as st
import openai

# ---------------------------
# STEP 1: Put your OpenAI API key here
# ---------------------------
openai.api_key ="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"

# ---------------------------
# Streamlit page setup
# ---------------------------
st.set_page_config(page_title="Janani AI Voice Assistant", page_icon="🤖")
st.title("Janani AI - Personal Voice Assistant")
st.write("Ask Janani anything about life, strengths, growth areas, mindset, and more!")

# ---------------------------
# User input
# ---------------------------
user_input = st.text_input("Type your question here:")

# ---------------------------
# Function to get AI response
# ---------------------------
def get_ai_response(question):
    try:
        # ---------------------------
        # Updated OpenAI Chat API call
        # ---------------------------
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Janani AI, a friendly and helpful personal voice assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=150,
            temperature=0.7
        )
        answer = response.choices[0].message.content
        return answer
    except Exception as e:
        return f"Error: {str(e)}"

# ---------------------------
# Display AI response
# ---------------------------
if user_input:
    ai_response = get_ai_response(user_input)
    st.markdown(f"**AI Response:** {ai_response}")