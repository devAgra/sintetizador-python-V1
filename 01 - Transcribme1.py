import pyttsx3                              # Biblioteca
engine = pyttsx3.init()						# Iniciando a biblioteca
engine.setProperty("voice","Brazil")		# Convertendo a biblioteca para o idioma portugues / Brazil
engine.say("Olá, como estão?")              # Texto convertido em voz
engine.runAndWait()
