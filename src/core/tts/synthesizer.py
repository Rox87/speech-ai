"""Core module for text-to-speech synthesis functionality."""
from openai import OpenAI
from gtts import gTTS

def synthesize_with_openai(text: str, output_file: str, voice: str = "nova", model: str = "tts-1"):
    """Synthesize text to speech using OpenAI's TTS service"""
    try:
        client = OpenAI()
        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=text
        )
        response.stream_to_file(output_file)
        return True
    except Exception as e:
        print(f"OpenAI TTS error: {str(e)}")
        return False

def synthesize_with_gtts(text: str, output_file: str, lang: str = 'en'):
    """Synthesize text to speech using Google's TTS service"""
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(output_file)
        return True
    except Exception as e:
        print(f"Google TTS error: {str(e)}")
        return False