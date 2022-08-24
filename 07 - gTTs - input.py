# Criará um arquivo mp3, e reproduzirá o arquivo automaticamente. 

from gtts import gTTS
from playsound import playsound
frase = input("Digite algo que vc deseja ser convertido para voz: \n")
tts = gTTS(lang='pt-br') # Mensagem no idioma portugues / Brasil
tts.save('mensagem.mp3') # salvando a mensagem
playsound('mensagem.mp3') # Conversão de texto para voz