import whisper
##Não esquecer que para usar precisa baixar o openai-whisper
##Configurar o FFmpeg
modelo = whisper.load_model("base")

audio = modelo.transcribe("PapoTech.mp3", verbose = False)
for treco in audio["segments"]:
    print(treco["text"].strip())