import logging
import random
import os
import openai

import streamlit as st
from revChatGPT.V3 import Chatbot
from streamlit.commands.page_config import RANDOM_EMOJIS

st.set_page_config(page_title="Raynor ChatGPT", page_icon=random.choice(RANDOM_EMOJIS), menu_items={})
st.title("Demo ChatGPT with Streamlit")
st.sidebar.header("Chatting")
st.sidebar.info("Chat")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
openai.api_key = 'api_key'

def request_to_rev_openai(query):
    chatbot = Chatbot(api_key="api_key")
    prev_text = ""
    for data in chatbot.ask_stream(prompt=query):
        if isinstance(data, dict):
            prev_text = data["message"]
    if not prev_text:
        prev_text = "No answer from Raynor ChatGPT"
    return prev_text

def getImage(text):
    response = openai.Image.create(
        prompt=text,
        n=1,
        size="256x256"
    )
    return response["data"][0]["url"]

def app_main():
    user_query = st.text_input("Enter").strip()
    if user_query is not None and user_query and user_query != "":
        with st.spinner(text="Waiting for response..."):
            response = request_to_rev_openai(user_query)
            st.text(response)
            image_url = getImage(user_query)
            st.image(image_url, width=256)

if __name__ == "__main__":
    app_main()
