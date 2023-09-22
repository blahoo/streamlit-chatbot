import openai
from key import getOpenAiKey
import streamlit as st

st.cache_data.clear()
list_context = []
max_context_length = st.secrets["max_context"]

openai.api_key = getOpenAiKey()

list_context.append({"role": "assistant", "content": "Hello World 👋"})

def add(role, message):
    list_context.append({"role": role, "content": message})
    if len(list_context) > max_context_length:
        list_context.pop(0)

def get():
    return list_context
