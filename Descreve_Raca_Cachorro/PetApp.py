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

#pegar descrição da raça
def pegar_descricao(raca):
    #fazendo a requisição
    response = requests.get(f'https://dog.ceo/api/breed/{raca}/list')
    #pegando o json
    data = response.json()
    #pegar tamanho do cachorro
    tamanho = data['message']['height']['metric']~
    #pegar peso do cachorro
    peso = data['message']['weight']['metric']
    #pegar a vida média do cachorro
    vida = data['message']['life_span']
    #pegar a origem do cachorro
    origem = data['message']['origin']
    #pegar a descrição do cachorro
    descricao = data['message']['bred_for']
    #mostrar as informações
    st.subheader('Informações sobre a raça')
    st.write(f'Tamanho: {tamanho} cm')
    st.write(f'Peso: {peso} kg')
    st.write(f'Vida média: {vida} anos')
    st.write(f'Origem: {origem}')
    st.write(f'Descrição: {descricao}')
    



#função principal
def main():
    st.title('Pet App')
    st.subheader('Descubra a raça do seu cachorro')
    raca = selecionar_raca()
    mostrar_imagem(raca)

if __name__ == '__main__':
    main()