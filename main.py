import streamlit as st
import openai
import context

# prompt method
def chatgpt(prompt):

    # adds the prompt to a conversation history list for context
    context.add("user", (context.pre_prompt + prompt))
    
    # outputs the input to the chat display
    with st.chat_message("user"):
        st.markdown(prompt)

    # prompts chatgpt
    with st.chat_message("assistant"):
        message = st.empty()
        full_response = ""

        # call request to chatgpt
        for response in openai.ChatCompletion.create(

            # choose the model you wish to work with, in this case, the classic chatgpt - gpt 3.5
            model = "gpt-3.5-turbo",
            messages = context.get(),
            max_tokens = 100,

            # stream creates a python generator which outputs a response word by word
            stream = True
            ):
            
            # interacts with the generator response in order to append each new word to the final response
            msg_chunk = response["choices"][0].get("delta", {}).get("content")
            if msg_chunk is not None:
                full_response += msg_chunk

                # outputs the response word by word
                message.markdown(full_response + "")

        # finaly outputs the full response
        message.markdown(full_response)

    # appends the final response to the chat history
    context.add("assistant", full_response)

    print(context.get())

    return full_response

# initialize session state
if "list_context" not in st.session_state:
    print("---- session initialized -----")
    st.session_state["list_context"] = []
    st.session_state.list_context.append({"role": "assistant", "content": "Hello World 👋"})


# st.title("Streamlit-Chatbot") but fancy
new_title = """
<style>
.title {
    font-size: 45px !important;
    font-family: sans-serif;
    font-weight: 600;
    text-align: center;
    color: #fef8ef;
    background-image: linear-gradient(to left, #ff6c6c, #f0a830);
}
</style>
<p class="title">Streamlit-Chatbot</p>
"""
st.markdown(new_title, unsafe_allow_html=True)


for message in context.get():
    print(message)

    role = message["role"]
    content = message["content"]

    if role == "user":
        content = content[context.pre_prompt_len:]
    
    with st.chat_message(message["role"]):    
        st.markdown(content)


if prompt := st.chat_input("Input prompt, or \"reset\""):
    if prompt == "reset":
        context.reset()
        st.experimental_rerun()
    else:
        chatgpt(prompt)
