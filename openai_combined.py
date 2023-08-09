import streamlit as st
import openai

openai.api_key = st.secrets["openai_api_key"]

complete_list = openai.Model.list()
model_list = [model["id"] for model in complete_list["data"]]
model_list.sort()
st.write(model_list)


def generate(prompt, engine):
    if engine == "text":
        completion = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{prompt}",
            max_tokens=100,
            temperature=0
        )
        response = completion.choices[0].text
    elif engine == "image":
        completion = openai.Image.create(
            prompt=f"{prompt}",
            n=1,
            size="512x512"
        )
        response = completion.data[0].url
