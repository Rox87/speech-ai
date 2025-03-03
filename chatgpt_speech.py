from openai import OpenAI
import pygame
import time
import os
import tempfile

client = OpenAI()

def time_elapsed(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time elapsed: {end_time - start_time} seconds")
        return result
    return wrapper

@time_elapsed
def get_chatgpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

@time_elapsed
def speech(text):
        # Generate speech from text
        response = client.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=text
        )
        
        # Create temporary file
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
            temp_filename = temp_file.name
            response.stream_to_file(temp_filename)
            
        # Initialize pygame mixer
        pygame.mixer.init()
        pygame.mixer.music.load(temp_filename)
        pygame.mixer.music.play()
        
        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            

def chat_and_speak(prompt):
    # Get response from ChatGPT
    response_text = get_chatgpt_response(prompt)
    print(f"ChatGPT Response: {response_text}")
    
    # Convert response to speech
    speech(response_text)

if __name__ == "__main__":
    # Example usage
    chat_and_speak("Who are you?")
