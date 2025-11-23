"""
Voice input handler for interview agent
"""
import speech_recognition as sr

class VoiceHandler:
    """Handles speech recognition (voice input only)"""
    
    def __init__(self):
        """Initialize voice handler"""
        self.recognizer = sr.Recognizer()
        
        # Adjust recognizer settings for better long-form speech
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 1.5  # Wait 1.5s of silence before stopping
    
    def listen(self, timeout=10, phrase_time_limit=None):
        """
        Listen to microphone and convert speech to text
        
        Args:
            timeout: Seconds to wait for speech to start
            phrase_time_limit: Maximum phrase length (None = unlimited)
            
        Returns:
            str: Recognized text or None if failed
        """
        try:
            with sr.Microphone() as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                # Listen for audio
                audio = self.recognizer.listen(
                    source, 
                    timeout=timeout,
                    phrase_time_limit=phrase_time_limit
                )
                
                # Convert to text using Google Speech Recognition
                text = self.recognizer.recognize_google(audio)
                return text
                
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
            return None
        except Exception as e:
            print(f"Microphone error: {e}")
            return None
