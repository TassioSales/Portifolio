# biblioteca para traduzir o texto
from googletrans import Translator, LANGUAGES
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

# função para pedir texto para o usuário
def get_text():
    text = st.text_area("Digite o texto a ser traduzido")
    if text:
        return text


# criar função para retornar o um diciônario com todos os idiomas disponíveis
def get_langs():
    langs = LANGUAGES
    return langs

# traduzir o texto do português para o idioma selecionado
def translate_text(text, lang):
    translator = Translator()
    text = translator.translate(text, dest=lang)
    return text.text


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
    get_langs()
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
    #vericar quais emoções estão presentes em emotion.raw_emotion_scores
    emocoes = emotion.raw_emotion_scores.keys()
    # criar um dicionário com as emoções e seus valores
    emocoes_dict = {}
    for i in emocoes:
        emocoes_dict[i] = emotion.raw_emotion_scores[i]
    emocoes_tb = {k: v for k, v in emocoes_dict.items() if v != 0}
    # remover as chaver positivo e negativo do dicionário
    emocoes_tb.pop('positive')
    emocoes_tb.pop('negative')
    # criar um dataframe com as emoções e seus valores
    df = pd.DataFrame(emocoes_tb.items(), columns=['Emoção', 'Valor'])
    # traduzir o nome das emoções para o português
    df['Emoção'] = df['Emoção'].replace({'fear': 'Medo', 'anger': 'Raiva', 'anticipation': 'Antecipação', 'trust': 'Confiança',
                                        'surprise': 'Surpresa', 'sadness': 'Tristeza', 'disgust': 'Nojo', 'joy': 'Alegria'})
    return df


def CriarDataFrameSentimentos(text):
    emotion = NRCLex(text)
    emocoes = emotion.raw_emotion_scores.keys()
    positivo = emotion.raw_emotion_scores['positive']
    negativo = emotion.raw_emotion_scores['negative']
    emocoes_dict = {}
    for i in emocoes:
        emocoes_dict[i] = emotion.raw_emotion_scores[i]
        # pegar somente as emoções positivas e negativas
    emocoes_tb = {k: v for k, v in emocoes_dict.items() if k == 'positive' or k == 'negative'}
    # criar um dataframe com as emoções e seus valores
    df = pd.DataFrame(emocoes_tb.items(), columns=['Sentimento', 'Valor'])
    # traduzir o nome das emoções para o português
    df['Sentimento'] = df['Sentimento'].replace({'positive': 'Positivo', 'negative': 'Negativo'})
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



if __name__ == "__main__":
    main()
