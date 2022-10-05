# import Streamlit
import streamlit as st
# importar biblioteca para fazer requisições
import requests
import traceback


# criar funçao quer dar conselho aleatorio usando advise slip
def get_advice():
    """
    Função que retorna um conselho aleatório
    return: str advice para o usuário
    """
    # criar variavel que vai receber a resposta da api
    response = requests.get("https://api.adviceslip.com/advice")
    # criar variavel que vai receber o json da resposta
    json_data = response.json()
    # criar variavel que vai receber o conselho
    advice = json_data["slip"]["advice"]
    # retornar o conselho
    return advice


# criar funçao quer dar conselho aleatorio usando chuck norris
def get_chuck_norris():
    """
    Função que retorna um conselho aleatório
    return: str advice para o usuário
    """
    # criar variavel que vai receber a resposta da api
    response = requests.get("https://api.chucknorris.io/jokes/random")
    # criar variavel que vai receber o json da resposta
    json_data = response.json()
    # criar variavel que vai receber o conselho
    chunk = json_data["value"]
    # retornar o conselho
    return chunk

#api gerador de piadas aleatorias
def get_joke():
    """
    Função que retorna uma piada aleatória
    return: str joke para o usuário
    """
    # criar variavel que vai receber a resposta da api
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    # criar variavel que vai receber o json da resposta
    json_data = response.json()
    # criar variavel que vai receber a piada
    joke = json_data["setup"] + " " + json_data["punchline"]
    # retornar a piada
    return joke



def main():
    # criar um titulo
    st.title("Gerador de conselhos e piadas aleatórias")
    # criar um subtitulo
    st.subheader("Escolha uma opção abaixo")
    # criar um menu
    menu = ["Conselhos", "Piadas", "Chuck Norris"]
    # criar uma variavel que vai receber o menu
    choice = st.sidebar.selectbox("Menu", menu)
    # criar um if para cada opção do menu
    if choice == "Conselhos":
        # criar um botão
        st.subheader("Clique no botão abaixo para receber um conselho")
        # criar um botão
        if st.button("Dê um conselho"):
            # criar uma variavel que vai receber o conselho
            advice = get_advice()
            # mostrar o conselho para o usuário
            st.success(advice)
    elif choice == "Piadas":
        # criar um botão
        st.subheader("Clique no botão abaixo para receber uma piada")
        # criar um botão
        if st.button("Dê uma piada"):
            # criar uma variavel que vai receber a piada
            joke = get_joke()
            # mostrar a piada para o usuário
            st.success(joke)
    elif choice == "Chuck Norris":
        # criar um botão
        st.subheader("Clique no botão abaixo para receber uma piada do Chuck Norris")
        # criar um botão
        if st.button("Dê uma piada do Chuck Norris"):
            # criar uma variavel que vai receber a piada
            chuck = get_chuck_norris()
            # mostrar a piada para o usuário
            st.success(chuck)

if __name__ == '__main__':
    main()
