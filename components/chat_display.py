"""
Chat display component for Streamlit UI
"""
import streamlit as st

def render_chat_messages(messages):
    """Render chat message history"""
    for message in messages:
        if message["role"] == "user":
            with st.chat_message("user", avatar="👤"):
                st.markdown(message["content"])
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(message["content"])