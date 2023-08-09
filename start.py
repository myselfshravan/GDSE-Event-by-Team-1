import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = ""

st.title("AI Text Gen 🤖")
st.subheader("Write the Prompt")
prompt = st.text_area("Prompt", "Enter the Text Here")

check = st.button("Ask the AI")
if check:
    st.subheader("OpenAI Davinci-3 AI")
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{prompt}",
        max_tokens=100,
        temperature=0
    )
    text = completion.choices[0].text
    st.write(text)
