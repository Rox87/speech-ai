import sounddevice as sd
from openai import OpenAI
from openai import OpenAI
from core.audio.audio_transcriber import local_transcribe_audio
from core.tts.synthesizer import synthesize_with_openai
from dotenv import load_dotenv
import pygame
import os

# Load environment variables from .env file
load_dotenv()

# Initialize pygame for audio playback
pygame.mixer.init()

# Initialize OpenAI client with API key from environment
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Chat history
history = [
    {"role": "system", "content": "You are a helpful voice assistant."}
]

def chat_and_speak(prompt: str):
    """Get ChatGPT response and convert it to speech"""
    try:
        # Add user message to history
        history.append({"role": "user", "content": prompt})
        
        # Get response from ChatGPT
        response = client.chat.completions.create(
            model="gpt-4",
            messages=history
        )
        response_text = response.choices[0].message.content
        
        # Add assistant response to history
        history.append({"role": "assistant", "content": response_text})
        
        # Generate speech from response
        output_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "temp", "response.mp3")
        os.makedirs(os.path.dirname(output_file), mode=0o755, exist_ok=True)
        if synthesize_with_openai(response_text, output_file):
            try:
                # Set file permissions for response.mp3
                os.chmod(output_file, 0o755)
                # Play the audio
                pygame.mixer.music.load(output_file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                # Unload and stop the music to release the file
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                return response_text
            except Exception as audio_error:
                print(f"Error playing audio: {str(audio_error)}")
                return response_text
            finally:
                # Ensure pygame mixer is properly reset
                pygame.mixer.quit()
                pygame.mixer.init()
    except Exception as e:
        print(f"Error in chat_and_speak: {str(e)}")
        return str(e)
import io
import wave

client = OpenAI()

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
    print("Voice assistant started. Say 'bye' to quit.")
    
    # Ensure temp directory exists
    import os
    os.makedirs("temp", exist_ok=True)
    
    while True:
        try:
            # Record audio from microphone
            # Transcribe the audio
            user_input = ""
            for segment in local_transcribe_audio(record_audio_to_bytes()):
                user_input += segment
            
            print(f"You said: {user_input}")
            
            # Check for exit command
            if user_input.lower().strip().__contains__("bye") and len(user_input.lower().strip()) < 5:
                print("Exiting voice assistant...")
                break
                
            # Get ChatGPT response and speak it
            response = chat_and_speak(user_input)
            print(f"Assistant: {response}")
                
        except KeyboardInterrupt:
            print("\nExiting voice assistant...")
            break
        except Exception as e:
            print(f"Error: {str(e)}")
            

if __name__ == "__main__":
    clean_folder("temp")
    listen_and_respond()
