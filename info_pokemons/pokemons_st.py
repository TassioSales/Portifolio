#criar app que recebe um pokemon e retorna suas informações
#acessar a api  https://pokeapi.co/api/v2/pokemon/{}

import requests
import json
import streamlit as st

def main():
    pokemon = st.text_input("Digite o nome do pokemon: ")
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)
    data = json.loads(response.text)
    st.write(f"Nome: {data['name']}")
    st.write(f"Altura: {data['height']}")
    st.write(f"Peso: {data['weight']}")
    st.write(f"Tipo: {data['types'][0]['type']['name']}")
    st.write(f"Habilidades: {data['abilities'][0]['ability']['name']}")
    st.write(f"Experiência base: {data['base_experience']}")
    st.write(f"Ordem: {data['order']}")
    st.write(f"ID: {data['id']}")
    st.image(data['sprites']['front_default'])
    st.image(data['sprites']['back_default'])
    st.image(data['sprites']['front_shiny'])
    st.image(data['sprites']['back_shiny'])

if __name__ == "__main__":
    main()