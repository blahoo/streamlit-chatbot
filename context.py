import openai
from key import getOpenAiKey

list_context = []

openai.api_key = getOpenAiKey()

list_context.append({"role": "assistant", "content": "👋"})

def add(role, message):
    list_context.append({"role": role, "content": message})

def get():
    return list_context