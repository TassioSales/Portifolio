# criar arquivo package.txt
# pip3 freeze > package.txt
# imports

# import biblioteca tradutor google
import googletrans
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


# criar funçao que vai traduzir o conselho somente para portugues
def traduzir_conselho(advice):
    """
    Função que traduz o conselho para português
    return: str translated_advice para o usuário
    """
    # criar variavel que vai receber o tradutor
    translator = googletrans.Translator()
    # criar variavel que vai receber o conselho traduzido
    translated_advice = translator.translate(advice, dest="pt")
    # retornar o conselho traduzido
    return translated_advice
def main():
    try:
        # criar titulo
        st.title("Conselho do dia")
        # criar subtitulo
        st.subheader("Clique no botão para receber um conselho")
        # criar botão
        button = st.button("Clique aqui")
        # criar condicional para o botão
        if button:
            # criar variavel que vai receber o conselho
            advice = get_advice()
            # criar variavel que vai receber o conselho traduzido
            translated_advice = traduzir_conselho(advice)
            # criar titulo para o conselho
            st.title("Conselho")
            # criar subtitulo para o conselho
            st.subheader(translated_advice.text)
    except Exception:
        st.write(traceback.format_exc())


if __name__ == '__main__':
    main()
