import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = ""

# Webpage title and icon
st.set_page_config(page_title="OpenAI Text Gen", page_icon="🤖")

# Streamlit App Title and Prompt Input
st.title("AI Text Generation 🤖")

prompt = st.text_area("Prompt")  # Input for Prompt

# "Ask" Button for AI Generation
ask_button = st.button("Generate Text")

# Generate and Display AI Response
if ask_button:
    st.subheader("AI Response:")
    response = openai.Completion.create(
        model="text-davinci-003",  # Model to use
        prompt=prompt,
        max_tokens=100,  # Max length of the response
        temperature=0.2  # Controls randomness of the response (0 to 2)
    )
    generated_text = response.choices[0].text
    st.write(generated_text)
