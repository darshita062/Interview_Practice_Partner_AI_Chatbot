"""
Header component for Streamlit UI
"""
import streamlit as st
from config import Config

def render_header():
    """Render application header"""
    st.title(Config.APP_TITLE)
    st.markdown(f"### {Config.APP_SUBTITLE}")
    st.markdown("---")