from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input="Hello world! How are you?"
)
mp3_filename = "output.mp3"
response.stream_to_file(mp3_filename)