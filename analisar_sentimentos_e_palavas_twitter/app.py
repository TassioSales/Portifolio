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

# função para pesquisar os tweets usando o StreamlitAPIException
def pegar_tweets():
    try:
        #perguntar ao usaurio o tema dos tweets
        tema = st.text_input("Digite o tema dos tweets que deseja pesquisar: ")
        #perquentar ao usuario a quantidade de tweets
        quantidade =st.number_input("Digite a quantidade de tweets que deseja pesquisar: ")
        #pesquisar os tweets
        tweets = tw.Cursor(api.search_tweets, q=tema, lang="pt").items(quantidade)
        #salvar os tweets em uma lista em arquivo csv com a coluna Tweets
        tweets = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        #salvar os tweets em um arquivo csv
        tweets.to_csv(path_or_buf='tweets.csv', index=False)
        #ler o arquivo csv e mostrar o dataframe
        df = pd.read_csv('tweets.csv')
        #criar botao para mostrar os tweets
        mostrar_tweets = st.button("Mostrar Tweets")
        if mostrar_tweets:
            st.table(df)
    except Exception as e:
        st.write(e)
        
#função com botao para limpar tweets do arquivo csv e mostra a tabela com os tweets limpos
def limpar_tweets():
    try:
        df = pd.read_csv('tweets.csv')
        #remover #
        df['Tweets'] = df['Tweets'].str.replace('#', '')
        #remover numeros
        df['Tweets'] = df['Tweets'].str.replace('\d+', '')
        #remover links
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r'http\S+', '', x))
        #remover @
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r'RT', '', x))
        #remover @
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
        df = pd.read_csv('tweets_limpos.csv')
        #Criar botão para limpar os tweets
        limpar_tweets = st.button("Limpar Tweets")
        if limpar_tweets:
            st.table(df)
    except Exception as e:
        st.write(e)
        
#função principal
def main():
    autenticar()
    pegar_tweets()
    limpar_tweets()
                
if __name__ == '__main__':
    main()


        