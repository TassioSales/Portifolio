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
    #criar um título
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
        except:
            st.error(traceback.format_exc())
    st.subheader("Lista de pokemons")
    # criar um select
    pokemon = st.selectbox("Selecione um pokemon", pokemons_ordem_alfabetica)
    #se pokemon for selecionado
    if pokemon:
        try:
            # criar uma variável que recebe o pokemon digitado
            data = get_pokemon(pokemon)
            # mostrar os dados do pokemon
            show_pokemon(data)
        except:
            st.error(traceback.format_exc())



if __name__ == "__main__":
    main()
