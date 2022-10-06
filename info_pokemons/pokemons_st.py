# criar app que recebe um pokemon e retorna suas informações
# acessar a api  https://pokeapi.co/api/v2/pokemon/{}

import requests
import json
import streamlit as st
from lista_de_pokemons import pokemons_ordem_alfabetica
import traceback


# criar funçaõ que retorna o pokemon que mostre o pokemon digitado
def get_pokemon(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data


# criar que mostra os dados do pokemon
def show_pokemon(data):
    st.title(f"Nome: {data['name']}")
    # colocar imagens do pokemon em colunas
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image(data['sprites']['front_default'])
    with col2:
        st.image(data['sprites']['back_default'])
    with col3:
        st.image(data['sprites']['front_shiny'])
    with col4:
        st.image(data['sprites']['back_shiny'])
    with st.spinner("Carregando dados..."):
        # criar uma tabela em html para mostrar os dados do pokemon
        html = f"""
        <table>
            <tr>
                <th>Altura</th>
                <th>Peso</th>
                <th>Tipo</th>
                <th>Habilidades</th>
                <th>Experiência base</th>
                <th>Ordem</th>
                <th>ID</th>
                </tr>
                <tr>
                <td>{data['height']} </td>
                <td>{data['weight']} Kg</td>
                <td>{data['types'][0]['type']['name']}</td>
                <td>{data['abilities'][0]['ability']['name']}</td>
                <td>{data['base_experience']}</td>
                <td>{data['order']}</td>
                <td>{data['id']}</td>
                </tr>"""
        st.markdown(html, unsafe_allow_html=True)
        # centrar a tabela
        st.markdown("<style>table {margin-left: auto; margin-right: auto;}</style>", unsafe_allow_html=True)


#pegar descrição do pokemon no site bulbapedia
def description(data):
    # criar uma variável que recebe o nome do pokemon
    pokemon = data['name']
    # criar uma variável que recebe o id do pokemon
    id = data['id']
    # criar uma variável que recebe a url do pokemon
    url = f"https://bulbapedia.bulbagarden.net/wiki/{pokemon}_(Pok%C3%A9mon)"
    # criar uma variável que recebe o html da url
    response = requests.get(url)
    # criar uma variável que recebe o texto do html
    html = response.text
    # criar uma variável que recebe a descrição do pokemon
    description = html.split("==Biography==")[1].split("==Game data==")[0].split("{{vital|")[1].split("}}")[0]
    # criar uma variável que recebe a altura do pokemon
    height = html.split("==Biography==")[1].split("==Game data==")[0].split("{{vital|")[1].split("}}")[0].split("|")[1]
    # criar uma variável que recebe o peso do pokemon
    weight = html.split("==Biography==")[1].split("==Game data==")[0].split("{{vital|")[1].split("}}")[0].split("|")[2]
    # criar uma variável que recebe o tipo do pokemon
    type = html.split("==Biography==")[1].split("==Game data==")[0].split("{{vital|")[1].split("}}")[0].split("|")[3]
    # criar uma variável que recebe a categoria do pokemon
    category = html.split("==Biography==")[1].split("==Game data==")[0].split("{{vital|")[1].split("}}")[0].split("|")[4]
    # criar uma variável que recebe a habilidade do pokemon
    ability = html.split("==Biography==")[1].split("==Game data==")[0].split("{{vital|")[1].split("}}")[0].split("|")[5]
    # criar uma variável que recebe a experiência base do pokemon
    base_experience = html.split("==Biography==")[1].split("==Game data==")[0].split("{{vital|")[1].split("}}")[0].split("|")[6]
    # criar uma variável que recebe a geração do pokemon
    generation = html.split("==Biography==")[1].split("==Game data==")[0].split("{{vital|")[1].split("}}")[0].split("|")[7]
    # criar uma variável que recebe a evolução do pokemon
    evolution = html.split("==Biography==")[1].split("==Game data==")[0].split("{{vital|")[1].split("}}")[0].split("|")[8]
    # criar uma variável que recebe a localização do pokemon
    location = html.split("==Biography==")[1].split("==Game data==")[0].split("{{vital|")[1].split("}}")[0].split("|")[9]
    # criar uma variável que recebe a cor do pokemon
    color = html.split("==Biography==")[1].split("==Game data==")[0].split("{{vital|")[1].split("}}")[0].split("|")[10]
    # criar uma variável que recebe a forma do pokemon
    shape = html.split("==Biography==")[1].split("==Game data==")[0].split("{{vital|")[1].split("}}")[0].split("|")[11]
    # criar uma variável que recebe a espécie do pokemon
    species = html.split("==Biography==")[1].split("==Game data==")[0].split("{{vital|")[1].split("}}")[0].split("|")[12]
    #criar uma tabela em html para mostrar os dados do pokemon
    html = f"""
    <table>
        <tr>
            <th>Altura</th>
            <th>Peso</th>
            <th>Tipo</th>
            <th>Categoria</th>
            <th>Habilidade</th>
            <th>Experiência base</th>
            <th>Geração</th>
            <th>Evolução</th>
            <th>Localização</th>
            <th>Cor</th>
            <th>Forma</th>
            <th>Espécie</th>
            </tr>
            <tr>
            <td>{height} </td>
            <td>{weight} </td>
            <td>{type} </td>
            <td>{category} </td>
            <td>{ability} </td>
            <td>{base_experience} </td>
            <td>{generation} </td>
            <td>{evolution} </td>
            <td>{location} </td>
            <td>{color} </td>
            <td>{shape} </td>
            <td>{species} </td>
            </tr>"""
    st.markdown(html, unsafe_allow_html=True)
    # centrar a tabela
    st.markdown("<style>table {margin-left: auto; margin-right: auto;}</style>", unsafe_allow_html=True)
def main():
    # criar um título
    st.title("Pokemons")
    # criar um subtitulo
    st.subheader("Digite o nome do pokemon")
    # criar um input
    pokemon = st.text_input("Digite o nome do pokemon", "pikachu")
    # criar um botão
    if st.button("Buscar"):
        try:
            # criar uma variável que recebe o pokemon digitado
            data = get_pokemon(pokemon)
            # mostrar os dados do pokemon
            show_pokemon(data)
            # mostrar a descrição do pokemon
            description(data)
        except:
            # mostra que o pokemon não existe
            st.error("Pokemon não encontrado")
    st.subheader("Lista de pokemons")
    # criar um select
    pokemon = st.selectbox("Selecione um pokemon", pokemons_ordem_alfabetica)
    # se pokemon for selecionado
    if pokemon:
        try:
            # criar uma variável que recebe o pokemon digitado
            data = get_pokemon(pokemon)
            # mostrar os dados do pokemon
            show_pokemon(data)
            # mostrar a descrição do pokemon
            description(data)
        except:
            # mostra que o pokemon não existe
            st.error("Pokemon não encontrado")


if __name__ == "__main__":
    main()
