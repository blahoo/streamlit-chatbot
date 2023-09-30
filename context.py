import openai
from key import getOpenAiKey
import streamlit as st

# optional pre prompt to shorten response size
pre_prompt = "limit response to 100 words: "
pre_prompt_len = len(pre_prompt)

max_context_length = st.secrets["max_context"]

openai.api_key = getOpenAiKey()


def add(role, message):
    st.session_state.list_context.append({"role": role, "content": message})
    if len(st.session_state.list_context) > max_context_length:
        st.session_state.list_context.pop(0)

def get():
    return st.session_state.list_context

def reset():
    print("---- context reset -----")

    st.session_state.list_context = []
    st.session_state.list_context.append({"role": "assistant", "content": "Hello World 👋"})
