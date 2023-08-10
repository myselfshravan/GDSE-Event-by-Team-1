import streamlit as st
import openai

openai.api_key = st.secrets["openai_api_key"]

st.title("AI Text Gen 🤖")
prompt = st.text_area("Prompt", "")
#
if st.button("Generate"):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.9
    )
    st.write(response.choices[0].text)
