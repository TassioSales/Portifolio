#Bibliotecas
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
import Streamlit as st

#chaves de acesso
consumer_key = st.secrets["consumer_key"]
consumer_secret = st.secrets["consumer_secret"]
access_token = st.secrets["access_token"]
access_token_secret = st.secrets["access_token_secret"]
openai.api_key = st.secrets["api"]

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

# função para perguntar ao usuário o tema que deseja
def perguntar():
    """[summary]
    Função para perguntar ao usuário o tema que deseja
    Returns:
        [type]: string
    :param: tema: tema que desejado
    """
    tema = st.text_input("Digite o tema que deseja pesquisar")
    return tema

# função pegunta ao usuário o número de tweets que deseja
def perguntar_numero():
    """[summary]
    Função para perguntar ao usuário o número de tweets que deseja
    Returns:
        [type]: string
    :param: numero: número de tweets que desejada
    """
    numero = st.text_input("Digite o número de tweets que deseja")
    return numero

# função para pesquisar os tweets
def pegar_tweets():
    """[summary]
    Função para pesquisar os tweets
    Returns: string
    :param: tema: tema que desejado
    :param: numero: número de tweets que desejada
    :param: tweets: lista de tweets
    """
    tema = perguntar()
    numero = perguntar_numero()
    autenticar()
    tweets = tw.Cursor(api.search_tweets, q=tema, lang='pt', tweet_mode='extended').items(int(numero))
    #ignorar os retweets
    tweets = [tweet for tweet in tweets if not tweet.retweeted]
    #ignorar os tweets que não tem texto
    tweets = [tweet for tweet in tweets if tweet.full_text]
    #ignnoras tweets repetidos
    tweets = list(set(tweets))
    return tweets

#função para gerar um data frame com os tweets
def gerar_dataframe():
    """[summary]
    Retorna um dataframe com os tweets
    :param: tweets: lista de tweets
    :param: df: dataframe com os tweets
    :param: df['Tweets']: coluna com os tweets
    """
    tweets = pegar_tweets()
    df = pd.DataFrame(data=[tweet.full_text for tweet in tweets], columns=['Tweets'])
    return df

def realizar_limpeza():
    """[summary]
    Realiza a limpeza dos tweets
    Returns: string
    :param: df: dataframe com os tweets
    :param: df['Tweets']: coluna com os tweets
    :param: df['Tweets']: coluna com os tweets limpos
    """
    df = gerar_dataframe()
    df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r'http\S+', '', x))
    df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r'RT', '', x))
    df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r'@[A-Za-z0-9]+', '', x))
    # remove pontuação
    df['Tweets'] = df['Tweets'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
    # remove números
    df['Tweets'] = df['Tweets'].apply(lambda x: x.translate(str.maketrans('', '', string.digits)))
    # remove espaços em branco
    df['Tweets'] = df['Tweets'].apply(lambda x: x.strip())
    # remove palavras com menos de 3 caracteres
    df['Tweets'] = df['Tweets'].apply(lambda x: ' '.join([w for w in x.split() if len(w) > 3]))
    # remove stopwords
    stop_words = nltk.corpus.stopwords.words('portuguese')
    # remove palavras com menos de 3 caracteres
    df['Tweets'] = df['Tweets'].apply(lambda x: ' '.join([w for w in x.split() if w not in stop_words]))
    #remove palavras com mais de 15 caracteres
    df['Tweets'] = df['Tweets'].apply(lambda x: ' '.join([w for w in x.split() if len(w) < 15]))
    #remover emojis
    df['Tweets'] = df['Tweets'].apply(lambda x: x.encode('ascii', 'ignore').decode('ascii'))
    return df

#gerar database
dataframe = realizar_limpeza()


#percorre a coluna de tweets e mostra se o tweet é positivo, negativo ou neutro
def analisar_sentimento_open(df):
    for tweet in df['Tweets']:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Decida se o sentimento de um Tweet é Positivo, Neutro ou Negativo.\n\nTweet: \"{tweet}\"\nSentimento:",
            temperature=0.9,
            max_tokens=5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
        )
        print(f"Tweet: {tweet}")
        print("Sentimento: {}".format(response.choices[0].text))
        print("")