"""Core module for audio playback functionality."""
import pygame
from playsound import playsound

def play_with_pygame(filename: str):
    """Play audio file using pygame with error handling"""
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        print("Playing audio...")
        
        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
        print("Audio playback finished.")
            
    except pygame.error as e:
        print(f"Audio playback error: {str(e)}")

def play_with_playsound(filename: str):
    """Play audio file using playsound"""
    try:
        playsound(filename)
    except Exception as e:
        print(f"Audio playback error: {str(e)}")