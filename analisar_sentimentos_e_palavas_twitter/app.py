# Bibliotecas
import os
import openai
import tweepy as tw
import re
import string
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from collections import Counter
import streamlit as st
import plotly.graph_objects as go
from googletrans import Translator
from stop_word import stop_palavras

# chaves de acesso
consumer_key = st.secrets['ck']
consumer_secret = st.secrets['cs']
access_token = st.secrets['act']
access_token_secret = st.secrets['ats']
openai.api_key = st.secrets['api']


# função para autenticar twitter
def autenticar():
    """[summary]
    Função para autenticar o twitter
    Returns:
        [type]: [description]
    :param: auth: autenticação do twitter
    """
    global api
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    return api


# função para pesquisar os tweets usando o StreamlitAPIException
def pesquisar_tweets():
    api = autenticar()
    try:
        # perguntar ao usaurio o tema dos tweets
        tema = st.text_input("Digite o tema dos tweets que deseja pesquisar: ")
        # perquentar ao usuario a quantidade de tweets
        quantidade = st.number_input("Digite a quantidade de tweets que deseja pesquisar: ")
        # pesquisar os tweets
        tweets = tw.Cursor(api.search_tweets, q=tema, lang="pt").items(quantidade)
        # salvar os tweets em uma lista em arquivo csv com a coluna Tweets
        tweets = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        # salvar os tweets em um arquivo csv
        tweets.to_csv(path_or_buf='tweets.csv', index=False)
        # ler o arquivo csv e mostrar o dataframe
        df = pd.read_csv('tweets.csv')
        # criar botao para mostrar os tweets
        mostrar_tweets = st.button("Mostrar Tweets")
        if mostrar_tweets:
            st.table(df)
    except Exception as e:
        st.write(e)


# função com botao para limpar tweets do arquivo csv e mostra a tabela com os tweets limpos
def limpar_tweets():
    try:
        df = pd.read_csv('tweets.csv')
        # remeover links usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"http\S+", "", x))
        # remover @ usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"@\S+", "", x))
        # remover # usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"#\S+", "", x))
        # remover emojis usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"\\U\S+", "", x))
        # remover pontuação usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"[^\w\s]", "", x))
        # remover números usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"\d+", "", x))
        # remover espaços em branco usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"\s+", " ", x))
        # remover palavras com menos de 3 letras usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"\b\w{1,3}\b", "", x))
        # remover palavras com mais de 15 letras usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"\b\w{15,}\b", "", x))
        # remover RT usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"RT", "", x))
        # salvar os tweets limpos em um arquivo csv
        df.to_csv(path_or_buf='tweets_limpos.csv', index=False)
        ##ler o arquivo csv e mostrar o dataframe
        tweets_limpos = pd.read_csv('tweets_limpos.csv')
        # criar botao para mostrar os tweets limpos
        mostrar_tweets_limpos = st.button("Mostrar Tweets Limpos")
        if mostrar_tweets_limpos:
            st.table(tweets_limpos)
    except Exception as e:
        st.write(e)
        st.write(e.__class__())


def analisar_sentimentos_nltk(df):
    # criar coluna Traducao no dataframe
    df['Traducao'] = ""
    df['Sentimento_completo'] = ""
    df['Sentimento'] = ""
    try:
        for tweet in df['Tweets']:
            translator = Translator()
            traduzir = translator.translate(tweet, dest='en')
            # colocar traducao para cada tweet na coluna traducao
            df['Traducao'].loc[df['Tweets'] == tweet] = traduzir.text
        for tweet in df['Traducao']:
            sid = SentimentIntensityAnalyzer()
            ss = sid.polarity_scores(tweet)
            for k in sorted(ss):
                if k == 'compound':
                    df['Sentimento_completo'].loc[df['Traducao'] == tweet] = ss[k]
        for tweet in df['Sentimento_completo']:
            if tweet > 0:
                df['Sentimento'].loc[df['Sentimento_completo'] == tweet] = 'Positivo'
            if tweet < 0:
                df['Sentimento'].loc[df['Sentimento_completo'] == tweet] = 'Negativo'
            if tweet == 0:
                df['Sentimento'].loc[df['Sentimento_completo'] == tweet] = 'Neutro'
        if st.button("Mostrar Sentimento"):
            st.table(df)
        else:
            st.write("Clique no botão para mostrar o sentimento do tweet")
        # salvar os tweets com o sentimento em um arquivo csv
        df.to_csv(path_or_buf='tweets_sentimento_nltk.csv', index=False)
    except Exception as e:
        st.write(e)
        st.write(e.__class__())


def analisar_sentimentos_textblob(df):
    # criar coluna Traducao no dataframe
    df['Traducao'] = ""
    df['Sentimento_completo'] = ""
    df['Sentimento'] = ""
    try:
        for tweet in df['Tweets']:
            translator = Translator()
            traduzir = translator.translate(tweet, dest='en')
            # colocar traducao para cada tweet na coluna traducao
            df['Traducao'].loc[df['Tweets'] == tweet] = traduzir.text
        for tweet in df['Traducao']:
            traducao = TextBlob(tweet)
            df['Sentimento_completo'].loc[df['Traducao'] == tweet] = traducao.sentiment.polarity
        for tweet in df['Sentimento_completo']:
            if tweet > 0:
                df['Sentimento'].loc[df['Sentimento_completo'] == tweet] = 'Positivo'
            if tweet < 0:
                df['Sentimento'].loc[df['Sentimento_completo'] == tweet] = 'Negativo'
            if tweet == 0:
                df['Sentimento'].loc[df['Sentimento_completo'] == tweet] = 'Neutro'
        if st.button("Mostrar Sentimento"):
            st.table(df)
        else:
            st.write("Clique no botão para mostrar o sentimento do tweet")
        # salvar os tweets com o sentimento em um arquivo csv
        df.to_csv(path_or_buf='tweets_sentimento_textblob.csv', index=False)
    except Exception as e:
        st.write(e)
        st.write(e.__class__())


# criar função para criar grafico de barras
def grafico_barras():
    try:
        if st.button('Grafico NLTK'):
            # ler o arquivo csv com os tweets e o sentimento
            df = pd.read_csv('tweets_sentimento_nltk.csv')
            # criar um dataframe com a coluna Sentimento
            df_sentimento = df['Sentimento']
            # criar um grafico de barras com a contagem de cada sentimento
            st.bar_chart(df_sentimento.value_counts())
            string = "O gráfico acima mostra a quantidade de tweets positivos, negativos e neutros."
            st.write(string)
        if st.button('Grafico TextBlob'):
            # ler o arquivo csv com os tweets e o sentimento
            df = pd.read_csv('tweets_sentimento_textblob.csv')
            # criar um dataframe com a coluna Sentimento
            df_sentimento = df['Sentimento']
            # criar um grafico de barras com a contagem de cada sentimento
            st.bar_chart(df_sentimento.value_counts())
            string = "O gráfico acima mostra a quantidade de tweets positivos, negativos e neutros."
            st.write(string)
    except Exception as e:
        st.write(e)
        st.write(e.__class__())


# criar função para criar grafico de pizza
def grafico_pizza():
    try:
        if st.button('Grafico NLTK'):
            # ler o arquivo csv com os tweets e o sentimento
            df = pd.read_csv('tweets_sentimento_nltk.csv')
            # criar um dataframe com a coluna Sentimento
            df_sentimento = df['Sentimento']
            # criar um grafico de pizza com a contagem de cada sentimento
            fig = go.Figure(
                data=[go.Pie(labels=df_sentimento.value_counts().index, values=df_sentimento.value_counts().values)])
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(title_text="Sentimento dos Tweets NTL", title_x=0.5, title_font_size=20, autosize=True,
                              width=500, height=500)
            st.plotly_chart(fig)
            string = "O gráfico acima mostra a quantidade de tweets positivos, negativos e neutros."
            st.write(string)
        if st.button('Grafico TextBlob'):
            # ler o arquivo csv com os tweets e o sentimento
            df = pd.read_csv('tweets_sentimento_textblob.csv')
            # criar um dataframe com a coluna Sentimento
            df_sentimento = df['Sentimento']
            # Plotar grafico de pizza usando plotly.graph_objects
            fig = go.Figure(
                data=[go.Pie(labels=df_sentimento.value_counts().index, values=df_sentimento.value_counts().values)])
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(title_text="Sentimento dos Tweets TextBlob", title_x=0.5, title_font_size=20,
                              autosize=True, width=500, height=500)
            # mostra o grafico:
            st.plotly_chart(fig)
            string = "O gráfico acima mostra a quantidade de tweets positivos, negativos e neutros."
            st.write(string)
    except Exception as e:
        st.write(e)
        st.write(e.__class__())


def wordcloud(df):
    try:
        palavras = ''
        # criar lista com stop words
        stop = stop_palavras
        for tweet in df['Tweets']:
            palavras += tweet
            # remove palavras com menos de 3 caracteres
            palavras = re.sub(r'\W*\b\w{1,3}\b', '', palavras)
            # remover palavras com mais de 15 caracteres
            palavras = ' '.join([w for w in palavras.split() if len(w) < 15])
            # remover palavras repetidas
            palavras = ' '.join(set(palavras.split()))
            # remover stopwords caso ele exista nas palavras
            palavras = ' '.join(set(palavras.split()) - set(stop))
            # criar uma wordclod com as palavras mais usadas
        wordcloud = WordCloud(width=800, height=800,
                              background_color='white',
                              min_font_size=10).generate(palavras)
        # plotar a wordclod
        plt.figure(figsize=(8, 8), facecolor=None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)
        plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    except Exception as e:
        st.write(e)
        st.write(e.__class__())


# criar função principal
def main():
    # criar um menu com as opções
    menu = ["Home", "Pesquisar Tweets", "Limpar Tweets", "WordCloud", "Analise de Sentimento NLTK",
            "Analise de Sentimento TextBlob", "Grafico de Barras", "Grafico de Pizza", "WordCloud", "tutorial"]
    opcoes = st.sidebar.selectbox("Menu", menu)
    # criar um titulo
    st.title("Análise de Sentimento de Tweets")
    if opcoes == "Home":
        # criar um subtitulo
        st.subheader("Análise de Sentimento de Tweets")
        # criar um texto
        st.text("Escolha uma opção no menu ao lado")
    elif opcoes == "Pesquisar Tweets":
        # criar um subtitulo
        st.subheader("Pesquisar Tweets")
        # criar um texto
        st.text("Pesquise por tweets")
        # criar um campo para digitar o texto
        texto = st.text_input("Digite o texto")
        # criar um botão para pesquisar
        if st.button("Pesquisar"):
            # chamar a função para pesquisar tweets
            pesquisar_tweets()
    elif opcoes == "Limpar Tweets":
        # criar um subtitulo
        st.subheader("Limpar Tweets")
        # criar um texto
        st.text("Limpar tweets")
        # criar um botão para limpar tweets
        if st.button("Limpar Tweets"):
            # chamar a função para limpar tweets
            limpar_tweets()




if __name__ == '__main__':
    main()
