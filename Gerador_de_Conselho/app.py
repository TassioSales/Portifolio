#criar arquivo package.txt
#pip3 freeze > package.txt
#imports

#import biblioteca tradutor google
from googletrans import Translator
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
    :param language: str linguagem para traduzir
    :return: str conselho traduzido
    """
    #criar variavel que vai receber o tradutor
    translator = Translator()
    #criar variavel que vai receber o conselho traduzido
    translated_advice = translator.translate(advice, dest=language)
    #retornar o conselho traduzido
    return translated_advice.text

if __name__ == '__main__':
    #criar titulo
    st.title("Advice Slip")
    #criar subtitulo
    st.subheader("Get a random advice")
    #criar botao que vai chamar a funçao que vai dar o conselho
    if st.button("Get advice"):
        #criar variavel que vai receber o conselho
        advice = get_advice()
        #criar variavel que vai receber a linguagem que o usuario escolheu
        language = st.selectbox("Select the language", ["en", "es", "pt", "fr", "de", "it", "ru", "ja", "zh-CN"])
        #criar variavel que vai receber o conselho traduzido
        translated_advice = translate_advice(advice, language)
        #mostrar o conselho traduzido
        st.write(translated_advice)