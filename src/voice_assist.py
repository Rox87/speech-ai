import sounddevice as sd
import soundfile as sf
import tempfile
import os
from openai import OpenAI
from chatgpt_speech import chat_and_speak
from clean_folder import clean_folder


client = OpenAI()

def record_audio(file_path, duration=5, samplerate=44100):
    """Record audio from the microphone and save it to a file."""
    print("Recording...")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    sf.write(file_path, audio_data, samplerate)
    print("Recording finished.")

def listen_and_respond():
    print("Voice assistant started. Say 'exit' to quit.")
    
    while True:
  # Remove the file
        try:
            # Create temporary file for recording
            with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_audio:
                temp_filename = temp_audio.name

                # Record audio from microphone
                record_audio(temp_filename, duration=5)  # Record for 5 seconds
                
            # Transcribe the audio
            with open(temp_filename, 'rb') as audio_file:
                user_input = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                ).text
            
            # Get transcribed text
            #user_input = audio
            print(f"You said: {user_input}")
            
            # Check for exit command
            if user_input.lower().strip().__contains__("bye") and len(user_input.lower().strip()) < 7:
                print("Exiting voice assistant...")
                break
                
            # Get ChatGPT response
            response = chat_and_speak(user_input)
            print(f"Assistant: {response}")
            
       
                
        except KeyboardInterrupt:
            print("\nExiting voice assistant...")
            break
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            # Clean up temporary files
            if os.path.exists(temp_filename):
                os.remove(temp_filename)

if __name__ == "__main__":
    clean_folder("temp")
    listen_and_respond()
