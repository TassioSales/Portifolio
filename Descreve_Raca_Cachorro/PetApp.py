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
    racas = list(data['message'].keys())
    #selecionando a raça
    raca = st.selectbox('Selecione a raça do cachorro', racas)
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

#pegar a descrição da raça no wikipedia
def pegar_descricao(raca):
    response = requests.get(f'https://en.wikipedia.org/api/rest_v1/page/summary/{raca}')
    data = response.json()
    descricao = data['extract']
    return descricao


#função principal
def main():
    st.title('Descubra a raça do seu cachorro')
    raca = selecionar_raca()
    mostrar_imagem(raca)
    mostrar_descricao(raca)



if __name__ == '__main__':
    main()