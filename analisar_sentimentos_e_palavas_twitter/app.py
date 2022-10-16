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
import streamlit as st

#chaves de acesso
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

# função para pesquisar os tweets usando o StreamlitAPIException
def pegar_tweets():
    """[summary]
    Função para pesquisar os tweets
    Returns:
        [type]: [description]
    :param: tema: tema que desejado
    :param: numero: número de tweets que desejada
    :param: tweets: lista de tweets
    """
    tema = perguntar()
    numero = perguntar_numero()
    autenticar()
    tweets = tw.Cursor(api.search, q=tema, lang='pt', tweet_mode='extended').items(int(numero))
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

#mostra os tweets coletados
def main():
    """[summary]
    Mostra os tweets coletados
    """
    st.title("Coletor de tweets")
    st.subheader("Coletor de tweets")
    df = realizar_limpeza()
    st.write(df)
    
if __name__ == '__main__':
    main()  


        