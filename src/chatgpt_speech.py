from openai import OpenAI
import pygame
import time
import os
import tempfile
import hashlib
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from gtts import gTTS
import io
# InitialiProcessandoze OpenAI client
client = OpenAI()

# Initialize pygame once
pygame.mixer.init()

# Thread pool for I/O operations
executor = ThreadPoolExecutor(max_workers=4)
history = [
        {"role": "system", "content": "You are a English teacher who will help me to learn english, you only speak english"}
]
# Cache for ChatGPT responses (max 128 entries)
@lru_cache(maxsize=128)
def get_chatgpt_response(prompt: str) -> str:
    """Get cached ChatGPT response with thread pool execution"""
    def _get_response():
        history.append({"role": "user", "content": prompt})
        return client.chat.completions.create(
            model="gpt-4o-mini",
            messages=history
        ).choices[0].message.content
    
    return executor.submit(_get_response).result()

def generate_audio_file(text: str) -> str:
    """Generate audio file from text using OpenAI TTS"""
    try:
        # response = client.audio.speech.create(
        #     model="tts-1",
        #     voice="nova",
        #     input=text
        # )
        
        # with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as fp:
        #     temp_filename = fp.name
                
        # Convert text to speech    
        tts = gTTS(text=text, lang='en')
        # file_hash = hashlib.md5(text.encode()).hexdigest()
        # temp_filename = f"temp/temp_{file_hash}.mp3"
        # tts.save(temp_filename)
        audio_bytes = io.BytesIO()
        tts.write_to_fp(audio_bytes)  # Save the audio directly to BytesIO
        audio_bytes.seek(0)  # Seek to the beginning of the BytesIO
        # Create temporary file with hash-based name
        
        

        # Stream to file
        # response.stream_to_file(temp_filename)
        return audio_bytes
        
    except Exception as e:
        print(f"Error generating audio: {str(e)}")
        raise

def play_audio(filename: str):
    """Play audio file using pygame with error handling"""
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
    except pygame.error as e:
        print(f"Audio playback error: {str(e)}")



def chat_and_speak(prompt: str):
    """Main function to get ChatGPT response and speak it"""
    try:
        # Get response from ChatGPT
        response_text = get_chatgpt_response(prompt)
        print(f"ChatGPT Response: {response_text}")
        
        # Generate and play audio
        audio_file = generate_audio_file(response_text)
        play_audio(audio_file)
        
    except Exception as e:
        print(f"Error in chat_and_speak: {str(e)}")


if __name__ == "__main__":
    # Example usage
    chat_and_speak("Who are you?")
