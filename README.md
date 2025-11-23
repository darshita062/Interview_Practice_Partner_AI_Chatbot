# 🎤 Interview Practice Partner

An AI-powered conversational agent that helps users practice for job interviews through realistic mock interviews, voice input, and detailed feedback.

## 📝 Overview

This project is an intelligent interview practice assistant that:
- Conducts role-specific mock interviews with natural conversation flow
- Asks relevant follow-up questions based on user responses
- Provides constructive feedback on communication, answer quality, and areas for improvement
- Supports voice input for realistic interview practice
- Features both command-line and web-based interfaces
- Works with multiple job roles (engineering, sales, marketing, data science, etc.)

## ✨ Features

- **Natural Conversations**: Engages in realistic interview dialogue with contextual awareness
- **Intelligent Question Generation**: Asks technical, behavioral, and situational questions tailored to your role
- **Adaptive Follow-ups**: Dynamically generates relevant follow-up questions based on your answers
- **Detailed Feedback**: Provides quantitative scores (1-10) and actionable improvement suggestions
- **Voice Input Support**: Answer questions using your voice for a more natural interview experience
- **Progress Tracking**: Visual progress bar showing interview completion (6 questions)
- **Transcript Download**: Save complete interview transcripts for review
- **Dual Interface**: Command-line tool for developers, web UI for general users

## 🏗️ Architecture
```
User Input → Interview Agent → Google Gemini API → Response Generation
                ↓
         State Management
    (introduction → interviewing → feedback)
```

### **System Components:**

1. **InterviewAgent Class** (`agents/interview_agent.py`)
   - Manages conversation state and flow
   - Tracks question count and interview stage
   - Generates context-aware responses

2. **Prompt Manager** (`agents/prompt_manager.py`)
   - Dynamic prompt engineering based on interview stage
   - Role-specific question generation
   - Structured feedback templates

3. **State Manager** (`utils/state_manager.py`)
   - Streamlit session state management
   - Message history tracking
   - Agent lifecycle control

4. **Voice Handler** (`utils/voice_handler.py`)
   - Speech-to-text conversion using Google Speech Recognition
   - Supports unlimited response length
   - Intelligent pause detection (1.5 seconds)

5. **UI Components** (`components/`)
   - Modular Streamlit components
   - Header, sidebar, and chat display
   - Reusable across different views

## 🛠️ Technologies Used

- **Python 3.10+**
- **Google Gemini 2.5 Flash API** - Natural language understanding and generation
- **Streamlit** - Web interface framework
- **SpeechRecognition** - Voice input processing
- **PyAudio** - Audio capture
- **python-dotenv** - Environment variable management

## 📁 Project Structure
```
interview-practice-agent/
├── app.py                      # Streamlit web interface
├── cli.py                      # Command-line interface
├── config.py                   # Configuration management
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
├── .env                        # Environment variables (not in repo)
├── .gitignore                  # Git ignore rules
│
├── agents/                     # AI Agent logic
│   ├── __init__.py
│   ├── interview_agent.py      # Main agent class
│   └── prompt_manager.py       # Prompt engineering
│
├── components/                 # UI components
│   ├── __init__.py
│   ├── header.py               # App header
│   ├── sidebar.py              # Sidebar with controls
│   └── chat_display.py         # Message display
│
└── utils/                      # Utility functions
    ├── __init__.py
    ├── state_manager.py        # Session state management
    └── voice_handler.py        # Voice input processing
```

This modular structure ensures:
- **Separation of concerns** for better maintainability
- **Reusable components** across different interfaces
- **Easy testing** of individual modules
- **Scalable architecture** for future enhancements

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- Microphone (for voice input feature)
- Google Gemini API key (free, no credit card required)

### Setup Instructions

**1. Clone the repository**
```bash
git clone https://github.com/darshita062/Interview_Practice_Partner_AI_Chatbot.git
cd interview-practice-agent
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**Note:** If `pyaudio` installation fails:

**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**Mac:**
```bash
brew install portaudio
pip install pyaudio
```

**Linux:**
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
```

**3. Get a free Gemini API key**
- Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
- Sign in with your Google account
- Click "Create API Key"
- Copy your API key

**4. Configure environment**
- Create a `.env` file in the project root
- Add your API key:
```env
GEMINI_API_KEY=your_api_key_here
```

**5. Run the application**

**Web Interface (Recommended):**
```bash
python -m streamlit run app.py
```
Opens at http://localhost:8501

**Command Line Interface:**
```bash
python cli.py
```

## 🎯 Usage

### Web Interface

1. **Start the app**: `python -m streamlit run app.py`
2. Click **"🚀 Start Interview"**
3. Tell the agent your target role
4. Answer questions using:
   - **Text input**: Type in the chat box
   - **Voice input**: Click 🎤 Speak button
5. Receive detailed feedback after 6 questions
6. Download transcript (optional)

### Command Line Interface

1. **Start the app**: `python cli.py`
2. Type your target role when prompted
3. Answer interview questions by typing
4. Get comprehensive feedback
5. Save transcript when offered

### Example Interaction
```
🤖 Interviewer: Hi! I'm excited to help you practice. What position are you preparing for?

👤 You: Software Engineer at Amazon

🤖 Interviewer: Great! Let's begin. Can you explain the difference between a stack and a queue, and provide real-world use cases for each?

👤 You: A stack follows LIFO (Last In, First Out) principle, like a stack of plates. 
It's commonly used in function call management and undo mechanisms. A queue follows 
FIFO (First In, First Out), like a line at a store. It's used in task scheduling 
and breadth-first search algorithms.

🤖 Interviewer: Excellent explanation! Can you describe a scenario where you had to 
optimize an algorithm's time complexity in a project?

[... continues for 5-6 questions ...]

🤖 Interviewer: Great! Let's wrap up with feedback on your performance.

**Communication Skills: 9/10**
You articulated your thoughts clearly and maintained a professional tone throughout...

**Answer Quality: 8/10**
Your responses were comprehensive with good examples. To improve, quantify your 
achievements when discussing past projects...

**Technical Knowledge: 9/10**
Strong understanding of data structures and algorithms...

**Areas for Improvement:**
1. Use the STAR method more consistently for behavioral questions
2. Provide specific metrics when discussing project impact
3. Take a brief pause before answering complex questions

**Strengths:**
✓ Excellent technical explanations with practical examples
✓ Confident and clear communication
✓ Good understanding of real-world applications
✓ Professional demeanor throughout

Keep practicing, and you'll do great in your real interview! 🎉
```

## 🎤 Voice Features

### Voice Input
The application supports voice input for a more natural interview experience:

**Features:**
- Click the **🎤 Speak** button to answer questions using your voice
- Speak naturally with pauses - the system captures long, detailed responses
- Automatically converts speech to text using Google Speech Recognition
- Supports unlimited response length with intelligent pause detection (1.5 seconds)
- Works alongside text input - use whichever you prefer

**Usage Tips:**
- Speak clearly at a normal pace
- Minimize background noise for best results
- Take natural pauses between sentences
- The system waits 1.5 seconds of silence before finalizing your response
- You'll see a preview of what was captured before it's sent

**Requirements:**
```bash
pip install SpeechRecognition pyaudio
```

**Note:** Microphone access is required. Grant permission when prompted by your browser/system.

## 🎨 Design Decisions

### 1. Three-Stage State Machine
Implemented a stage-based system (introduction → interviewing → feedback) rather than free-flowing conversation to ensure:
- Structured interview progression
- Appropriate prompts for each phase
- Natural conversation within defined boundaries
- Reliable state transitions

### 2. Dynamic Prompt Engineering
Instead of one generic prompt, the system generates context-aware prompts that include:
- Current interview stage
- Question number (e.g., "Question 3 of 6")
- Target role information
- Previous conversation context

This approach ensures relevant questions and maintains conversation coherence.

### 3. Google Gemini 2.5 Flash Selection
Chose Gemini for several reasons:
- **Free tier** with no credit card requirement
- **Strong conversational capabilities** for natural dialogue
- **Fast response times** (2.5 Flash model)
- **Generous rate limits** for development and testing
- **High-quality output** suitable for interview scenarios

### 4. Modular Architecture
Separated concerns into distinct modules:
- **Agents**: Core AI logic independent of UI
- **Components**: Reusable UI elements
- **Utils**: Shared functionality (state, voice)
- **Config**: Centralized configuration

Benefits:
- Easy to test individual components
- Can swap UI frameworks without changing agent logic
- Clear code organization for maintainability
- Enables future features (e.g., mobile app using same agent)

### 5. Conversation Logging & Transcript Generation
Every interaction is logged to enable:
- Complete transcript download
- State debugging
- Future analytics (e.g., common weak areas)
- Session review for improvement

### 6. Error Handling Strategy
Robust error handling at multiple levels:
- API failures: User-friendly messages
- Voice recognition errors: Fallback to text input
- Unexpected inputs: Graceful recovery
- Network issues: Clear error communication

### 7. Voice Input Design
Unlimited phrase length with pause detection rather than fixed time limits:
- Allows detailed, thoughtful responses
- More natural than strict time constraints
- 1.5-second pause threshold feels natural
- Shows character count and preview for transparency

## 🚀 Future Improvements

Potential enhancements for future versions:

- [ ] **Voice Output**: Text-to-speech for bot responses (audio output challenges on web)
- [ ] **Industry-Specific Question Banks**: Curated questions for different fields
- [ ] **Multi-Session Tracking**: Progress tracking across multiple practice sessions
- [ ] **Performance Analytics**: Detailed metrics on improvement over time
- [ ] **Video Interview Mode**: Facial expression and body language feedback
- [ ] **Multiple Languages**: Support for non-English interviews
- [ ] **Interview Recording**: Save audio/video for self-review
- [ ] **Role-Playing Modes**: Different interviewer personalities (friendly, challenging, etc.)
- [ ] **Company-Specific Prep**: Tailored questions based on target company
- [ ] **Peer Practice**: Match users for peer-to-peer interview practice
- [ ] **Mobile App**: Native iOS/Android applications
- [ ] **Integration with Resume**: Parse resume to ask relevant questions
- [ ] **Calendar Integration**: Schedule practice sessions with reminders

## 📹 Demo Video

[Link to your demo video will go here]

## 🧪 Testing

The application has been tested with various user scenarios:

### Test Scenarios
1. **The Confused User**: Vague responses like "I don't know" or "Maybe marketing?"
   - Agent asks clarifying questions
   - Helps user focus their preparation

2. **The Efficient User**: Clear, concise responses
   - Agent maintains conversation flow
   - Provides targeted questions

3. **The Detailed Responder**: Long, comprehensive answers
   - Voice input captures full responses
   - Agent asks relevant follow-ups

4. **Edge Cases**:
   - Off-topic responses → Gently redirects
   - Very short answers → Prompts for elaboration
   - Invalid inputs → Handles gracefully
   - API timeouts → Clear error messages

### Voice Input Testing
- Tested with various accents and speech patterns
- Background noise handling
- Long responses (60+ seconds)
- Natural pauses vs. hesitation detection

## 🔒 Privacy & Data Handling

- API keys stored in environment variables (not in code)
- Conversations not saved unless user explicitly downloads transcript
- All communication directly with Google's API (no intermediary storage)
- No user authentication or data collection
- For production use, consider adding:
  - Encryption at rest and in transit
  - User data deletion options
  - Privacy policy and terms of service

## ⚙️ Configuration

### Environment Variables (.env)
```env
GEMINI_API_KEY=your_api_key_here
```

### Configuration Options (config.py)
```python
MAX_QUESTIONS = 6              # Number of interview questions
GEMINI_MODEL = 'gemini-2.5-flash'  # AI model
VOICE_PAUSE_THRESHOLD = 1.5    # Seconds of silence before finalizing speech
```

## 🐛 Troubleshooting

### Common Issues

**"API Key not found"**
- Ensure `.env` file exists in project root
- Check API key is correctly formatted
- Verify no extra spaces around `=` in `.env`

**Voice input not working**
- Check microphone permissions
- Test microphone with: `python test_mic.py` (if provided)
- Try running as administrator/sudo
- Reinstall pyaudio: `pip uninstall pyaudio && pip install pyaudio`

**"Could not understand audio"**
- Speak more clearly
- Reduce background noise
- Check microphone is default input device
- Try speaking closer to microphone

**App won't start**
- Check Python version: `python --version` (need 3.10+)
- Reinstall dependencies: `pip install -r requirements.txt`
- Check for port conflicts (Streamlit uses 8501)

## 📚 Additional Resources

- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [Streamlit Documentation](https://docs.streamlit.io)
- [SpeechRecognition Library](https://github.com/Uberi/speech_recognition)
- [Interview Preparation Tips](https://www.indeed.com/career-advice/interviewing/interview-preparation-tips)

