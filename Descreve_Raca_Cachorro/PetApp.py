#criar um app para que drescreve raça de cachorro usando uma API externa
#api que vamos usar: https://dog.ceo/dog-api/

import requests
import streamlit as st

#função para pesquisar a raça do cachorro
def main():
    st.title('Descubra a raça do seu cachorro')
    st.write('Digite a raça do seu cachorro')
    raça = st.text_input('Raça do cachorro')
    if raça:
        #fazendo a requisição
        response = requests.get(f'https://dog.ceo/api/breed/{raça}/images/random')
        #pegando a resposta
        data = response.json()
        #pegando a url da imagem
        url = data['message']
        #mostrando a imagem
        st.image(url, use_column_width=True)


if __name__ == '__main__':
    main()