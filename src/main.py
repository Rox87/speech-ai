import sounddevice as sd
from openai import OpenAI
from core.tts.synthesizer import synthesize_with_openai
from core.voice_assistant import chat_and_speak, listen_and_respond
from core.audio.audio_transcriber import local_transcribe_audio
from dotenv import load_dotenv
import io
import wave
import os

# Load environment variables from .env file
load_dotenv()

# Ensure temp directory exists with absolute path
temp_dir = os.path.join(os.path.dirname(__file__), "..", "temp")
os.makedirs(temp_dir, exist_ok=True)

# Initialize OpenAI client with API key from environment
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def audio_stream_generator(duration=5, samplerate=44100, channels=1):
    while True:
        print("Recording...")
        # Record the audio
        audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
        sd.wait()  # Wait until recording is finished
        print("Recording finished.")

        # Save the audio to an in-memory BytesIO object
        audio_bytes = io.BytesIO()
        with wave.open(audio_bytes, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(2)  # 2 bytes for 'int16'
            wf.setframerate(samplerate)
            wf.writeframes(audio_data.tobytes())

        # Reset the pointer of BytesIO object to the start
        audio_bytes.seek(0)
        
        # Yield the audio stream
        yield audio_bytes.getvalue().decode('latin-1')

def record_audio_to_bytes(duration=5, samplerate=44100, channels=1):
    """Record audio from the microphone and save it to a BytesIO object."""
    print("Recording...")
    
    # Record audio
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")
    
    # Save the audio to an in-memory BytesIO object
    audio_bytes = io.BytesIO()
    with wave.open(audio_bytes, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)  # 2 bytes for 'int16'
        wf.setframerate(samplerate)
        wf.writeframes(audio_data.tobytes())
    
    # Reset the pointer of BytesIO object to the start
    audio_bytes.seek(0)
    
    return audio_bytes



def listen_and_respond():
    print("Voice assistant started. Say 'exit' to quit.")
    
    while True:
        
  # Remove the file
        try:
            # Create temporary file for recording
            # with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_audio:
            #     temp_filename = temp_audio.name

                # Record audio from microphone
                  # Record for 5 seconds
                
            # Transcribe the audio
            user_input = ""
            i=1
            for segment in local_transcribe_audio(record_audio_to_bytes()):
                user_input += segment
                # Loop through the segments and generate audio for each
            
            #whisper cpu version
            # user_input = transcribe_audio(temp_filename)
            
            #user_input = audio
            print(f"You said: {user_input}")
            
            # Check for exit command
            if user_input.lower().strip().__contains__("bye") and len(user_input.lower().strip()) < 5:
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
            

if __name__ == "__main__":
    listen_and_respond()
