#criaçao de um programa que recomenda frases motivacionais para o usuario usar em seu dia a dia
#usar o streamlit para criar a interface

import streamlit as st
import pandas as pd

#busca frase motivacional
#importa dataframe online
df = pd.read_csv('https://raw.githubusercontent.com/luizgustavocosta/recomendador_de_frases/main/frases_motivacionais.csv')

#cria uma função para recomendar frases_motivacionais
def recomenda_frase():
    return df.sample()

if __name__ == '__main__':
    st.title('Recomendador de frases motivacionais')
    st.write('Clique no botão abaixo para receber uma frase motivacional')
    if st.button('Recomenda uma frase'):
        st.write(recomenda_frase())