from openai import OpenAI
import pygame

client = OpenAI()

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

    temp_mp3 = "output.mp3"
        
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text
    )
    
    response.stream_to_file(temp_mp3)
     

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load("output.mp3")

    # Play the audio
    pygame.mixer.music.play()

    print("Playing audio...")

    # Keep the script running until the audio finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    print("Audio playback finished.")
    
    # Clean up
    #os.remove(mp3_filename)

if __name__ == "__main__":
    # Example usage
    speak("I am your english teacher nice to meet you?")
