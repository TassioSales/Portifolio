#criar um app para que drescreve raça de cachorro usando uma API externa
#api que vamos usar: https://dog.ceo/dog-api/

import requests
import streamlit as st
from bs4 import BeautifulSoup

#função para pesquisar a raça do cachorro
def selecionar_raca():
    #fazendo a requisição
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    #pegando o json
    data = response.json()
    #pegando as raças
    racas = data['message'].keys()
    #mostrando as raças em um selectbox
    raca = st.selectbox('Selecione a raça do seu cachorro', racas)
    return raca

#mostrar uma imagem da raça selecionada
def mostrar_imagem(raca):
    #fazendo a requisição
    response = requests.get(f'https://dog.ceo/api/breed/{raca}/images/random')
    #pegando o json
    data = response.json()
    #pegando a url da imagem
    url_imagem = data['message']
    #mostrando a imagem
    st.image(url_imagem, use_column_width=True)

#raspa site para pegar a descrição do cachorro
def description(group):
    #fazendo a requisição
    response = requests.get(f'https://www.thesprucepets.com/{group}-dog-breeds-4140716')
    #pegando o html
    html = response.content
    #transformando em um objeto do BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    #pegando a descrição
    description = soup.find('p').text
    return description


#função principal
def main():
    st.title('Descubra a raça do seu cachorro')
    raca = selecionar_raca()
    mostrar_imagem(raca)
    description = description(raca)
    st.write(description)


if __name__ == '__main__':
    main()