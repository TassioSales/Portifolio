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

#pegar a descrição da raça
def pegar_descricao(raca):
    response = requests.get(f'https://dog.ceo/api/breed/{raca}/list')
    #pegando o json
    data = response.json()
    #pegando a peso
    peso = data['message']['weight']['imperial']
    #pegando a altura
    altura = data['message']['height']['imperial']
    #pegando a expectativa de vida
    expectativa_vida = data['message']['life_span']
    #pegando a origem
    origem = data['message']['origin']
    #pegando o grupo
    grupo = data['message']['breed_group']
    #pegando a descrição
    descricao = data['message']['bred_for']
    #criando um texto
    texto = f'''
    Peso: {peso}
    Altura: {altura}
    Expectativa de vida: {expectativa_vida}
    Origem: {origem}
    Grupo: {grupo}
    Descrição: {descricao}
    '''
    return texto

#função principal
def main():
    #titulo
    st.title('Descubra a raça do seu cachorro')
    #subtitulo
    st.markdown('Escolha uma raça e veja a descrição dela')
    #selecionar a raça
    raca = selecionar_raca()
    #mostrar a imagem
    mostrar_imagem(raca)
    #mostrar a descrição
    descricao = pegar_descricao(raca)
    st.markdown(descricao)

if __name__ == '__main__':
    main()