#baixar bibliotecas para tradução de texto
from googletrans import Translator
#baixar biblioteca para reconhecimento de voz
import speech_recognition as sr
#baixar biblioteca para falar
import pyttsx3
#baixar biblioteca para pegar data e hora
import datetime
#baixar biblioteca para pegar o sistema operacional
import os
#baixar biblioteca para pegar o tempo
import time
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#criar função para reconhecer a voz
def ouvir_microfone():
    #Habilita o microfone para ouvir o usuário
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        #Chama a função de redução de ruido disponível na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        #Avisa ao usuário que está pronto para ouvir
        print("Diga alguma coisa: ")
        #Armazena a informação de áudio na variável
        audio = microfone.listen(source)
        try:
            #Passa o áudio para o reconhecedor de padroes do speech_recognition
            frase = microfone.recognize_google(audio, language='pt-BR')
            #Após alguns segundos, retorna a frase falada
            print("Você disse: " + frase)
            #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
        except sr.UnknownValueError:
            print("Não entendi")
    return frase

#menu para escolher para qual idioma traduzir
def menu():
    print("Escolha o idioma para traduzir")
    print("1 - Inglês")
    print("2 - Espanhol")
    print("3 - Francês")
    print("4 - Alemão")
    print("5 - Italiano")
    print("6 - Português")
    print("7 - Japonês")
    opt = int(input("Digite a opção desejada: "))
    if opt == 1:
        idioma = 'en'
    elif opt == 2:
        idioma = 'es'
    elif opt == 3:
        idioma = 'fr'
    elif opt == 4:
        idioma = 'de'
    elif opt == 5:
        idioma = 'it'
    elif opt == 6:
        idioma = 'pt'
    elif opt == 7:
        idioma = 'ja'
    else:
        print("Opção inválida") 
    return idioma
 

#criar funçaõ para traduzir frase para ingles
def traduzir(frase, idioma):
    #criar objeto para tradução
    tradutor = Translator()
    #traduzir frase
    traducao = tradutor.translate(frase, dest=idioma)
    #retornar frase traduzida
    return traducao.text


#tranforma frase em audio
def fala(frase, idioma):
    tts = gTTS(frase, lang=idioma)
    #salva o arquivo de audio
    tts.save('hello.mp3')
    #da play ao audio
    playsound('hello.mp3')

def main():
    #chamar função para reconhecer a voz
    frase = ouvir_microfone()
    #chamar função para traduzir a frase
    idioma = menu()
    traducao = traduzir(frase, idioma)
    print(traducao)
    fala(traducao, idioma)
    
if __name__ == "__main__":
    main()
    
   

    
    

    
    








