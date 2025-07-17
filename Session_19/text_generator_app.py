import streamlit as st
import openai
import os
import google.generativeai as genai

client = openai.OpenAI(
                #api_key = os.environ.get("OPENAI_API_KEY")
                api_key = "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"
                )


genai.configure(api_key="AIzaSyAJoYFwz7rFEMHKSr59uHtP6ikF4TOp5tU")

st.title("AI text Generator")
st.markdown("Generate text using Gemini or GPT")

prompt = st.text_area("Enter ypur prompt" , height=150)

#model selection
model_choice = st.radio("Choose a model:" , ("GPT (OpenAI)" , "Gemeini (Google)"))

'''
st.selectbox(
    "Choose a model:",
    ("GPT (OpenAI)" , "Gemeini (Google)")
)
'''

if st.button("Generate..."):
    if not prompt.strip():
        st.warning("Please enter a valid prompt!!")
    else:
        with st.spinner("Generating..."):
            try:
                if model_choice == "GPT (OpenAI)":
                    message = [
                        {"role" : "user", "content": prompt}
                    ]

                    response = client.responses.create(
                        model = "gpt-4.1-nano",
                        input = message,
                        temperature = 0.4
                    )
                    st.success("Response Generated using GPT-")
                    st.write(response.output_text)

                else:
                    model = genai.GenerativeModel('models/gemini-1.5-flash')
                    response = model.generate_content(prompt)
                    st.success("Response Generated using Gemini APi-")
                    st.write(response.text)
            except Exception as e:
                st.error(f"Error: {str(e)}")


