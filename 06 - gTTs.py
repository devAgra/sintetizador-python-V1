# Criará um arquivo mp3, e reproduzirá o arquivo automaticamente. 

from gtts import gTTS
from playsound import playsound
tts = gTTS('Que você possa colher as melhores flores de esperança e de fé deste novo dia lindo!', lang='pt-br') # Mensagem no idioma portugues / Brasil
tts.save('mensagem.mp3')
playsound('mensagem.mp3')
