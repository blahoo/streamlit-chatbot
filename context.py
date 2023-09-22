import openai
from key import getOpenAiKey
import streamlit as st

st.cache_data.clear()
if "list_context" not in st.session_state:
    st.session_state["list_context"] = []
max_context_length = st.secrets["max_context"]

openai.api_key = getOpenAiKey()

st.session_state.list_context.append({"role": "assistant", "content": "Hello World 👋"})

def add(role, message):
    st.session_state.list_context.append({"role": role, "content": message})
    if len(st.session_state.list_context) > max_context_length:
        st.session_state.list_context.pop(0)

def get():
    return st.session_state.list_context
