import logging
import random
import os
import openai

import streamlit as st
from streamlit.commands.page_config import RANDOM_EMOJIS
st.set_page_config(page_title="ChatGPT", page_icon=random.choice(RANDOM_EMOJIS), menu_items={})
st.title("ChatGPT with Dall-E")
st.sidebar.header("Chatting")
st.sidebar.info("Chat")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
element = st.empty()

import chatgpt
import dalle

openai.api_key = 'api_key'


def app_main():
    user_query = st.text_input("Enter").strip()
    if user_query is not None and user_query and user_query != "":
        with st.spinner(text="Waiting for response..."):
            response = chatgpt.request_to_rev_openai(user_query)
            st.text(response)
            image_url = dalle.getImage(user_query)
            st.image(image_url, width=256)

if __name__ == "__main__":
    app_main()