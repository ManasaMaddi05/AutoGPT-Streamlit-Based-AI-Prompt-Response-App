import os
from apikey import apikey
import google.generativeai as genai
import streamlit as st


os.environ["GEMINI_API_KEY"] = apikey
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

st.title('AutoGPT')
prompt = st.text_input('Plug in your prompt here')
model = genai.GenerativeModel("gemini-2.0-flash")

if prompt:
    response = model.generate_content(prompt)
    st.write(response.text)