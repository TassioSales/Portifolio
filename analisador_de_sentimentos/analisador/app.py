#Criação de programa para analisar sentimentos de frases e palavras digitadas pelo usuário
#Importando bibliotecasi
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator

#criar função para pedir frase ao usuário
def pedir_frase():
    frase = input('Digite uma frase: ')
    return frase

#criar função para traduzir frase do português para o inglês
def traduzir_frase(frase):
    tradutor = Translator()
    frase_traduzida = tradutor.translate(frase, dest='en')
    return frase_traduzida.text

#criar função para analisar a frase_traduzida
def analisar_sentimento(frase_traduzida):
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

#criar função para imprimir o resultado
def imprimir_resultado(dicionario):
    print("Frase sem tradução:", dicionario['frase'])
    print('Frase: ', dicionario['frase'])
    print('Sentimento: ', dicionario['sentimento'])
    print('Maior valor: ', dicionario['maior_valor'])
    print('Dicionario: ', dicionario['ss'])

def main():
    frase = pedir_frase()
    frase_traduzida = traduzir_frase(frase)
    dicionario = analisar_sentimento(frase_traduzida)
    imprimir_resultado(dicionario)


if __name__ == '__main__':
    main()
