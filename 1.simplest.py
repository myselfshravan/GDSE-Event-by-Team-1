import streamlit as st
import openai

openai.api_key = "sk-xxx"

st.title("AI Text Gen 🤖")
prompt = st.text_area("Prompt", "Enter your text here...")

if st.button("Generate"):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0
    )
    st.write(response.choices[0].text)
