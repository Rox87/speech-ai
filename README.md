# Text-to-Speech Solutions

Uma solução abrangente em Python contendo várias implementações para conversão de texto em fala e reprodução de áudio, utilizando diferentes bibliotecas e abordagens.

## Estrutura do Projeto

```
src/
├── audio_playback/       # Implementações de reprodução de áudio
│   ├── play_audio_playsound.py
│   └── play_audio_pygame.py
├── core/                 # Funcionalidades principais e utilitários
│   ├── audio/            # Processamento de áudio
│   ├── tts/              # Módulos de síntese de fala
│   ├── utils/            # Funções utilitárias
│   └── voice_assistant.py # Assistente de voz principal
├── realtime_processing/  # Processamento TTS em tempo real
│   ├── realtime_gtts.py
│   ├── realtime_openai.py
│   └── speech_to_text_realtime.py
├── text_to_speech/       # Implementações de texto para fala
│   ├── text_to_speech_gtts.py
│   ├── text_to_speech_openai.py
│   └── text_to_speech_openai_realtime.py
└── main.py               # Ponto de entrada principal
```

## Requisitos

- Python 3.x
- Dependências (instale via pip):
  ```bash
  pip install --no-cache-dir -r requirements.txt
  ```
- Para recursos OpenAI, configure sua chave de API no arquivo `.env`:
  ```
  OPENAI_API_KEY=sua_chave_aqui
  ```

## Dependências Principais

- **openai**: Integração com APIs de IA da OpenAI
- **pygame**: Reprodução de áudio
- **gTTS**: Google Text-to-Speech
- **playsound**: Reprodução simplificada de áudio
- **sounddevice**: Captura de áudio
- **python-dotenv**: Gerenciamento de variáveis de ambiente

## Implementações Disponíveis

### 1. Assistente de Voz (src/core/voice_assistant.py)
- Escuta contínua de comandos de voz
- Reconhecimento de fala
- Integração com ChatGPT-4 para geração de respostas
- Respostas de voz usando OpenAI TTS
- Suporte a comandos de saída

**Uso:**
```python
python src/main.py
```

### 2. OpenAI TTS em Tempo Real (src/realtime_processing/realtime_openai.py)
- Integração com a API TTS da OpenAI
- Reprodução de áudio baseada em Pygame
- Medição do tempo de execução
- Gerenciamento de arquivos temporários

**Uso:**
```python
from src.realtime_processing.realtime_openai import speak
speak("Olá, como você está?")
```

### 3. Google TTS em Tempo Real (src/realtime_processing/realtime_gtts.py)
- Integração com Google Text-to-Speech
- Reprodução de áudio baseada em Playsound
- Limpeza automática de arquivos temporários
- Medição de desempenho

**Uso:**
```python
from src.realtime_processing.realtime_gtts import speak
speak("Olá, como você está?")
```

### 4. Opções de Reprodução de Áudio
- Player Pygame (src/audio_playback/play_audio_pygame.py)
- Player Playsound (src/audio_playback/play_audio_playsound.py)

## Comparação de Soluções

| Recurso               | OpenAI TTS          | Google TTS           |
|-----------------------|--------------------|--------------------|
| Qualidade de Voz      | Alta               | Média               |
| Chave de API Necessária| Sim                | Não                 |
| Gerenciamento de Arquivos| Manual           | Automático          |
| Dependências          | OpenAI, Pygame     | gTTS, playsound     |
| Velocidade de Processamento| Mais lenta     | Mais rápida         |
| Suporte a Idiomas     | Limitado           | Extensivo           |

## Melhorias Futuras

- [ ] Expansão do suporte a múltiplos idiomas
- [ ] Implementação de fila de reprodução de áudio
- [ ] Interface gráfica de usuário
- [ ] Integração de controle de volume
- [ ] Suporte a streaming de áudio
- [ ] Integrações com motores TTS adicionais
- [ ] Melhor tratamento de erros e recuperação
- [ ] Sistema de gerenciamento de configurações
- [ ] Suporte a vozes personalizadas
- [ ] Otimização de desempenho para dispositivos de baixo poder computacional

## Como Contribuir

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um novo Pull Request

## Licença

MIT License
