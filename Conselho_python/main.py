#api gerador de conselho Advise slip

import requests
import traceback
from googletrans import Translator
import streamlit as st

#gera um conselho aleatorio
def get_random_advice():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    response.raise_for_status()
    advice = response.json()["slip"]["advice"]
    return advice

#mostra o conselho
def show_advice(advice):
    print("Seu conselho do dia é: ", advice)
    #traduz o conselho
    translator = Translator()
    translation = translator.translate(advice, dest="pt")
    print("Seu conselho do dia traduzido é: ", translation.text)

if __name__ == '__main__':
    st.title('Gerador de conselhos')
    st.write('Clique no botão para gerar um conselho')
    if st.button('Gerar conselho'):
        advice = get_random_advice()
        show_advice(advice)



