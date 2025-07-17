import streamlit as st

st.title("AI text Generator")
st.markdown("Generate text using Gemini or GPT")

prompt = st.text_area("Enter ypur prompt" , height=150)

#model selection
st.radio("Choose a model:" , ("GPT (OpenAI)" , "Gemeini (Google)"))

st.selectbox(
    "Choose a model:",
    ("GPT (OpenAI)" , "Gemeini (Google)")
)

st.button("Generate...")