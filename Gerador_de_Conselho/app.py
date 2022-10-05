#criar arquivo package.txt
#pip3 freeze > package.txt
#imports

#import biblioteca tradutor google
from google.cloud import translate
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


#criar funçao que vai traduzir o conselho somente para portugues
def translate_advice(advice):
    """
    Função que traduz o conselho para português
    :param advice: str conselho para ser traduzido
    :return: str conselho traduzido
    """
    #criar variavel que vai receber o texto que vai ser traduzido
    text = [advice]
    #criar variavel que vai receber o idioma que vai ser traduzido
    target = "pt"
    #criar variavel que vai receber o idioma que vai ser traduzido
    source = "en"
    #criar variavel que vai receber o texto traduzido
    translation = translate_client.translate(text, target_language=target, source_language=source)
    #criar variavel que vai receber o texto traduzido
    translated_text = translation["translatedText"]
    #retornar o texto traduzido
    return translated_text



def main():
    """
    Função principal do programa
    """
    #criar variavel que vai receber o titulo do programa
    st.title("Conselho do dia")
    #criar variavel que vai receber o subtitulo do programa
    st.subheader("Clique no botão para receber um conselho")
    #criar variavel que vai receber o botão
    button = st.button("Receber conselho")
    #criar condicional que vai verificar se o botão foi clicado
    if button:
        #criar variavel que vai receber o conselho
        advice = get_advice()
        #criar variavel que vai receber o conselho traduzido
        translated_advice = translate_advice(advice)
        #criar variavel que vai receber o conselho

if __name__ == '__main__':
    main()
 
