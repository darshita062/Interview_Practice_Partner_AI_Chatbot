"""
Session state management for Streamlit
"""
import streamlit as st
from agents.interview_agent import InterviewAgent

class StateManager:
    """Manages Streamlit session state"""
    
    @staticmethod
    def initialize():
        """Initialize session state variables"""
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        
        if 'agent' not in st.session_state:
            st.session_state.agent = None
        
        if 'interview_started' not in st.session_state:
            st.session_state.interview_started = False
    
    @staticmethod
    def start_interview():
        """Start a new interview session"""
        st.session_state.interview_started = True
        st.session_state.agent = InterviewAgent()
        
        # Send initial greeting
        greeting = st.session_state.agent.send_message("Hello, I'm ready to practice!")
        st.session_state.messages.append({
            "role": "assistant",
            "content": greeting
        })
    
    @staticmethod
    def reset_interview():
        """Reset interview session"""
        st.session_state.messages = []
        st.session_state.agent = None
        st.session_state.interview_started = False
    
    @staticmethod
    def add_message(role, content):
        """Add message to conversation"""
        st.session_state.messages.append({
            "role": role,
            "content": content
        })
    
    @staticmethod
    def get_agent():
        """Get current interview agent"""
        return st.session_state.agent
    
    @staticmethod
    def is_interview_started():
        """Check if interview has started"""
        return st.session_state.interview_started