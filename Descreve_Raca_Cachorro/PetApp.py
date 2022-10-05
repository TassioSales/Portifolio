#criar um app para que drescreve raça de cachorro usando uma API externa
#https://dog.ceo/dog-api/documentation/random

import requests
import streamlit as st

#criar uma função para pegar a imagem
def get_dog():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    return data["message"]

#criar uma função para pegar a raça
def get_breed():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    data = response.json()
    return data["message"]

#criar uma função para pegar a sub-raça
def get_subbreed(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/list")
    data = response.json()
    return data["message"]

def main():
    st.title("Dog Breed App")
    st.image(get_dog(), width=500)
    st.write("Select a breed to see a sub-breed")
    breed = st.selectbox("Breed", list(get_breed().keys()))
    subbreed = st.selectbox("Sub-breed", get_subbreed(breed))
    st.image(get_dog(), width=500)

if __name__ == '__main__':