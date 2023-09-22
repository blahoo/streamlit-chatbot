import streamlit as st

OPENAI_API_KEY = st.secrets["openai_key.api_key"] # used in order to deploy using streamlit and streamlit secrets

def getOpenAiKey():
    return OPENAI_API_KEY
