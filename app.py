import logging
import random

import streamlit as st
from revChatGPT.V3 import Chatbot
from streamlit.commands.page_config import RANDOM_EMOJIS

st.set_page_config(page_title="Raynor ChatGPT", page_icon=random.choice(RANDOM_EMOJIS), menu_items={})
st.title("Demo ChatGPT with Streamlit")
st.sidebar.header("Chatting")
st.sidebar.info("Chat")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# https://chat.openai.com/api/auth/session
def request_to_rev_openai(query):
    chatbot = Chatbot(api_key="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")
    prev_text = ""
    for data in chatbot.ask_stream(prompt=query):
        if isinstance(data, dict):
            prev_text = data["message"]
    if not prev_text:
        prev_text = "No answer from Raynor ChatGPT"
    return prev_text


def app_main():
    user_query = st.text_input("Enter").strip()
    if user_query is not None and user_query and user_query != "":
        with st.spinner(text="Waiting for response..."):
            response = request_to_rev_openai(user_query)
        st.text(response)


if __name__ == "__main__":
    app_main()
