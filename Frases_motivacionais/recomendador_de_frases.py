#criaçao de um programa que recomenda frases motivacionais para o usuario usar em seu dia a dia
#usar o streamlit para criar a interface

import streamlit as st
import pandas as pd

#busca frase motivacional
#importa dataframe online
df = pd.read_csv('frases_motivacionaiss.csv', encoding='utf-8', sep=';')

#cria uma função para buscar a frases_motivacionaiss
def busca_frase():
    #cria um botão para buscar a frase
    if st.button('Buscar frase motivacional'):
        #cria uma variavel para receber a frase
        frase = df['Frase_motivacionais'].sample(1).values[0]
        #mostra a frase
        st.write(frase)

#mostra o titulo
st.title('Recomendador de frases motivacionais')
#mostra a frase
st.write('Clique no botão abaixo para receber uma frase motivacional')
#chama a função
busca_frase()




