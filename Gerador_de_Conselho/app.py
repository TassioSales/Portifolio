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
    advice = json_data["value"]
    # retornar o conselho
    return advice

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
    # criar titulo
    st.title("Conselhos aleatórios")
    # criar subtitulo
    st.subheader("Aqui você encontra conselhos aleatórios normal")
    # criar botao
    button = st.button("Clique aqui para receber um conselho")
    #criar titulo
    st.title(" Chuck Norris")
    # criar botao
    button2 = st.button("Clique aqui e veja algo sobre Chuck Norris")
    #criar titulo
    st.title("Piadas aleatórias")
    # criar botao
    button3 = st.button("Clique aqui e veja uma piada aleatória")
    # criar condicional para verificar se o botao foi clicado
    if button:
        # criar variavel que vai receber o conselho
        advice = get_advice()
        # criar texto com o conselho
        st.write('Conselho', advice)
    # criar condicional para verificar se o botao foi clicado
    if button2:
        # criar variavel que vai receber o conselho
        advice = get_chuck_norris()
        # criar texto com o conselho
        st.text_area('Chock norris',advice)
    # criar condicional para verificar se o botao foi clicado
    if button3:
        # criar variavel que vai receber o conselho
        joke = get_joke()
        # criar texto com o conselho
        st.write('Piada', joke)


if __name__ == '__main__':
    main()
