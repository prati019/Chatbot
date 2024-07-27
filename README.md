# Gemini Q/A Chatbot

A simple Q/A chatbot using Gemini Pro LLM and Streamlit.

## Overview

This project is a Q/A chatbot built with Streamlit, leveraging the Gemini Pro API for generating responses. Users can input questions, and the chatbot will provide answers using the Gemini Pro language model.

## Installation

### Prerequisites

- Python 3.9 or higher
- anaconada

###Project link
https://github.com/prati019/Chatbot

### Steps

1. **Create a Virtual Environment**
    python -m venv myenv    

2. **Install the Required Dependencies(libraries)**
    pip install -r requirements.txt


3. **Set Up Your API Key**
    - Create a `.env` file in the project directory and add your Gemini Pro API key:
        ```
        GEMINI_API_KEY=your_gemini_pro_api_key_here
        ```
4.  **Create the file app.py and write the code for the structure**


## Usage

1. **Run the Streamlit App**
    streamlit run app.py
    

2. **Open the App in Your Browser**
    - Navigate to `http://localhost:8501` to interact with the chatbot.

## File Structure
.env # Environment variables file (API keys, etc.)
app.py # Main Streamlit app script
requirements.txt # Python dependencies
README.md # Project documentation

