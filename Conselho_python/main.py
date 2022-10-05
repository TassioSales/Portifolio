#api gerador de conselho Advise slip

import requests
import traceback
#from googletrans import Translator
import streamlit as st
from google_trans_new import google_translator  

#gera um conselho aleatorio
def get_random_advice():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    response.raise_for_status()
    advice = response.json()["slip"]["advice"]
    return advice

#traduz o conselho
def translate_advice(advice, lang):
    translator = google_translator()  
    translated = translator.translate(advice, lang_tgt=lang)
    return translated

    
if __name__ == '__main__':
    st.title('Gerador de conselhos')
    st.write('Clique no botão para gerar um conselho')
    if st.button('Gerar conselho'):
        try:
            advice = get_random_advice()
            st.write(advice)
            lang = st.selectbox('Selecione o idioma', ['en', 'pt', 'es'])
            translated = translate_advice(advice, lang)
            st.write(translated)
        except:
            st.write('Ocorreu um erro')
            st.write(traceback.format_exc())
       



