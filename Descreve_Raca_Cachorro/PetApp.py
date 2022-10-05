#criar um app para que drescreve raça de cachorro usando uma API externa
#api que vamos usar: https://dog.ceo/dog-api/

import requests
import streamlit as st

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

#pegando peso da raça do cachorro no wikipedia
def pegar_peso(raca):
    #fazendo a requisição
    response = requests.get(f'https://en.wikipedia.org/api/rest_v1/page/summary/{raca}')
    #pegando o json
    data = response.json()
    #pegando o peso
    peso = data['extract']
    return peso


#função principal
def main():
    #titulo
    st.title('Descubra a raça do seu cachorro')
    #subtitulo
    st.subheader('Selecione a raça do seu cachorro')
    #chamando a função para selecionar a raça
    raca = selecionar_raca()
    #chamando a função para mostrar a imagem
    mostrar_imagem(raca)
    #chamando a função para pegar o peso
    peso = pegar_peso(raca)
    #mostrando o peso
    st.write(peso)

if __name__ == '__main__':
    main()