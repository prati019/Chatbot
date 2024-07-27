import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load all the env variables
load_dotenv()

# GenAI config of API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel("gemini-pro")


# Define a function to generate a response from LLM
def get_gemini_response(ques):
    resp = model.generate_content(ques)
    return resp.text


# Setting up Streamlit app
st.set_page_config(
    page_title="Gemini Pro Q/A Project",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Setting up header
st.header("Gemini Q/A App")

# Input
question = st.text_input("Ask a question: ")

# Submit button
if st.button("Submit"):
    response = get_gemini_response(question)
    st.write("User:", question)
    st.write("Bot:", response)
