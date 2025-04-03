import streamlit as st
import requests
import json

# Set up Streamlit app
st.title("Gemini AI Chatbot")
st.write("Chat with Gemini AI using Google's Generative Language API!")

# Input API Key
api_key = st.text_input("Enter your Gemini API Key:", type="password")

# User input for chatbot
user_input = st.text_area("You:")

# API call function
def get_gemini_response(api_key, user_text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": user_text}]}]}
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        result = response.json()
        try:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        except KeyError:
            return "Error: Unexpected response format."
    else:
        return f"Error: {response.status_code} - {response.text}"

# Display response
if st.button("Send") and user_input and api_key:
    response = get_gemini_response(api_key, user_input)
    st.write("**Gemini AI:**", response)
