from gtts import gTTS
from playsound import playsound
import os
import tempfile
def time_elapsed(func):
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Time elapsed: {end_time - start_time} seconds")
    return wrapper

@time_elapsed
def speak(text):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as fp:
        temp_filename = fp.name
        
    # Convert text to speech
    tts = gTTS(text=text, lang='en')
    tts.save(temp_filename)
    
    # Play the audio
    playsound(temp_filename)
    
    # Clean up
    os.remove(temp_filename)

if __name__ == "__main__":
    # Example usage
    speak("I am your english teacher nice to meet you?")
