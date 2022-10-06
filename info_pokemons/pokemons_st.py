# criar app que recebe um pokemon e retorna suas informações
# acessar a api  https://pokeapi.co/api/v2/pokemon/{}

import requests
import json
import streamlit as st
from lista_de_pokemons import pokemons_ordem_alfabetica


# criar funçaõ que retorna o pokemon que mostre o pokemon digitado
def get_pokemon(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data


# criar que mostra os dados do pokemon
def show_pokemon(data):
    st.title(f"Nome: {data['name']}")
    st.image(data['sprites']['front_default'])
    st.image(data['sprites']['back_default'])
    st.image(data['sprites']['front_shiny'])
    st.image(data['sprites']['back_shiny'])
    st.write(f"Altura: {data['height']}")
    st.write(f"Peso: {data['weight']}")
    st.write(f"Tipo: {data['types'][0]['type']['name']}")
    st.write(f"Habilidades: {data['abilities'][0]['ability']['name']}")
    st.write(f"Experiência base: {data['base_experience']}")
    st.write(f"Ordem: {data['order']}")
    st.write(f"ID: {data['id']}")


# criar função principal
def main():
    # criar um título
    st.title("Pokemons")
    # criar um subtitulo
    st.subheader("Digite o nome do pokemon")
    # criar um input com o nome do pokemon preenchido com o primeiro pokemon da lista
    pokemon = st.text_input("Digite o nome do pokemon", pokemons_ordem_alfabetica[0])
    # criar um botão
    if st.button("Buscar"):
        # criar uma variável que recebe o pokemon digitado
        data = get_pokemon(pokemon)
        # mostrar os dados do pokemon
        show_pokemon(data)
    # criar um selectbox com a lista de pokemons
    pokemon = st.selectbox("Selecione o pokemon", pokemons_ordem_alfabetica)
    # criar um botão
    if st.button("Buscar"):
        # criar uma variável que recebe o pokemon digitado
        data = get_pokemon(pokemon)
        # mostrar os dados do pokemon
        show_pokemon(data)


if __name__ == "__main__":
    main()
