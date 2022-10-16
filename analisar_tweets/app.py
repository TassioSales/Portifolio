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

