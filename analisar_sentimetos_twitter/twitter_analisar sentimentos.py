# entrando no twitter api
# imports necessários
import tweepy
from textblob import TextBlob


# funcao para conectar com a api do twitter API v2
def conectar_api_v2():




# funcao para conectar com a api do twitter
def conectar_api():
    global API
    consumer_key = '8UwtArZ5juvtBFG1Mt4CgAouE'
    consumer_secret = 'uLjfL2KU4fnhRCew4Lt7o8Hko0QCUjq6tRXzSaBEGlgen8ov8X'
    aceess_token = '1579911754620043265-78MGdZ8Q1KuF0ZFCjkWMOPArYGvZ53'
    access_token_secret = 'IuM2PzD7AE79qermPDLsuNI7SxFS0L85KdHObJhyGG1U1'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(aceess_token, access_token_secret)

    API = tweepy.API(auth)

    return API


# criar uma função para perguntar sobre o assunto que queremos analisar
def get_tema():
    tema = input("Digite o tema que deseja analisar: ")
    return tema


# criar uma função para perguntar o numero de tweets que queremos analisar
def get_numero_tweets():
    numero_tweets = int(input("Digite o numero de tweets que deseja analisar: "))
    return numero_tweets


# criar uma função para perguntar o idioma que queremos analisar
def get_idioma():
    # menu de idiomas
    print("1 - Português")
    print("2 - Inglês")
    print("3 - Espanhol")

    idioma = int(input("Digite o idioma que deseja analisar: "))
    if idioma == 1:
        idioma = "pt"
    elif idioma == 2:
        idioma = "en"
    elif idioma == 3:
        idioma = "es"
    else:
        print("Idioma não encontrado")
    return idioma


# criar uma função para pegar os tweets
def get_tweets():
    tema = get_tema()
    numero_tweets = get_numero_tweets()
    idioma = get_idioma()

    tw = API.search_tweets(tema, count=numero_tweets, lang=idioma)
    return tw


# mostrar os tweets
def mostrar_tweets(tweets):
    for tweet in tweets:
        print(tweet.text)
        print("")


if __name__ == "__main__":
    conectar_api()
    tweets = get_tweets()
    mostrar_tweets(tweets)
