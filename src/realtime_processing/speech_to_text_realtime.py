import sounddevice as sd
import numpy as np
import io
import requests
import wave
import os
# OpenAI API endpoint and API key
API_URL = "https://api.openai.com/v1/audio/transcriptions"
API_KEY = os.environ.get("OPENAI_API_KEY")

# Function to record audio and process in chunks
def record_and_transcribe(chunk_duration=5, samplerate=44100, channels=1):
    print("Starting real-time audio processing...")
    
    def send_to_openai(audio_data):
        """Send audio data to OpenAI API for transcription."""
        # Save audio data to an in-memory WAV file
        audio_buffer = io.BytesIO()
        with wave.open(audio_buffer, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(2)  # Sample width for int16
            wf.setframerate(samplerate)
            wf.writeframes(audio_data.tobytes())
        audio_buffer.seek(0)
        
        # Prepare the request
        files = {
            "file": ("audio.wav", audio_buffer, "audio/wav"),
        }
        headers = {
            "Authorization": f"Bearer {API_KEY}",
        }
        data = {
            "model": "whisper-1",  # Whisper model name (adjust if needed)
        }

        # Send request to OpenAI API
        response = requests.post(API_URL, headers=headers, files=files, data=data)
        if response.status_code == 200:
            return response.json().get("text", "")
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None

    try:
        while True:
            print("Recording...")
            # Record audio in chunks
            audio_data = sd.rec(int(chunk_duration * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
            sd.wait()  # Wait for the recording to complete
            print("Processing...")
            
            # Transcribe the audio using OpenAI API
            transcription = send_to_openai(audio_data)
            if transcription:
                print(f"Transcription: {transcription}")
            else:
                print("Failed to transcribe audio.")
    
    except KeyboardInterrupt:
        print("Stopped real-time audio processing.")

# Start processing
record_and_transcribe()
