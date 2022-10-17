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
    api = autenticar()
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
        #remeover links usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"http\S+", "", x))
        #remover @ usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"@\S+", "", x))
        #remover # usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"#\S+", "", x))
        #remover emojis usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"\\U\S+", "", x))
        #remover pontuação usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"[^\w\s]", "", x))
        #remover números usando regex usando a função lambda 
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"\d+", "", x))
        #remover espaços em branco usando regex usando a função lambda 
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"\s+", " ", x))
        #remover palavras com menos de 3 letras usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"\b\w{1,3}\b", "", x))
        #remover palavras com mais de 15 letras usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"\b\w{15,}\b", "", x))
        #remover RT usando regex usando a função lambda
        df['Tweets'] = df['Tweets'].apply(lambda x: re.sub(r"RT", "", x))
        #salvar os tweets limpos em um arquivo csv
        df.to_csv(path_or_buf='tweets_limpos.csv', index=False)
        ##ler o arquivo csv e mostrar o dataframe
        tweets_limpos = pd.read_csv('tweets_limpos.csv')
        #criar botao para mostrar os tweets limpos
        mostrar_tweets_limpos = st.button("Mostrar Tweets Limpos")
        if mostrar_tweets_limpos:
            st.table(tweets_limpos)
    except Exception as e:
        st.write(e)
        
#percorre a coluna de tweets e mostra se o tweet é positivo, negativo ou neutro
def analisar_sentimento_open(df):
    """[summary]
    Realiza a análise de sentimento dos tweets
    Returns: string
    :param: df: dataframe com os tweets
    :param: df['Tweets']: coluna com os tweets
    :param: df['Tweets']: coluna com os tweets limpos
    :param: df['Sentimento']: coluna com o sentimento do tweet
    """
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
        #titulo

    if st.button("Mostrar Sentimento"):
        df['Sentimento'] = response['choices'][0]['text']
        st.table(df)
    else:
        st.write("Clique no botão para mostrar o sentimento do tweet")
    #salvar os tweets com o sentimento em um arquivo csv
    df.to_csv(path_or_buf='tweets_sentimento_openia.csv', index=False)
    
def mostrar_grafico_openia(df):
    #mostrar o gráfico de pizza com a quantidade de tweets positivos, negativos e neutros
    fig = go.Figure()
    #criar botao para mostrar o grafico de pizza com a porcentagem de tweets positivos, negativos e neutros
    if st.button("Mostrar Gráfico de Pizza"):
        fig.add_trace(go.Pie(labels=df['Sentimento'].value_counts().index, values=df['Sentimento'].value_counts().values))
        st.plotly_chart(fig)
    #criar botao para mostrar o grafico de barras com a quantidade de tweets positivos, negativos e neutros
    if st.button("Mostrar Gráfico de Barras"):
        fig.add_trace(go.Bar(x=df['Sentimento'].value_counts().index, y=df['Sentimento'].value_counts().values))
        st.plotly_chart(fig)
    
    

    
            
   
        
#função principal
def main():
    #criar o menu
    menu = ["Home", "Pesquisar Tweets", "Limpar Tweets", "Analisar Sentimento OpenAI", "Mostrar Gráfico OpenAI"]
    #criar o selectbox
    choice = st.sidebar.selectbox("Menu", menu)
    #selecionar a opção do menu
    if choice == "Home":
        st.title("Análise de Sentimento de Tweets")
        st.subheader("Análise de Sentimento de Tweets com OpenAI")
    if choice == "Pesquisar Tweets":
        pegar_tweets()
    if choice == "Limpar Tweets":
        limpar_tweets() 
    if choice == "Analisar Sentimento OpenAI":
        #ler o arquivo csv e mostrar o dataframe
        df = pd.read_csv('tweets_limpos.csv')
        analisar_sentimento_open(df)
    if choice == "Mostrar Gráfico OpenAI":
        df = pd.read_csv('tweets_sentimento_openia.csv')
        mostrar_grafico_openia(df)

                
if __name__ == '__main__':
    main()


        