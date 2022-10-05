#criar arquivo package.txt
#pip3 freeze > package.txt
#imports

#import biblioteca tradutor google
from py_trans import PyTranslator
#import Streamlit
import streamlit as st
#importar biblioteca para fazer requisições
import requests

#criar funçao quer dar conselho aleatorio usando advise slip
def get_advice():
    """
    Função que retorna um conselho aleatório
    return: str advice para o usuário
    """
    #criar variavel que vai receber a resposta da api
    response = requests.get("https://api.adviceslip.com/advice")
    #criar variavel que vai receber o json da resposta
    json_data = response.json()
    #criar variavel que vai receber o conselho
    advice = json_data["slip"]["advice"]
    #retornar o conselho
    return advice

#criar funçao que vai traduzir o conselho
def translate_advice(advice, language):
    """
    Função que traduz o conselho
    :param advice: str conselho
    :param language: str linguagem
    :return: str conselho traduzido
    """
    #criar variavel que vai receber o tradutor
    translator = PyTranslator()
    #criar variavel que vai receber o conselho traduzido
    translated_advice = translator.translate(advice, language)
    #retornar o conselho traduzido
    return translated_advice

def main():
    #motrar titulo
    st.title("Conselho Aleatório")
    #crar selectbox para escolher a linguagem
    language = st.selectbox("Escolha a linguagem", ["pt", "es", "fr", "de", "it", "ru", "ja", "zh-CN"])
    #criar botao para gerar conselho
    if st.button("Gerar conselho"):
        #mostra o conselho sem traduzir
        st.write(get_advice())
        #criar variavel que vai receber o conselho
        advice = get_advice()
        #criar variavel que vai receber o conselho traduzido
        translated_advice = translate_advice(advice, language)
        #mostrar o conselho traduzido
        st.write(translated_advice)

if __name__ == '__main__':
    main()
 
