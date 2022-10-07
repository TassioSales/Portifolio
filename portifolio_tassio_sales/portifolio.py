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
    if menu == "Home":
        st.title("Home")
        st.write("Bem vindo ao meu portifolio")
    elif menu == "Sobre":
        st.title("Sobre")
        st.write("Sobre mim")
    elif menu == "Contato":
        st.title("Contatos")
        #configurando meus contatos em html
        #criar um link para o meu linkedin com o icone do linkedin e o nome do meu linkedin e botao para abrir em outra aba
        st.markdown('<a href="https://www.linkedin.com/in/tassiosales/" target="_blank"><img src="https://img.icons8.com/color/48/000000/linkedin.png" width="30px" height="30px" alt="linkedin"></a> <a href="https://www.linkedin.com/in/tassio-sales-7b1b3b1b9/" target="_blank">Tassio Sales</a>', unsafe_allow_html=True)
        #criar um link para o meu github com o icone do github e o nome do meu github e botao para abrir em outra aba
        st.markdown('<a href="https://github.com/TassioSales" target="_blank"><img src="https://img.icons8.com/color/48/000000/github--v1.png" width="30px" height="30px" alt="github"></a> <a href="https://www.github.com/tassiosales" target="_blank">Tassio Sales</a>', unsafe_allow_html=True)
        #criar um para meu whatsapp com o icone do whatsapp e o numero do meu whatsapp e botao para abrir em outra aba
        st.markdown('<a href="https://api.whatsapp.com/send?phone=61982970840" target="_blank"><img src="https://img.icons8.com/color/48/000000/whatsapp--v1.png" width="30px" height="30px" alt="whatsapp"></a> <a href="https://api.whatsapp.com/send?phone=5581999999999" target="_blank">81 99999-9999</a>', unsafe_allow_html=True)
    
        
    



if __name__ == '__main__':
    main()