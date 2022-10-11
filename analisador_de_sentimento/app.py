#criar progrma para analisar sentimento de frases digitas pelo usuario

from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st
import openai
import tracebac


openai.api_key = st.secrets['api']

#função para pedir frase ao usuario
def get_frase():
    """
    Função para pedir frase ao usuario
    :return: frase digitada pelo usuario
    """
    try:
        frase = st.text_input("Digite uma frase para analisar o sentimento")
        return frase
    except:
        st.error(traceback.format_exc())

#função para traduzir frase
def traduzir_frase(frase):
    """
    Função para traduzir frase
    :param frase: frase digitada pelo usuario
    :return: frase traduzida"""
    try:
        traducao = TextBlob(frase)
        traducao = traducao.translate(to='en')
        return traducao
    except:
        st.error(traceback.format_exc())

#função para analisar sentimento
def analisar_sentimento(frase_traduzida):
    """
    Função para analisar sentimentos
    :param frase_traduzida: frase traduzida
    :return: sentimento da frase_traduzida
    """
    # criar objeto
    sid = SentimentIntensityAnalyzer()
    # criar dicionario
    ss = sid.polarity_scores(frase_traduzida)
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


#funçao para mostra resultado
def mostra_resultado(dicionario):
    """
    Função para mostrar resultado
    :param dicionario: dicionario com os dados
    :return: None
    """
    # criar variavel para armazenar a frase digitada pelo usuario
    frase = dicionario['frase']
    # criar variavel para armazenar o sentimento
    sentimento = dicionario['sentimento']
    # criar variavel para armazenar o maior valor
    maior_valor = dicionario['maior_valor']
    # criar variavel para armazenar o maior
    maior = dicionario['maior']
    # criar variavel para armazenar o dicionario
    ss = dicionario['ss']
    # criar variavel para armazenar o objeto
    sid = dicionario['sid']
    # criar condicao para mostrar resultado
    if frase != '':
        st.write(f'Frase: {frase}')
        st.write(f'Sentimento: {sentimento}')
        st.write(f'Maior valor: {maior_valor}')
        st.write(f'Maior: {maior}')
        st.write(f'Dicionario: {ss}')
        st.write(f'Objeto: {sid}')

def main():
    """
    Função principal
    :return: None
    """
    # pedir frase ao usuario
    frase = get_frase()
    # traduzir frase
    frase_traduzida = traduzir_frase(frase)
    # analisar sentimento
    dicionario = analisar_sentimento(frase_traduzida)
    # mostrar resultado
    mostra_resultado(dicionario)

if __name__ == '__main__':
    main()



