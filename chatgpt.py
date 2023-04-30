import os
import openai
import streamlit as st
element = st.empty()


def request_to_rev_openai(query):

    openai.api_key = ""
    prev_text = ""

    messages=[]
    # while True:
    user_content = query
    messages.append({"role" : "user", "content" : f"{user_content}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    assistant_content = completion.choices[0].message['content'].strip()
    messages.append({"role" : "assistant", "content" : f"{assistant_content}"})

    prev_text = assistant_content
    element.write(prev_text, unsafe_allow_html=True)