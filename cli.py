"""
Command-line interface for Interview Practice Agent
"""
from config import Config
from agents.interview_agent import InterviewAgent

def print_welcome():
    """Print welcome message"""
    print("\n" + "=" * 70)
    print(" " * 20 + Config.APP_TITLE)
    print("=" * 70)
    print("\nWelcome! I'm here to help you practice for your job interview.")
    print("\nHow it works:")
    print("  1. Tell me what role you're preparing for")
    print("  2. I'll ask you 5-6 interview questions")
    print("  3. Answer naturally, as you would in a real interview")
    print("  4. I'll provide detailed feedback at the end")
    print("\nTips:")
    print("  • Type 'quit' or 'exit' anytime to end the session")
    print("  • Be honest and authentic in your responses")
    print("  • Take your time to think before answering")
    print("=" * 70 + "\n")

def main():
    """Main CLI function"""
    
    print_welcome()
    
    # Validate configuration
    try:
        Config.validate()
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please add GEMINI_API_KEY to your .env file\n")
        return
    
    # Initialize agent
    agent = InterviewAgent()
    
    # Start conversation
    print("Interviewer: ", end="")
    intro = agent.send_message("Hello! I'm ready to start practicing.")
    print(intro + "\n")
    
    # Main conversation loop
    while True:
        try:
            # Get user input
            user_input = input(" You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye', 'stop']:
                print("\nInterviewer: Thank you for practicing with me!")
                print("Good luck with your real interview! \n")
                
                # Ask to save transcript
                save = input("Would you like to save the transcript? (yes/no): ").strip().lower()
                if save in ['yes', 'y']:
                    filename = agent.save_transcript()
                    print(f"Transcript saved to {filename}\n")
                break
            
            # Skip empty inputs
            if not user_input:
                print("(Please type your response)\n")
                continue
            
            # Get agent response
            print("\nInterviewer: ", end="")
            response = agent.send_message(user_input)
            print(response + "\n")
            
            # Show progress
            if agent.stage == "interviewing":
                print(f"[Progress: {agent.questions_asked}/{Config.MAX_QUESTIONS} questions]\n")
            
            # End after feedback
            if agent.is_complete():
                print("\n" + "=" * 70)
                print("Interview practice session complete!")
                print("=" * 70 + "\n")
                
                save = input("Would you like to save the transcript? (yes/no): ").strip().lower()
                if save in ['yes', 'y']:
                    filename = agent.save_transcript()
                    print(f"Transcript saved to {filename}\n")
                break
                
        except KeyboardInterrupt:
            print("\n\nSession interrupted.")
            print("Thank you for practicing! Goodbye!\n")
            break
            
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            print("Please try again or type 'quit' to exit.\n")

if __name__ == "__main__":
    main()
