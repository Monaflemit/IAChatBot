# cd C:\Users\quewa\Documents\pyzo\Mistral
import streamlit as st # streamlit run Mistral.py
import requests
import json

API_URL = "https://api.mistral.ai/v1/chat/completions"
API_KEY = "3CKymu8LjZ8BQZmkq3NRZRrQTyiTRJxP"


headers = {
    "Authorization": f"Bearer {API_KEY}",
}

def chat_with_mistral(message):
    data = {
        "model": "mistral-small",
        "messages": [
            {"role": "user", "content": message}
        ]
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    response_json = response.json()

    return response_json["choices"][0]["message"]["content"]

st.title("AI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    st.markdown(message["content"])

string = st.text_input("Poser votre question")

if string!="" and st.button("Valider"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": string})
    
    st.markdown(string)
    
    reponse = chat_with_mistral(string)
    
    # Add chatbot response to chat history
    st.session_state.messages.append({"role": "chatbot", "content": reponse})
    
    st.markdown(reponse)
    
    
