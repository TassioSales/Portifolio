#api gerador de conselho Advise slip

import requests
import traceback
#from googletrans import Translator
import streamlit as st

#gera um conselho aleatorio
def get_random_advice():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    response.raise_for_status()
    advice = response.json()["slip"]["advice"]
    return advice

    
if __name__ == '__main__':
    st.title('Gerador de conselhos')
    st.write('Clique no botão para gerar um conselho')
    if st.button('Gerar conselho'):
        try:
            advice = get_random_advice()
            st.text_area(advice)
            #traduzir com streamlit
            st.write(Translator().translate(advice, dest='pt').text)
        except:
            st.write('Ocorreu um erro ao gerar o conselho')
            traceback.print_exc()
       



