import streamlit as st
import requests
import json


st.title("Chat with LLama 3 (An offline AI app)")

user_prompt = st.text_area("Enter ypur prompt" , height=150)

#Function to get response from llama
def ask_llama(prompt , model = 'llama3.1:8b' , host = 'http://127.0.0.1:11434/'):
    response = requests.post(
        f"{host}/api/generate",
        json = {"model" : model , "prompt" : prompt}
    )

    full_response = ""
    for line in response.iter_lines():
        data = json.loads(line.decode("utf-8"))
        full_response += data["response"]

    return full_response.strip()
    
if st.button("Generate..."):
    if user_prompt:
        llama_response = ask_llama(user_prompt)
        st.markdown(llama_response)