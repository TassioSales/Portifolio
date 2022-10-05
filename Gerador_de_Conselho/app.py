#criar arquivo package.txt
#pip3 freeze > package.txt
#imports

#import biblioteca tradutor google
from googletrans import Translator
#import Streamlit
import streamlit as st

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

if __name__ == '__main__':
    conselho = get_advice()
    print(conselho)