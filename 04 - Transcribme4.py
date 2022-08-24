import pyttsx3
engine = pyttsx3.init()
engine.setProperty("voice", "Brazil")
arquivo = open("dados/frase.txt", "r", encoding="utf-8") # Realizará a leitura do texto com acentuações.
conteudo = arquivo.read()
print(conteudo)
engine.say(conteudo)
arquivo.close()
engine.runAndWait()