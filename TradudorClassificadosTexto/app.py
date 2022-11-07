from collections import Counter
from googletrans import Translator
import streamlit as st
from langdetect import detect_langs, DetectorFactory
from nltk.stem import RSLPStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nrclex import NRCLex
import plotly.express as px
import pandas as pd
import spacy
import nltk
nltk.download('punkt')
nltk.download('rslp')


# função para pedir texto para o utilizador
def get_text():
    try:
        text = st.text_area("Digite o texto a ser traduzido")
        if text:
            return text
    except Exception as e:
        st.write(e)
        st.write("Erro ao ler o texto")


# criar função para retornar o diciônario com todos os idiomas disponíveis
def get_langs():
    try:
        # criar dicionario com os 20 principais idiomas disponíveis
        idiomas = {'Português': 'pt', 'Inglês': 'en', 'Espanhol': 'es', 'Francês': 'fr', 'Alemão': 'de',
                   'Italiano': 'it', 'Holandês': 'nl', 'Russo': 'ru', 'Japonês': 'ja', 'Chinês': 'zh-cn',
                   'Coreano': 'ko', 'Árabe': 'ar', 'Hindi': 'hi', 'Tailandês': 'th', 'Vietnamita': 'vi',
                   'Malaio': 'ms', 'Turco': 'tr', 'Polonês': 'pl', 'Sueco': 'sv', 'Norueguês': 'no'}
        # perguntar ao utilizador qual idioma ele deseja traduzir o texto
        lang = st.selectbox("Selecione o idioma para traduzir o texto", list(idiomas.keys()))
        # retornar o idioma valor do idioma selecionado
        return idiomas[lang]
    except Exception as e:
        st.write(e)
        st.write("Erro ao ler o idioma")


# traduzir o texto do português para o idioma selecionado
def translate_text(text, lang):
    try:
        translator = Translator()
        text = translator.translate(text, dest=lang)
        return text.text
    except Exception as e:
        st.write(e)
        st.write("Erro ao traduzir o texto")


# função para traduzir o texto sempre para o inglês
def traduzirParaIngles(texto):
    try:
        translator = Translator()
        texto = translator.translate(texto, dest="en")
        return texto.text
    except Exception as e:
        st.write(e)
        st.write("Erro ao traduzir o texto")


# funçao para stemizar o texto
def Stemize(text):
    try:
        stemmer = RSLPStemmer()
        text = [stemmer.stem(palavra) for palavra in text]
        return text
    except Exception as e:
        st.write(e)
        st.write("Erro ao stemizar o texto")


# função para tokenizar o texto
def Tokenize(text):
    try:
        text = word_tokenize(text)
        return text
    except Exception as e:
        st.write(e)
        st.write("Erro ao tokenizar o texto")
        
# remover stopwords do texto
def remove_stopwords(text):
    try:
        nltk.download('stopwords')
        stop_words = set(stopwords.words('português'))
        text = [palavra for palavra in text if palavra not in stop_words]
        return text
    except Exception as e:
        st.write(e)
        st.write("Erro ao remover as stopwords")

def tratar_texto(text):
    try:
        # traduzir o texto para o inglês
        text = traduzirParaIngles(text)
        # tokenizar o texto
        text = Tokenize(text)
        # stemizar o texto
        text = Stemize(text)
        # remover stopwords do texto
        text = remove_stopwords(text)
        return text
    except Exception as e:
        st.write(e)
        st.write("Erro ao tratar o texto")


# função para analisar sentimento do texto
def analisar_sentimento(text):
    try:
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
    except Exception as e:
        st.write(e)


def CriarDataFrameEmocoes(text):
    try:
        emotion = NRCLex(text)
        # vericar quais emoções estão presentes em emotion.raw_emotion_scores
        emocoes = emotion.raw_emotion_scores.keys()
        # criar um dicionário com as emoções e os seus valores
        emocoes_dict = {}
        for i in emocoes:
            emocoes_dict[i] = emotion.raw_emotion_scores[i]
        emocoes_tb = {k: v for k, v in emocoes_dict.items() if v != 0}
        # remover as chaver positivo e negativo do dicionário
        emocoes_tb.pop('positive')
        emocoes_tb.pop('negative')
        # criar um dataframe com as emoções e os seus valores
        df = pd.DataFrame(emocoes_tb.items(), columns=['Emoção', 'Valor'])
        # traduzir o nome das emoções para o português
        df['Emoção'] = df['Emoção'].replace(
            {'fear': 'Medo', 'anger': 'Raiva', 'anticipation': 'Antecipação', 'trust': 'Confiança',
             'surprise': 'Surpresa', 'sadness': 'Tristeza', 'disgust': 'Nojo', 'joy': 'Alegria'})
        return df
    except Exception as e:
        st.write(e)
        st.write("Erro ao criar o dataframe com as emoções")


def CriarDataFrameSentimentos(text):
    try:
        emotion = NRCLex(text)
        emocoes = emotion.raw_emotion_scores.keys()
        emocoes_dict = {}
        for i in emocoes:
            emocoes_dict[i] = emotion.raw_emotion_scores[i]
            # pegar somente as emoções positivas e negativas
        emocoes_tb = {k: v for k, v in emocoes_dict.items() if k == 'positive' or k == 'negative'}
        # criar um dataframe com as emoções e os seus valores
        df = pd.DataFrame(emocoes_tb.items(), columns=['Sentimento', 'Valor'])
        # traduzir o nome das emoções para o português
        df['Sentimento'] = df['Sentimento'].replace({'positive': 'Positivo', 'negative': 'Negativo'})
        return df
    except Exception as e:
        st.write(e)
        st.write("Erro ao criar o dataframe com os sentimentos")


# função para analisar emoções do texto
def analisar_emocoes(df):
    try:
        st.markdown(df.to_html(index=False), unsafe_allow_html=True)
        # mostra ‘top’ 3 emoções
        st.write("Top 3 emoções")
        st.write(df.sort_values(by=['Valor'], ascending=False).head(3))
        # mostra gráfico de barras
        fig = px.bar(df, x='Emoção', y='Valor', title='Emoções', color='Valor')
        st.plotly_chart(fig)
    except Exception as e:
        st.write(e)
        st.write("Erro ao analisar as emoções")


def analisar_sentimentos(df):
    try:
        st.markdown(df.to_html(index=False), unsafe_allow_html=True)
        # mostra gráfico de barras
        fig = px.bar(df, x='Sentimento', y='Valor', title='Sentimentos', color='Valor')
        st.plotly_chart(fig)
    except Exception as e:
        st.write(e)
        st.write("Erro ao analisar os sentimentos")


# criar função para detetar entidades
def detectar_entidades(text):
    try:
        nlp = spacy.load('pt_core_news_lg')
        # traduzir o texto para o inglês
        text = traduzirParaIngles(text)
        doc = nlp(text)
        detalhes_entidade = [(entidade, entidade.label_) for entidade in doc.ents]
        # criar um dataframe com as entidades e os seus detalhes
        df = pd.DataFrame(detalhes_entidade, columns=['Entidade', 'Detalhes'])
        # melhorar a visualização do dataframe
        df['Detalhes'] = df['Detalhes'].replace({'CARDINAL': 'Cardinal', 'DATE': 'Data', 'EVENT': 'Evento',
                                                 'FAC': 'Local', 'GPE': 'País', 'LANGUAGE': 'Língua',
                                                 'LAW': 'Lei', 'LOC': 'Local', 'MONEY': 'Dinheiro', 'ORDINAL':
                                                     'Ordinal', 'PERCENT': 'Percentual', 'PERSON': 'Pessoa',
                                                 'PRODUCT': 'Produto', 'QUANTITY': 'Quantidade', 'TIME': 'Tempo',
                                                 'WORK_OF_ART': 'Obra', 'MISC': 'Misto', 'PER': 'Pessoa',
                                                 'NORP': 'Grupo', 'ORG': 'Organização'})

        df = df.sort_values(by=['Entidade'])
        # traduzir o nome as entidades para o português
        tralator = Translator()
        df['Entidade'] = df['Entidade'].apply(lambda x: tralator.translate(x, dest='pt').text)
        # criar grafico de barras contatando os detalhes
        cotador = Counter(df['Detalhes'])
        df_cotador = pd.DataFrame(cotador.items(), columns=['Detalhes', 'Quantidade'])
        # organizar o dataframe por quantidade
        df_cotador = df_cotador.sort_values(by=['Quantidade'], ascending=False)
        fig = px.bar(df_cotador, x='Detalhes', y='Quantidade', title='Detalhes das entidades', color='Quantidade')
        st.plotly_chart(fig)
        return df
    except Exception as e:
        st.write(e)
        st.write("Não foi possível detectar entidades")


def analisar_gramatical(text):
    try:
        nlp = spacy.load('pt_core_news_lg')
        doc = nlp(text)
        gramat = [(token.orth_, token.pos_) for token in doc]
        # criar um dataframe com as entidades e os seus detalhes
        df = pd.DataFrame(gramat, columns=['Palavra', 'Detalhes'])
        # melhorar a visualização do dataframe
        df['Detalhes'] = df['Detalhes'].replace(
            {'ADJ': 'Adjetivo', 'ADP': 'Adposição', 'ADV': 'Advérbio', 'AUX': 'Auxiliar',
             'CCONJ': 'Conjunção coordenativa', 'DET': 'Determinante',
             'INTJ': 'Interjeição', 'NOUN': 'Substantivo', 'NUM': 'Numeral',
             'PART': 'Partícula', 'PRON': 'Pronome', 'PROPN': 'Nome próprio',
             'PUNCT': 'Pontuação', 'SCONJ': 'Conjunção subordinativa', 'SYM': 'Símbolo',
             'VERB': 'Verbo', 'X': 'Outro'})
        # remover os duplicados do dataframe da coluna palavra
        df = df.drop_duplicates(subset=['Palavra'])
        contador = Counter(df['Detalhes'])
        df_contador = pd.DataFrame(contador.items(), columns=['Detalhes', 'Quantidade'])
        # ordenar dataframe pela quantidade
        df_contador = df_contador.sort_values(by=['Quantidade'], ascending=False)
        fig = px.bar(df_contador, x='Detalhes', y='Quantidade', title='Detalhes gramaticais', color='Quantidade')
        st.plotly_chart(fig)
        return df
    except Exception as e:
        st.write(e)
        st.write("Não foi possível analisar o texto")


# função para indentificar idiomas presentes no texto usando o pacote langdetect
def detectar_idioma(text):
    try:
        DetectorFactory.seed = 0
        idiomas = detect_langs(text)
        # criar um dicionário com os idiomas e as suas probabilidades
        idiomas_dict = {}
        for i in idiomas:
            idiomas_dict[i.lang] = i.prob
        # criar um dataframe com os idiomas, as suas probabilidade e porcentagem
        df = pd.DataFrame(idiomas_dict.items(), columns=['Idioma', 'Probabilidade'])
        df['Porcentagem'] = df['Probabilidade'].apply(lambda x: round(x * 100, 2))
        df['Porcentagem'] = df['Porcentagem'].astype(str) + '%'
        return df
    except Exception as e:
        st.write(e)
        st.write("Não foi possível identificar o idioma...")


def analisar_idioma(text):
    try:
        translator = Translator()
        # criar dataframe com as frases do texto
        df = pd.DataFrame(text.split('.'), columns=['Frases'])
        # criar coluna com o idioma da frase
        df['Idioma'] = df['Frases'].apply(lambda x: translator.detect(x).lang)
        return df
    except Exception as e:
        st.write(e)
        st.write("Não foi possível identificar o idioma")


def main():
    try:
        # criar interface com menuS
        menu = ["Home", "Analisar Texto", "Analise de Sentimento", "Analise de Emoções",
                "Analise de Sentimentos Secundários", "Tradutor", "Detecção de Entidades",
                "Análise Gramatical", "Detectar Linguagem", "Detectar Idioma"]
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
                st.write(analisar_sentimento(text))
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
            st.subheader("Tradutor")
            text = st.text_area("Digite o texto")
            lang = get_langs()
            # traduzir texto
            if st.button("Traduzir"):
                traducao = translate_text(text, lang)
                st.write(traducao)
        elif choice == "Detecção de Entidades":
            st.subheader("Detecção de Entidades")
            text = st.text_area("Digite o texto")
            if st.button("Detectar"):
                df = detectar_entidades(text)
                st.markdown(df.to_html(index=False), unsafe_allow_html=True)
        elif choice == "Análise Gramatical":
            st.subheader("Análise Gramatical")
            text = st.text_area("Digite o texto")
            if st.button("Analisar"):
                df = analisar_gramatical(text)
                st.markdown(df.to_html(index=False), unsafe_allow_html=True)
        elif choice == "Detectar Linguagem":
            st.subheader("Detectar Linguagem")
            text = st.text_area("Digite o texto")
            if st.button("Detectar"):
                df = detectar_idioma(text)
                st.markdown(df.to_html(index=False), unsafe_allow_html=True)
        elif choice == "Detectar Idioma":
            st.subheader("Detectar Idioma")
            text = st.text_area("Digite o texto")
            if st.button("Detectar"):
                df = analisar_idioma(text)
                st.dataframe(df)

    except Exception as e:
        st.write(e)
        st.write("Não foi possível analisar o texto")


if __name__ == "__main__":
    main()