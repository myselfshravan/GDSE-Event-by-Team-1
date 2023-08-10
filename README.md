# EventName - Unleashing Creativity with OpenAI and Streamlit

## Setup Python Environment

```bash
py -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
```

### Check if Python is installed

```bash
python --version
```

## How to install Streamlit and OpenAI

```bash
pip install streamlit
pip install openai

```

#### [Streamlit Official Docs](https://docs.streamlit.io/library/api-reference/write-magic)

#### [Streamlit Cheat Sheet](https://cheatsheet.streamlit.app/)

#### [OpenAI API Reference for Text Completion](https://platform.openai.com/docs/api-reference/completions)

#### [OpenAI API Reference for Image Generation](https://platform.openai.com/docs/api-reference/completions)

## How to run

```bash
streamlit run app.py
```

---

#### [Source Code](https://github.com/myselfshravan/GDSE-Event-by-Team-1)

#### [Demo App](https://github.com/myselfshravan/GDSE-Event-by-Team-1)

#### [Some Public APIs](https://github.com/Postman-Student-Program/public-apis)

#### [Code for TextGen](https://github.com/githubhosting/Streamlit-Demo/blob/main/textgen.py)

#### [Claude API Docs](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)

#### [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python)

---

## API key Hiding

Create a file called `secrets.toml` under `.streamlit` folder and add the following lines

```toml
openai_api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
calude_api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

## Creating requirements.txt

[Reference](https://pip.pypa.io/en/stable/user_guide/#requirements-files)

```bash
py -m pip install -r requirements.txt
pip3 freeze >requirements.txt
```

#### [Deploy Here](https://share.streamlit.io/)
