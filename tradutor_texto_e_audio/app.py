#baixar bibliotecas para tradução de texto
from googletrans import Translator
#baixar biblioteca para reconhecimento de voz
import speech_recognition as sr
#baixar biblioteca gtts para transformar texto em voz
from gtts import gTTS
#baixar biblioteca playsound para tocar o audio
from playsound import playsound
#baixar biblioteca Streamlit para criar a interface
import streamlit as st
import pyaudio

#função para reconhecer a voz
def ouvir_microfone():
    #Habilita o microfone para ouvir o usuário
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        #Chama a função de redução de ruido disponível na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        #Avisa ao usuário que está pronto para ouvir
        st.write("Diga alguma coisa: ")
        #Criar botao para iniciar a gravação
        if st.button("Iniciar Gravação"):
            #Armazena a informação de áudio na variável
            audio = microfone.listen(source)
        #criar botao para parar a gravação
        if st.button("Parar Gravação"):
            microfone.stop_listening()
        try:
            #Passa o áudio para o reconhecedor de padroes do speech_recognition
            frase = microfone.recognize_google(audio, language='pt-BR')
            #Após alguns segundos, retorna a frase falada
            st.text_area("Você disse: " + frase)
            #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
        except sr.UnknownValueError:
            st.write("Não entendi")
    return frase

#função para configurar pyaudio
def config_pyAudio():
    #cria um objeto
    p = pyaudio.PyAudio()
    #abre o stream
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    #fecha o stream
    stream.stop_stream()
    stream.close()
    p.terminate()

#menu para escolher para qual idioma traduzir
def menu():
    st.write("Escolha o idioma para traduzir")
    st.write("1 - Inglês")
    st.write("2 - Espanhol")
    st.write("3 - Francês")
    st.write("4 - Alemão")
    st.write("5 - Italiano")
    st.write("6 - Português")
    st.write("7 - Japonês")
    opt = st.number_input("Digite a opção desejada: ")
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
    return idioma

#função para traduzir o texto
def traduzir(texto, idioma):
    tradutor = Translator()
    traducao = tradutor.translate(texto, dest=idioma)
    return traducao.text

#função para falar o texto
def falar(texto, idioma):
    #cria o arquivo de audio
    tts = gTTS(texto, lang=idioma)
    #define o nome do arquivo
    nome_arquivo = 'audio.mp3'
    #salva o arquivo
    tts.save(nome_arquivo)
    #da play no audio
    playsound(nome_arquivo)
    
#função principal
def main():
    #cria o menu
    idioma = menu()
    #configura o pyaudio
    config_pyAudio()
    #chama a função para ouvir e reconhecer a fala
    texto = ouvir_microfone()
    #chama a função para traduzir o texto
    texto_traduzido = traduzir(texto, idioma)
    #chama a função para falar o texto
    falar(texto_traduzido, idioma)
    #mostra o texto traduzido
    st.text_area("Texto traduzido: " + texto_traduzido)

#chama a função principal
if __name__ == '__main__':
    main()