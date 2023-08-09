import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = ""

# Streamlit website title and icon
st.set_page_config(page_title="OpenAI Text Gen", page_icon="🤖")

# Streamlit App Title and Prompt Input
st.title("AI Text Generation 🤖")
prompt = st.text_area("Enter Prompt", "Type your text here...")

# "Ask" Button for AI Generation
ask_button = st.button("Generate Text")

# Generate and Display AI Response
if ask_button:
    st.subheader("AI Response:")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.2
    )
    generated_text = response.choices[0].text
    st.write(generated_text)
