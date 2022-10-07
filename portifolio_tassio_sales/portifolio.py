#criar portifolio personalizado sobre mim
#autor: Tassio Sales

import streamlit as st

#funcao para configurçoes da pagina web em html
def config():
    st.set_page_config(page_title="Portifolio",page_icon=":smiley:",layout="centered",initial_sidebar_state="expanded",
    menu_items={"Get Help": "https://docs.streamlit.io/en/stable/troubleshooting/clean-install.html", "Report a bug": "https://streamlit.io/en/stable/troubleshooting/clean-install.html", "About": "https://streamlit.io/about"})


def main():
    config()
    st.sidebar.title("Menu")
    menu = st.sidebar.radio("Menu",["Home","Sobre","Contato"])


if __name__ == '__main__':
    main()