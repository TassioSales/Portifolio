#criar portifolio personalizado sobre mim
#autor: Tassio Sales

#src para o icone do de email
#https://img.icons8.com/doodle/48/000000/newsletter.png



import streamlit as st

#funcao para configurçoes da pagina web em html
def config():
    st.set_page_config(page_title="Portifolio",page_icon=":smiley:",layout="centered",initial_sidebar_state="expanded",
    menu_items={"Get Help": "https://docs.streamlit.io/en/stable/troubleshooting/clean-install.html", "Report a bug": "https://streamlit.io/en/stable/troubleshooting/clean-install.html", "About": "https://streamlit.io/about"})

#criar função com questionario de envio de email para o meu email
def questionario():
    #criar caixa com bordas para o conteudo
    with st.expander("Envie um email para mim"):
        st.title("Envie um email para mim")
        #criar formulario para envio de email
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        mensagem = st.text_area("Mensagem")
        #criar botao para enviar email
        if st.button("Enviar"):
            st.write("Enviado com sucesso")
        st.expander("Contato", expanded=True)

def paginacontato():
    #criar caixa com bordas para o conteudo
    with st.expander("Contato"):
        st.title("Contatos")
        #configurando meus contatos em html
        #criar um link para o meu linkedin com o icone do linkedin e o nome do meu linkedin e botao para abrir em outra aba
        st.markdown('<a href="https://www.linkedin.com/in/tassiosales/" target="_blank"><img src="https://img.icons8.com/color/48/000000/linkedin.png" width="30px" height="30px" alt="linkedin"></a> <a href="https://www.linkedin.com/in/tassiosales/" target="_blank">Linkedin</a>', unsafe_allow_html=True)
        #criar um link para o meu github com o icone do github e o nome do meu github e botao para abrir em outra aba
        st.markdown('<a href="https://github.com/TassioSales" target="_blank"><img src="https://img.icons8.com/color/48/000000/github--v1.png" width="30px" height="30px" alt="github"></a> <a href="https://github.com/TassioSales" target="_blank">Github</a>', unsafe_allow_html=True)
        #criar um para meu whatsapp com o icone do whatsapp e o numero do meu whatsapp e botao para abrir em outra aba
        st.markdown('<a href="https://api.whatsapp.com/send?phone=5561982970840" target="_blank"><img src="https://img.icons8.com/color/48/000000/whatsapp--v1.png" width="30px" height="30px" alt="whatsapp"></a> <a href="https://api.whatsapp.com/send?phone=5561982970840" target="_blank">WhatSapp</a>', unsafe_allow_html=True)
        #criar um link para o meu email com o icone do email e o meu email e botao para abrir em outra aba
        st.markdown('<a href="mailto:tassiolucian.ljs@gmail.com" target="_blank"><img src="https://img.icons8.com/doodle/48/000000/newsletter.png" width="30px" height="30px" alt="email"></a> <a href="mailto:tassiolucian.ljs@gmail.com" target="_blank">Email</a>', unsafe_allow_html=True)
        #deixa st.expander aberto por padrao
        st.expander("Contato", expanded=True)
        questionario()



def main():
    try:
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
            paginacontato()
  
    except Exception as e:
        print(e)


            
    



if __name__ == '__main__':
    main()