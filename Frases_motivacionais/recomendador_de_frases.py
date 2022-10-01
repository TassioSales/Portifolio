#criaçao de um programa que recomenda frases motivacionais para o usuario usar em seu dia a dia
#usar o streamlit para criar a interface

import streamlit as st
import pandas as pd
import emoji


#busca frase motivacional
#importa dataframe online
df = pd.read_csv('https://raw.githubusercontent.com/TassioSales/Portifolio/main/Frases_motivacionais/frases_motivacionaiss.csv', sep=';', encoding='utf-8')

#cria uma lista com as frases
frases = df['Frase_motivacionais'].tolist()

#recomenda uma frase aleatoria
import random
frase = random.choice(frases)
#mostra um emoji aleatorio
emoji = random.choice(emoji.EMOJI_UNICODE.values())

#cria a interface
st.title('Recomendador de frases motivacionais')
st.write('Clique no botão abaixo para receber uma frase motivacional')
if st.button('Recomendar frase'):
    st.write(frase, emoji)







