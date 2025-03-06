import pygame

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
