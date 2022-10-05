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

#criar funçao que vai traduzir o conselho somente para portugues
def translate_advice(advice):
    """
    Função que traduz o conselho para português
    param advice: str conselho
    return: str conselho traduzido
    """
    #criar variavel que vai receber o tradutor
    translator = Translator()
    #criar variavel que vai receber o conselho traduzido
    translated_advice = translator.translate(advice, dest="pt")
    #retornar o conselho traduzido
    return translated_advice.text

def main():
    """
    Função principal
    """
    #criar titulo
    st.title("Conselho do dia")
    #criar subtitulo
    st.subheader("Um conselho aleatório para você")
    #criar botao
    if st.button("Gerar conselho"):
        #criar variavel que vai receber o conselho
        advice = get_advice()
        #criar variavel que vai receber o conselho traduzido
        translated_advice = translate_advice(advice)
        #mostrar o conselho traduzido
        st.write(translated_advice)

if __name__ == '__main__':
    main()
 
