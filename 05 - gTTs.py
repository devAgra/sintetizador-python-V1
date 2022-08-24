# Criará um arquivo mp3, e reproduzirá o arquivo automaticamente. 

from gtts import gTTS
from playsound import playsound
tts = gTTS('Hello World!!') # Mensagem no idioma padrão / inglês
tts.save('hello.mp3')
playsound('hello.mp3')