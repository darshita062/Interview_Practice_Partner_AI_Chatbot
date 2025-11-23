"""
Streamlit UI for Interview Practice Agent
Main entry point for web interface
"""
import streamlit as st
from config import Config
from utils.state_manager import StateManager
from components.header import render_header
from components.sidebar import render_sidebar
from components.chat_display import render_chat_messages

# Configure page
st.set_page_config(
    page_title=Config.APP_TITLE,
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stAppDeployButton{
         display: none;   
    }
    .stMainMenu {
        display: none;        
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 2rem;
        border: none;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    """Main application logic"""
    
    # Initialize session state
    StateManager.initialize()
    
    # Initialize voice handler in session state (for input only)
    if 'voice_handler' not in st.session_state:
        try:
            from utils.voice_handler import VoiceHandler
            st.session_state.voice_handler = VoiceHandler()
            st.session_state.voice_available = True
        except Exception as e:
            st.session_state.voice_available = False
            print(f"Voice input not available: {e}")
    
    # Initialize pending voice input
    if 'pending_voice_input' not in st.session_state:
        st.session_state.pending_voice_input = None
    
    # Render header
    render_header()
    
    # Render sidebar
    render_sidebar()
    
    # Check API key
    try:
        Config.validate()
    except ValueError as e:
        st.error(f"{str(e)}")
        st.info("Please add GEMINI_API_KEY to your .env file")
        st.stop()
    
    # Start interview section
    if not StateManager.is_interview_started():
        st.info("Welcome! Click below to start your interview practice session.")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Start Interview", use_container_width=True):
                StateManager.start_interview()
                st.rerun()
    
    # Interview in progress
    else:
        agent = StateManager.get_agent()
        
        # Show progress bar
        if agent.stage == "interviewing":
            progress = agent.get_progress()
            st.progress(progress, text=f"Progress: {agent.questions_asked}/{Config.MAX_QUESTIONS} questions")
        
        # Display chat history
        render_chat_messages(st.session_state.messages)
        
        # Voice input controls (only if available)
        if st.session_state.voice_available:
            st.markdown("---")
            
            # Voice input instructions
            with st.expander("Voice Input Guide", expanded=False):
                st.markdown("""
                **How to use voice input:**
                1. Click the **Speak** button below
                2. Wait for "Listening..." message
                3. **Speak your full answer** - take your time!
                4. **Pause for 1.5 seconds** when done
                5. Your speech will be converted to text automatically
                
                **Tips for best results:**
                - Speak clearly at a normal pace
                - Minimize background noise
                - Take natural pauses between sentences
                - No need to rush - it captures long responses!
                
                **Note:** You can also type your response in the text box below.
                """)
            
            # Voice input button
            col1, col2, col3 = st.columns([2, 1, 2])
            with col2:
                if st.button("Speak", use_container_width=True, key="voice_input_btn", type="primary"):
                    with st.spinner("Listening... Speak now! (Pause 1.5s when done)"):
                        try:
                            text = st.session_state.voice_handler.listen(
                                timeout=10, 
                                phrase_time_limit=None
                            )
                            
                            if text:
                                st.session_state.pending_voice_input = text
                                preview = text[:150] + '...' if len(text) > 150 else text
                                st.success(f"Heard ({len(text)} characters): {preview}")
                                st.rerun()
                            else:
                                st.error("Could not understand. Please try again or type your response below.")
                        except Exception as e:
                            st.error(f"Microphone error: {str(e)}")
                            st.info("Make sure your microphone is connected and working.")
        
        # Process pending voice input
        prompt = None
        if st.session_state.pending_voice_input:
            prompt = st.session_state.pending_voice_input
            st.session_state.pending_voice_input = None
        
        # Chat input (text)
        if not prompt:
            prompt = st.chat_input("Type your response here...")
        
        # Process input (voice or text)
        if prompt:
            # Display user message
            StateManager.add_message("user", prompt)
            with st.chat_message("user", avatar="👤"):
                st.markdown(prompt)
            
            # Get bot response
            with st.chat_message("assistant", avatar="🤖"):
                with st.spinner("Thinking..."):
                    response = agent.send_message(prompt)
                    st.markdown(response)
            
            # Save message to history
            StateManager.add_message("assistant", response)
            
            # Check if complete
            if agent.is_complete():
                st.balloons()
                st.success("Interview practice complete! Great job!")
                
                st.markdown("---")
            
            # Rerun to update UI
            st.rerun()

if __name__ == "__main__":
    main()