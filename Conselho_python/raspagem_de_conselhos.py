# criar webscraping para raspagem de dados de conselhos do dia a dia e colocar em um arquivo csv
# -*- coding: utf-8 -*-
import requests
import streamlit as st

link = 'https://br.pinterest.com/eunicealvesmelo/conselhos-importantes-para-o-dia-a-dia/'


# funçao para fazer a requisição
def requisicao(link):
    requisita = requests.get(link)
    return requisita


# funçao para pegar o link das imagens sem o BeautifulSoup
def pegar_link_imagem(requisita):
    import re
    imagens = re.findall(r"<img.*?src=\"(.*?)\"", requisita.text)
    return imagens



# funçao para mostra o link das imagens
def mostrar_link_imagem(imagens):
    for imagem in imagens:
        print(imagem['src'])


# funçao para mostra uma imagem aleatoria
def mostrar_imagem_aleatoria(imagens):
    import random
    imagem = random.choice(imagens)
    print(imagem['src'])


# funçao para mostra imagens no streamlit
def mostrar_imagem_streamlit(imagens):
    for imagem in imagens:
        st.image(imagem['src'])


def main():
    requisita = requisicao(link)
    imagens = pegar_link_imagem(requisita)
    st.title('Gerador de Conselho')
    st.write('clique no botão para receber um Conselho')
    st.write('')
    st.write('')
    # cria botao para mostrar imagem aleatoria
    if st.button('Mostrar Conselho'):
        mostrar_imagem_aleatoria(imagens)
