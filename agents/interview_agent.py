"""
Main interview agent logic
"""
import google.generativeai as genai
from config import Config
from agents.prompt_manager import PromptManager

class InterviewAgent:
    """AI-powered interview practice agent"""
    
    def __init__(self):
        """Initialize the interview agent"""
        # Validate configuration
        Config.validate()
        
        # Configure Gemini API
        genai.configure(api_key=Config.GEMINI_API_KEY)
        
        # Initialize model and chat
        self.model = genai.GenerativeModel(Config.GEMINI_MODEL)
        self.chat = self.model.start_chat(history=[])
        
        # Initialize state
        self.role = None
        self.questions_asked = 0
        self.stage = "introduction"
        self.conversation_log = []
        self.prompt_manager = PromptManager()
    
    def get_current_prompt(self):
        """Get prompt based on current stage"""
        if self.stage == "introduction":
            return self.prompt_manager.get_introduction_prompt()
        
        elif self.stage == "interviewing":
            return self.prompt_manager.get_interviewing_prompt(
                self.role,
                self.questions_asked + 1,
                Config.MAX_QUESTIONS
            )
        
        elif self.stage == "feedback":
            return self.prompt_manager.get_feedback_prompt()
    
    def send_message(self, user_input):
        """Send message to agent and get response"""
        # Log user message
        self.conversation_log.append({
            "role": "user",
            "content": user_input,
            "stage": self.stage
        })
        
        # Prepare contextualized message
        system_context = self.get_current_prompt()
        full_message = f"{system_context}\n\nCandidate's response: {user_input}"
        
        try:
            # Send to Gemini
            response = self.chat.send_message(full_message)
            bot_response = response.text
            
            # Log bot response
            self.conversation_log.append({
                "role": "assistant",
                "content": bot_response,
                "stage": self.stage
            })
            
            # Update state
            self.update_state(user_input, bot_response)
            
            return bot_response
            
        except Exception as e:
            error_msg = f"Sorry, I encountered an error: {str(e)}"
            return error_msg
    
    def update_state(self, user_msg, bot_response):
        """Update conversation state"""
        # Detect role from introduction
        if self.stage == "introduction" and not self.role:
            user_lower = user_msg.lower()
            if any(keyword in user_lower for keyword in Config.JOB_KEYWORDS):
                self.role = user_msg.strip()
                self.stage = "interviewing"
        
        # Track questions during interview
        elif self.stage == "interviewing":
            if "?" in bot_response:
                self.questions_asked += 1
            
            # Transition to feedback
            if self.questions_asked >= Config.MAX_QUESTIONS or "feedback" in bot_response.lower():
                self.stage = "feedback"
    
    def get_progress(self):
        """Get interview progress as percentage"""
        if self.stage == "interviewing":
            return self.questions_asked / Config.MAX_QUESTIONS
        return 0.0
    
    def is_complete(self):
        """Check if interview is complete"""
        return self.stage == "feedback" and len(self.conversation_log) > 12