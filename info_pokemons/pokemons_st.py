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
        #centrar a tabela
        st.markdown("<style>table {margin-left: auto; margin-right: auto;}</style>", unsafe_allow_html=True)



# criar função principal
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
        except:
            # mostra que o pokemon não existe
            st.error("Pokemon não encontrado")


if __name__ == "__main__":
    main()
