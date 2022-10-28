# biblioteca para traduzir o texto
from googletrans import Translator
# biblioteca para ambiente web
import streamlit as st
# usar nltk para classificar o texto
import nltk
from nltk.stem import RSLPStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
from bases import stop_palavras
from nltk.tokenize import word_tokenize
from nrclex import NRCLex
import plotly.express as px
import pandas as pd
import json

nltk.download('all')


# função para pedir texto para o usuário
def get_text():
    text = st.text_area("Digite o texto a ser traduzido")
    if text:
        return text


# menu de idiomas para tradução
def get_lang():
    try:
        lang = st.selectbox("Selecione o idioma",
                            ("Alemão", "Inglês", "Espanhol", "Francês", "Italiano", "Japonês", "Coreano", "Chinês"))
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
        print("Erro ao selecionar idioma", e)


# traduzir o texto do português para o idioma selecionado
def translate_text(text, lang):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=lang)
        return translated.text
    except Exception as e:
        print("Erro ao traduzir o texto", e)


# remover stopwords do texto
def remove_stopwords(text):
    stopwords = stop_palavras
    text = [word for word in text if word not in stopwords]
    return text


# função para traduzir o texto sempre para o inglês
def traduzirParaIngles(texto):
    translator = Translator()
    texto = translator.translate(texto, dest="en")
    return texto.text


# funçao para stemizar o texto
def Stemize(text):
    stemmer = RSLPStemmer()
    stem = []
    for i in text:
        stem.append(stemmer.stem(i))
    return stem


# função para tokenizar o texto
def Tokenize(text):
    text = word_tokenize(text)
    return text


def tratar_texto(text):
    # traduzir o texto para o inglês
    text = traduzirParaIngles(text)
    # tokenizar o texto
    text = Tokenize(text)
    # remover stopwords do texto
    text = remove_stopwords(text)
    # stemizar o texto
    text = Stemize(text)
    return text


# função para analisar sentimento do texto
def analisar_sentimento(text):
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(text)
    # retornar se o texto é positivo, negativo ou neutro
    st.write(score)
    if score['compound'] > 0.0:
        st.text("O sentimento do texto é positivo")
    elif score['compound'] < 0.0:
        st.write("O sentimento do texto é negativo")
    else:
        st.write("O sentimento do texto é neutro")


def CriarDataFrameEmocoes(text):
    emotion = NRCLex(text)
    # pegar resultado do de cada emoção
    anger = emotion.raw_emotion_scores['anger']
    anticipation = emotion.raw_emotion_scores['anticipation']
    disgust = emotion.raw_emotion_scores['disgust']
    fear = emotion.raw_emotion_scores['fear']
    joy = emotion.raw_emotion_scores['joy']
    sadness = emotion.raw_emotion_scores['sadness']
    surprise = emotion.raw_emotion_scores['surprise']
    trust = emotion.raw_emotion_scores['trust']
    # criar um dicionário com as emoções e seus valores
    emocoes = {"Raiva": anger, "Antecipação": anticipation, "Nojo": disgust, "Medo": fear, "Alegria": joy,
               "Tristeza": sadness, "Surpresa": surprise, "Confiança": trust}
    # criar um dataframe com as emoções e seus valores
    df = pd.DataFrame(emocoes.items(), columns=['Emoção', 'Valor'])
    return df


def CriarDataFrameSentimentos(text):
    emotion = NRCLex(text)
    # pegar resultado do de cada emoção
    positivo = emotion.raw_emotion_scores['positive']
    negativo = emotion.raw_emotion_scores['negative']
    # criar um dicionário com as emoções e seus valores
    sentimento = {"Positivo": positivo, "Negativo": negativo}
    # criar um dataframe com as emoções e seus valores
    df = pd.DataFrame(sentimento.items(), columns=['Sentimento', 'Valor'])
    return df


# função para analisar emoções do texto
def analisar_emocoes(df):
    st.markdown(df.to_html(index=False), unsafe_allow_html=True)
    # mostra top 3 emoções
    st.write("Top 3 emoções")
    st.write(df.sort_values(by=['Valor'], ascending=False).head(3))
    # mostra gráfico de barras
    fig = px.bar(df, x='Emoção', y='Valor', title='Emoções', color='Valor')
    st.plotly_chart(fig)


def analisar_sentimentos(df):
    st.markdown(df.to_html(index=False), unsafe_allow_html=True)
    # mostra gráfico de barras
    fig = px.bar(df, x='Sentimento', y='Valor', title='Sentimentos', color='Valor')
    st.plotly_chart(fig)


def main():
    # criar interface com menuS
    menu = ["Home", "Analisar Texto", "Analise de Sentimento", "Analise de Emoções",
            "Analise de Sentimentos Secundários", "Tradutor"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home")
        st.text("Bem vindo ao projeto de análise de sentimentos")
        st.text("Escolha uma opção no menu")
    elif choice == "Analisar Texto":
        st.subheader("Analisar Texto")
        text = st.text_area("Digite o texto")
        if st.button("Analisar"):
            st.write(text)
    elif choice == "Analise de Sentimento":
        st.subheader("Analise de Sentimento")
        text = st.text_area("Digite o texto")
        if st.button("Analisar"):
            text = tratar_texto(text)
            text = ' '.join(text)
            analisar_sentimento(text)
    elif choice == "Analise de Emoções":
        st.subheader("Analise de Emoções")
        text = st.text_area("Digite o texto")
        if st.button("Analisar"):
            text = tratar_texto(text)
            text = ' '.join(text)
            df = CriarDataFrameEmocoes(text)
            analisar_emocoes(df)
    elif choice == "Analise de Sentimentos Secundários":
        st.subheader("Analise de Sentimentos Secundários")
        text = st.text_area("Digite o texto")
        if st.button("Analisar"):
            text = tratar_texto(text)
            text = ' '.join(text)
            df = CriarDataFrameSentimentos(text)
            analisar_sentimentos(df)
    elif choice == "Tradutor":
        text = get_text()
        lang = get_lang()
        if st.button("Traduzir"):
            traducao = translate_text(text, lang)
            st.write(traducao)


if __name__ == "__main__":
    main()
