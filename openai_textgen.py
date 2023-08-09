import streamlit as st
import openai

st.set_page_config(page_title="OpenAI GPT", page_icon="🤖")

openai.api_key = st.secrets["openai_api_key"]

st.title("AI Text Gen 🤖")
st.subheader("Write the Prompt")
prompt = st.text_area("Prompt", "Enter the Text Here")

ask_button = st.button("Ask the AI")
if ask_button:
    st.subheader("OpenAI Davinci-3 AI")
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{prompt}",
        max_tokens=100,
        temperature=0
    )
    text = completion.choices[0].text
    st.write(text)
