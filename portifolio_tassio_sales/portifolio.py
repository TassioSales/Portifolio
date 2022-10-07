#criar portifolio personalizado sobre mim
#autor: Tassio Sales

import streamlit as st

def paginacontato():
    github ="https://github.com/TassioSales"
    linkedin ="https://www.linkedin.com/in/tassiosales/"
    whatsaap = "https://api.whatsapp.com/send?phone=5561982970840"
    email ='tassiosales@gmail.com'
    #criando flexbox cons links e ajuste automatically
    #criando Titulo
    st.markdown("<h1 style='text-align: center; color: White;'>Contatos</h1>", unsafe_allow_html=True)
    #criar caixa de texto explicativo sobre a pagina de contatos
    st.markdown("<p style='text-align: center; color: White;'>Aqui voce pode me encontrar em minhas redes sociais ou me mandar um email</p>", unsafe_allow_html=True)
    #criando flexbox
    st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items:ajuste;">
    <a href="{github}" target="_blank"><img src="https://img.icons8.com/fluent/48/000000/github.png"/>Github</a>
    <a href="{linkedin}" target="_blank"><img src="https://img.icons8.com/fluent/48/000000/linkedin.png"/>Linkedin</a>
    <a href="{whatsaap}" target="_blank"><img src="https://img.icons8.com/fluent/48/000000/whatsapp.png"/>Whatsap</a>
    <a href="mailto:{email}" target="_blank"><img src="https://img.icons8.com/fluent/48/000000/gmail.png"/>Email</a>
    </div>
    """, unsafe_allow_html=True)
    




    
def PaginadeMensagem():
    #configurando h1
    st.markdown("<h1 style='text-align: center; color: White;'>Mensagem</h1>", unsafe_allow_html=True)
    #configurando h2
    st.markdown("<h2 style='text-align: center; color: White;'>Aqui voce pode me deixar um mensagem ou um feedback</h2>", unsafe_allow_html=True)
    #criando um formulario para receber a mensagem do usuario
    with st.form("form1"):
        #criando um campo para o usuario digitar o nome
        nome = st.text_input("Nome")
        #força o usuario a digitar algo no campo nome
        #criando um campo para o usuario digitar o email
        email = st.text_input("Email")
        #criando um campo para o usuario digitar a mensagem
        mensagem = st.text_area("Mensagem")
        #criando um botao para enviar a mensagem
        submit_button = st.form_submit_button("Enviar")
        #se o botao for clicado
        if submit_button:
            #se o campo nome estiver vazio
            if nome == "":
                #mostra mensagem de erro
                st.error("Por favor digite seu nome")
            #se o campo email estiver vazio
            elif email == "":
                #mostra mensagem de erro
                st.error("Por favor digite seu email")
            #se o campo mensagem estiver vazio
            elif mensagem == "":
                #mostra mensagem de erro
                st.error("Por favor digite sua mensagem")
            #se todos os campos estiverem preenchidos
            else:
                #mostra mensagem de sucesso
                st.success("Mensagem enviada com sucesso")
        

def paginaSobre():
    #criar caixa com bordas para o conteudo
        #pegar foto do meu perfil do github
        st.image("https://avatars.githubusercontent.com/u/74218122?s=400&u=0ba1b9753d552bbc6cb3e54765d9ab4907e6d146&v=4", width=200)
        #deixa imagem redonda
        st.markdown("<style>img{border-radius: 50%;}</style>", unsafe_allow_html=True)
        #criar bordas para imagem
        st.markdown("<style>img{border: 5px solid blue;}</style>", unsafe_allow_html=True)
        #configurando h1
        st.markdown("<h1 style='text-align: left; color: White;'>Um pouco sobre mim:</h1>", unsafe_allow_html=True)
        #configurando h2

        with st.expander('Sobre Mim:'):
            st.markdown("<p style='text-align: center; color: White;'>Meu nome é Tassio Sales, sou estudante de Ciência de dados e Inteligencia artificial pelo Instituto de Educação Superior de Brasília, tenho 32 anos e sou apaixonado por tecnologia e programação, estou em busca de uma oportunidade de Trabalho na área de desenvolvimento de software, Engenheiro de dados ou como Cientista de dados.</p>", unsafe_allow_html=True)
        with st.expander('Formação Acadêmica:'):
            st.markdown("<p style='text-align: center; color: White;'>Estou me formando em Ciência de dados e Inteligencia artificial pelo Instituto de Educação Superior de Brasília, tambem tenho cursos tecnico na area de munutenção de computadores e rede.</p>", unsafe_allow_html=True)
        with st.expander('Experiência Profissional:'):
            st.markdown("<p style='text-align: center; color: White;'>Estágio na procuradoria geral da Fazenda Nacional: La eu atuei com coleta de dados usando python(Webscraping), também fiz limpeza de dados usando python, sas ou r, assim como algumas analises usando as mesmas ferramentas, também lidei com banco de dados usando impala, ou SQL. Trabalho </p>", unsafe_allow_html=True)



    
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