#criar um app para que drescreve raça de cachorro usando uma API externa
#https://dog.ceo/dog-api/documentation/random

import requests
import streamlit as st

#criar uma função para pegar nome da raça
def get_breed():
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    breeds = response.json()['message']
    return breeds

#criar uma função para pegar imagem da raça
def get_image(breed):
    response = requests.get(f'https://dog.ceo/api/breed/{breed}/images/random')
    image = response.json()['message']
    return image

#criar funçao para descrever a raça
def get_description(breed):
    response = requests.get(f'https://dog.ceo/api/breed/{breed}/list')
    description = response.json()['message']
    return description

def main():
    st.title('Dog Breed App')
    st.sidebar.title('Dog Breed App')
    st.markdown('This app retrieves dog breed from the [Dog API](https://dog.ceo/dog-api/)')

    breeds = get_breed()
    breeds = list(breeds.keys())
    breed = st.sidebar.selectbox('Breed', breeds)
    if st.button('Show random image'):
        image = get_image(breed)
        st.image(image, use_column_width=True)

    if st.button('Show description'):
        description = get_description(breed)
        st.write(description)

if __name__ == '__main__':
    main()