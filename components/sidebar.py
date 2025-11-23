"""
Sidebar component for Streamlit UI
"""
import streamlit as st
from utils.state_manager import StateManager

def render_sidebar():
    """Render sidebar with instructions and controls"""
    with st.sidebar:
        st.header("Instructions")
        st.markdown("""
        **How it works:**
        1. Click "Start Interview"
        2. Tell me your target role
        3. Answer 5-6 interview questions
        4. Receive detailed feedback
        
        **Tips:**
        - Be authentic and natural
        - Take your time to think
        - Answer as in a real interview
        """)
        st.markdown("---")

        # Agent info
        if StateManager.is_interview_started():
            agent = StateManager.get_agent()
            
            st.subheader("Interview Status")
            st.write(f"**Stage:** {agent.stage.title()}")
            if agent.role:
                st.write(f"**Role:** {agent.role}")
            if agent.stage == "interviewing":
                st.write(f"**Questions:** {agent.questions_asked}/6")
        st.markdown("---")
        st.markdown("**Made by Darshita Dixit**")
        
        # Reset button
        if StateManager.is_interview_started():
            if st.button("Reset Interview", use_container_width=True):
                StateManager.reset_interview()
                st.rerun()