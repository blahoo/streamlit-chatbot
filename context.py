import openai
from key import getOpenAiKey
import streamlit as st

print("---- setup initialized -----")

if "list_context" not in st.session_state:
    st.session_state["list_context"] = []
    st.session_state.list_context.append({"role": "assistant", "content": "Hello World 👋"})

max_context_length = st.secrets["max_context"]

openai.api_key = getOpenAiKey()


def add(role, message):
    st.session_state.list_context.append({"role": role, "content": message})
    if len(st.session_state.list_context) > max_context_length:
        st.session_state.list_context.pop(0)

def get():
    return st.session_state.list_context

def reset():
    st.session_state.list_context = []
    st.session_state.list_context.append({"role": "assistant", "content": "Hello World 👋"})

print("----- setup complete -----")
