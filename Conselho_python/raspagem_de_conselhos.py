# criar webscraping para raspagem de dados de conselhos do dia a dia e colocar em um arquivo csv
# -*- coding: utf-8 -*-
import requests
import streamlit as st

link = 'https://br.pinterest.com/eunicealvesmelo/conselhos-importantes-para-o-dia-a-dia/'


# funçao para fazer a requisição
def requisicao(link):
    requisita = requests.get(link)
    return requisita


# funçao para fazer a raspagem
def raspagem(requisita):
    # raspagem de dados
    dados = requisita.text
    return dados


# criar uma lista com links das imagens
def lista_de_links(dados):
    lista = []
    for i in range(0, len(dados)):
        if dados[i:i + 4] == 'src=':
            lista.append(dados[i + 5:i + 100])
    return lista


# gerar um link aleatorio
def link_aleatorio(lista):
    import random
    return random.choice(lista)


if __name__ == '__main__':
    requisita = requisicao(link)
    dados = raspagem(requisita)
    lista = lista_de_links(dados)
    link = link_aleatorio(lista)
    st.image(link)
