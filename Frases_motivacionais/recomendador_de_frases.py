#criaçao de um programa que recomenda frases motivacionais para o usuario usar em seu dia a dia
#usar o streamlit para criar a interface

import streamlit as st
import pandas as pd
import random


#busca frase motivacional
#importa dataframe online
df = pd.read_csv('https://raw.githubusercontent.com/TassioSales/Portifolio/main/Frases_motivacionais/frases_motivacionaiss.csv', sep=';', encoding='utf-8')

#cria uma lista com as frases
frases = df['Frase_motivacionais'].tolist()

#criar uma função para gerar uma frase aleatoria
def gerar_frase():
    return random.choice(frases)

#cria a interface
st.title('Gerador de frases motivacionais')
st.write('Clique no botão abaixo para gerar uma frase motivacional')
#cria um botão
if st.button('Gerar frase'):
    st.write(gerar_frase())
    #mostra um emoji aleatorio
    st.write(':smile:')







