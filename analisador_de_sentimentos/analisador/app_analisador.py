#Criação de programa para analisar sentimentos de frases e palavras digitadas pelo usuário
#Importando bibliotecasi
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator
import streamlit as st


import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = "q=Hello%2C%20world!&target=es&source=en"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "465714bfb2msh0bd0529770d8fa7p1772afjsn14f9735e14e9",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

#criar função para pedir frase ao usuário
def pedir_frase():
    frase = st.text_input('Digite uma frase:')
    return frase

#criar função para analisar a frase_traduzida
def analisar_sentimento(frase):
    # criar objeto
    sid = SentimentIntensityAnalyzer()
    # criar dicionario
    ss = sid.polarity_scores(frase)
    # criar variavel para armazenar a chave com maior valor
    maior = max(ss, key=ss.get)
    # criar variavel para armazenar o valor da chave com maior valor
    maior_valor = ss[maior]
    # criar variavel para armazenar o sentimento
    sentimento = ''
    # criar condicao para definir o sentimento
    if maior_valor == 0.0:
        sentimento = 'neutro'
    elif maior_valor > 0.0:
        sentimento = 'positivo'
    elif maior_valor < 0.0:
        sentimento = 'negativo'
    # criar variavel para armazenar a frase digitada pelo usuario
    frase = frase_traduzida
    # criar variavel para armazenar o sentimento
    sentimento = sentimento
    # criar variavel para armazenar o maior valor
    maior_valor = maior_valor
    # criar variavel para armazenar o maior
    maior = maior
    # criar variavel para armazenar o dicionario
    ss = ss
    # criar variavel para armazenar o objeto
    sid = sid
    # criar dicionario
    dicionario = {'frase': frase, 'sentimento': sentimento, 'maior_valor': maior_valor, 'maior': maior, 'ss': ss,
                  'sid': sid}
    # retornar dicionario
    return dicionario

#mostra o resultado
def imprimir_resultado(dicionario):
    st.write('Frase digitada:', dicionario['frase'])
    st.write('Sentimento:', dicionario['sentimento'])
    st.write('Maior valor:', dicionario['maior_valor'])
    st.write('Maior:', dicionario['maior'])
    st.write('Dicionario:', dicionario['ss'])
    st.write('Objeto:', dicionario['sid'])

def main():
    # criar variavel para armazenar a frase digitada pelo usuario
    frase = pedir_frase()
    # criar objeto
    translator = Translator()
    # criar variavel para armazenar a frase traduzida
    frase_traduzida = translator.translate(frase, dest='en').text
    # criar variavel para armazenar o dicionario
    dicionario = analisar_sentimento(frase_traduzida)
    # imprimir resultado
    imprimir_resultado(dicionario)

if __name__ == '__main__':
    main()