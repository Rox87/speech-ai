# Text-to-Speech Solutions

Este repositório contém diferentes implementações para conversão de texto em fala e reprodução de áudio em Python, utilizando diferentes bibliotecas e abordagens.

## Requisitos

- Python 3.x
- Dependências (instalar via pip):
  ```bash
  pip install openai pygame gtts playsound
  ```
- Para usar a API da OpenAI, configure sua chave API no arquivo `.env`:
  ```
  OPENAI_API_KEY=sua_chave_aqui
  ```

## Implementações Disponíveis

### 1. Assistente de Voz (`voice_assistant.py`)
- Escuta contínua de comandos de voz
- Uso do Whisper para reconhecimento de fala
- Integração com ChatGPT-4 para geração de respostas
- Respostas faladas usando OpenAI TTS
- Comando 'exit' para encerrar o assistente

**Uso:**
```python
python voice_assistant.py
```

### 2. ChatGPT-4 + OpenAI TTS (`chatgpt_speech.py`)
- Integração completa com ChatGPT-4 para geração de respostas
- Conversão automática da resposta em áudio
- Uso do Pygame para reprodução de áudio
- Medição de tempo para ambas operações (geração de texto e fala)

**Uso:**
```python
from chatgpt_speech import chat_and_speak
chat_and_speak("Explain quantum computing in simple terms")
```

### 2. OpenAI TTS + Pygame Player (`realtime_openai.py`)
- Usa a API da OpenAI para conversão de texto em fala
- Utiliza Pygame para reprodução de áudio
- Inclui medição de tempo de execução
- Gera arquivo temporário `output.mp3`

**Uso:**
```python
from realtime_openai import speak
speak("Hello, how are you?")
```

### 2. Google TTS + Playsound (`realtime_gtts.py`)
- Usa a biblioteca gTTS para conversão de texto em fala
- Utiliza playsound para reprodução de áudio
- Cria arquivos temporários que são automaticamente removidos
- Inclui medição de tempo de execução

**Uso:**
```python
from realtime_gtts import speak
speak("Hello, how are you?")
```

### 3. OpenAI TTS Básico (`audio.speechtotext.openai.py`)
- Implementação básica usando API da OpenAI
- Gera arquivo `output.mp3`

**Uso:**
```python
python audio.speechtotext.openai.py
```

### 4. Pygame Player (`audio.play.pygame.py`)
- Implementação básica de player de áudio usando Pygame
- Reproduz arquivo `output.mp3`

**Uso:**
```python
python audio.play.pygame.py
```

### 5. Playsound Player (`audio.play.playsound.py`)
- Implementação básica de player de áudio usando playsound
- Reproduz arquivo `output.mp3`

**Uso:**
```python
python audio.play.playsound.py
```

## Comparação de Soluções

| Característica           | OpenAI + Pygame | Google TTS + Playsound |
|--------------------------|-----------------|------------------------|
| Qualidade de voz         | Alta            | Média                  |
| Requer API Key           | Sim             | Não                    |
| Gerenciamento de arquivos| Manual          | Automático             |
| Dependências             | OpenAI, Pygame  | gTTS, playsound        |
| Velocidade               | Mais lento      | Mais rápido            |

## Melhorias Futuras

- Adicionar suporte a múltiplos idiomas
- Implementar fila de reprodução
- Adicionar interface gráfica
- Implementar controle de volume
- Adicionar suporte a streaming

## Licença

MIT License
