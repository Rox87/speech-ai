from faster_whisper import WhisperModel
from openai import OpenAI
client = OpenAI()

def time_elapsed(func):
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        return result
    return wrapper

# Carregar modelo médio (balance entre velocidade e precisão)
model = WhisperModel("tiny.en", device="cpu", compute_type="int8")

@time_elapsed
def openai_whisper_api(audio_file):
    # Transcribe the audio
    with open(audio_file, 'rb') as audio_file:
        user_input = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        ).text
    return user_input

@time_elapsed
def local_transcribe_audio(file_path):

    
    # Transcrever áudio
    # segments, info = model.transcribe(file_path)
    # text = " ".join(segment.text for segment in segments)
    
    segments, _ = model.transcribe(file_path)

    for segment in segments:
        print(segment.text, end=" ", flush=True)  # Stream transcription
        yield(segment.text)
    # Salvar transcrição
    # output_path = file_path + ".txt"
    # with open(output_path, "w") as f:
    #     f.write(text)
    
    # print(f"Transcrição salva em: {output_path}")
    #return text

if __name__ == "__main__":
    #print(openai_whisper_api("demo.mp3"))
    local_transcribe_audio("demo.mp3")
