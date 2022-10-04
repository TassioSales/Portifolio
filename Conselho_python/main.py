#api gerador de conselho Advise slip

import requests
import traceback
from googletrans import Translator
import streamlit as st
from py_trans import PyTranslator

#gera um conselho aleatorio
def get_random_advice():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    response.raise_for_status()
    advice = response.json()["slip"]["advice"]
    return advice

#mostra o conselho
def show_advice(advice):
    st.text_area("Advice", value=advice, height=200)
    #traduz o conselho
    translator = Translator()
    translation = translator.translate(advice, dest="pt")
    st.text_area("Advice in Portuguese", value=translation.text, height=200)
    #traduzir o conselho com PyTranslator
    translatorr = PyTranslator()
    translationn = translatorr.translate(advice, dest="pt")
    st.text_area("Advice in Portuguese", value=translationn, height=200)

    
if __name__ == '__main__':
    st.title('Gerador de conselhos')
    st.write('Clique no botão para gerar um conselho')
    if st.button('Gerar conselho'):
        advice = get_random_advice()
        show_advice(advice)



