import pyttsx3
engine = pyttsx3.init()
engine.setProperty("voice", "Brazil")
frase = input("Digite a frase a ser falada:\n ")
engine.say(frase)
engine.runAndWait()