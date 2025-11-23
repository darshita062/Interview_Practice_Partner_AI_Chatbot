"""
Configuration management for Interview Practice Agent
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Application configuration"""
    
    # API Configuration
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    GEMINI_MODEL = 'gemini-2.5-flash'
    
    # Interview Configuration
    MAX_QUESTIONS = 6
    STAGES = ['introduction', 'interviewing', 'feedback']
    
    # UI Configuration
    APP_TITLE = "Interview Practice Partner"
    APP_SUBTITLE = "AI-Powered Mock Interview Assistant"
    
    
    # Validation
    JOB_KEYWORDS = [
        "engineer", "developer", "designer", "manager", "analyst",
        "sales", "marketing", "consultant", "accountant", "teacher",
        "nurse", "doctor", "lawyer", "architect", "scientist"
    ]
    
    @classmethod
    def validate(cls):
        """Validate required configuration"""
        if not cls.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        return True