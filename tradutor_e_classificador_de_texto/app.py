#biblioteca para traduzir o texto
from googletrans import Translator
#biblioteca para ambiente web
import streamlit as st
#usar nltk para classificar o texto
import nltk
from nltk.stem import RSLPStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
from bases import stop_palavras
from nltk.tokenize import word_tokenize
from nrclex import NRCLex
import json
nltk.download('all')
#função para pedir texto para o usuário
def get_text():
    text = st.text_area("Digite o texto a ser traduzido")
    if text:
        return text

#menu de idiomas para tradução
def get_lang():
    try:
        lang = st.selectbox("Selecione o idioma",("Alemão","Inglês","Espanhol","Francês","Italiano","Japonês","Coreano","Chinês"))
        if lang == "Alemão":
            return "de"
        elif lang == "Inglês":
            return "en"
        elif lang == "Espanhol":
            return "es"
        elif lang == "Francês":
            return "fr"
        elif lang == "Italiano":
            return "it"
        elif lang == "Japonês":
            return "ja"
        elif lang == "Coreano":
            return "ko"
        elif lang == "Chinês":
            return "zh-CN"
    except Exception as e:
        print("Erro ao selecionar idioma",e)

#traduzir o texto do português para o idioma selecionado
def translate_text(text, lang):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=lang)
        return translated.text
    except Exception as e:
        print("Erro ao traduzir o texto",e)
        
#remover stopwords do texto
def remove_stopwords(text):
    stopwords = stop_palavras
    text = [word for word in text if word not in stopwords]
    return text
        
#função para traduzir o texto sempre para o inglês
def traduzirParaIngles(texto):
    translator = Translator()
    texto = translator.translate(texto, dest="en")
    return texto.text

#funçao para stemizar o texto
def Stemize(text):
    stemmer = RSLPStemmer()
    stem = []
    for i in text:
        stem.append(stemmer.stem(i))
    return stem

#função para tokenizar o texto
def Tokenize(text):
    text = word_tokenize(text)
    return text

def tratar_texto(text):
    #traduzir o texto para o inglês
    text = traduzirParaIngles(text)
    #tokenizar o texto
    text = Tokenize(text)
    #remover stopwords do texto
    text = remove_stopwords(text)
    #stemizar o texto
    text = Stemize(text)
    return text

#função para analisar sentimento do texto
def analisar_sentimento(text):
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(text)
    #retornar se o texto é positivo, negativo ou neutro
    st.write(score)
    if score['compound'] > 0.0:
        st.text("O sentimento do texto é positivo")
    elif score['compound'] < 0.0:
        st.write("O sentimento do texto é negativo")
    else:
        st.write("O sentimento do texto é neutro")
        
#função para analisar emoções do texto
def analisar_emocoes(text):
    emotion = NRCLex(text)
    #mostra emoçoes do texto em forma de dicionário
    st.write(emotion.raw_emotion_scores)
    #mostra o top 2 de emoções do texto
    st.write(emotion.top_emotions)
        
        
def main():
    st.title("Tradutor de Texto")
    text = get_text()
    lang = get_lang()
    #criar um botão para traduzir o texto
    if st.button("Traduzir"):
        translated_text = translate_text(text, lang)
        st.text_area(f"Tradução para {lang}",translated_text)
    #criar um botão para classificar o texto
    if st.button("Classificar"):    
        text = tratar_texto(text)
        text = ' '.join(text)
        analisar_sentimento(text)
    if st.button("Analisar emoções"):
        text = tratar_texto(text)
        text = ' '.join(text)
        analisar_emocoes(text)
        
if __name__ == "__main__":
    main()
    
