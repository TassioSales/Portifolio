#criar portifolio personalizado sobre mim
#autor: Tassio Sales

import streamlit as st

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

def PaginadeMensagem():
    #configurando h1
    st.markdown("<h1 style='text-align: center; color: red;'>Mensagem</h1>", unsafe_allow_html=True)
    #configurando h2
    st.markdown("<h2 style='text-align: center; color: red;'>Aqui voce pode me deixar um mensagem ou um feedback</h2>", unsafe_allow_html=True)
    #criando um formulario para receber a mensagem do usuario
    with st.form("form1"):
        #criando um campo para o usuario digitar o nome
        nome = st.text_input("Nome")
        #força o usuario a digitar algo no campo nome
        if nome == "":
            st.error("Por favor digite seu nome")
        #criando um campo para o usuario digitar o email
        email = st.text_input("Email")
        #força o usuario a digitar algo no campo email
        if email == "":
            st.error("Por favor digite seu email")
        #criando um campo para o usuario digitar a mensagem
        mensagem = st.text_area("Mensagem")
        #força o usuario a digitar algo no campo mensagem
        if mensagem == "":
            st.error("Por favor digite sua mensagem")
        #criando um botao para enviar a mensagem
        submit_button = st.form_submit_button("Enviar")
        #se o botao for clicado
        if submit_button:
            #mostrar mensagem de sucesso
            st.success("Mensagem enviada com sucesso")
            #limpar os campos
            nome = ""
            email = ""
            mensagem = ""
def paginaSobre():
    #criar caixa com bordas para o conteud
        #configurando h1
        st.markdown("<h1 style='text-align: left; color: red;'>Um pouco sobre mim:</h1>", unsafe_allow_html=True)
        #configurando h2
        st.markdown("<p style='text-align: center; color: red;'>Meu nome é Tassio Sales, sou estudante de Ciência de dados e Inteligencia artificial pelo Instituto de Educação Superior de Brasília, tenho 32 anos e sou apaixonado por tecnologia e programação, estou em busca de uma oportunidade de Trabalho na área de desenvolvimento de software, Engenheiro de dados ou como Cientista de dados.</p>", unsafe_allow_html=True)
        #deixa st.expander aberto por padrao


     
def main():
    try:
        st.sidebar.title("Menu")
        menu = st.sidebar.radio("Menu",["Home","Sobre","Contato", "Mensagem"])
        if menu == "Home":
            st.title("Home")
            st.write("Bem vindo ao meu portifolio")
        elif menu == "Sobre":
            paginaSobre()
        elif menu == "Contato":
            paginacontato()
        elif menu == "Mensagem":
            PaginadeMensagem()
  
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()