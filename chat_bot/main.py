import os
import openai
import streamlit as st

openai.api_key = st.secrets["api"]


def chat_bot():
    """Chatbot function
    Returns: str: Chat bot response
    :param question: str: User question
    :parameter response: str: Chat bot response
    :parameter pergunta: str: User question
    :parameter resposta: str: Chat bot response
    :parameter f: str: Chat bot response
    :param bot: str: Chat bot name
    """
    # titulo
    st.title("Chat Bot")
    with st.form("form"):
        question = st.text_input("Humano: ")
        st.form_submit_button("Enviar")
        #limpar caixa de texto
        st.empty()
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Human: {question}\nIA:",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["\n", " Human:", " IA:"]
        )
        # enviar a mensagem para o utilizador
        st.text_area("IA:", value=response['choices'][0]['text'], height=50)
        pergunta = question
        resposta = response['choices'][0]['text']
        with open("chat.txt", "a") as f:
            f.write(f"Humano: {pergunta} \n IA: {resposta}\n")
        # mostrar o historico
        with open("chat.txt", "r") as f:
            st.text_area("Historico", value=f.read(), height=200)


def chat_bot_amigos():
    """Chat Bot com amigos
    Returns:str: Chat bot response
    :param question: str: User question
    :parameter response: str: Chat bot response
    :parameter pergunta: str: User question
    :parameter resposta: str: Chat bot response
    :parameter f: str: Chat bot response
    :param bot: str: Chat bot name
    """
    # titulo,
    st.title("Chat Bot Amigos")
    with st.form("form"):
        question = st.text_input("Humano: ")
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Humano: {question}\nAmigo IA:",
            temperature=0.5,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0,
            stop=["Humano:"]
        )
        # enviar a mensagem para o utilizador
        st.write(f"Amigo IA: {response['choices'][0]['text']}")
        st.form_submit_button("Enviar")
        pergunta = question
        resposta = response['choices'][0]['text']
        with open("chat_amigos.txt", "a") as f:
            f.write(f"Humano: {pergunta} \n Amigo: {resposta}\n")
        # mostrar o historico
        with open("chat_amigos.txt", "r") as f:
            st.text_area("Historico", value=f.read(), height=200)


def chat_bot_marv():
    """Chat Bot com Marv
    Returns: str: Chat bot response
    :param question: str: User question
    :parameter response: str: Chat bot response
    :parameter pergunta: str: User question
    :parameter resposta: str: Chat bot response
    :parameter f: str: Chat bot response
    :param bot: str: Chat bot name
    """
    # titulo
    st.title("Chat Bot Marvin")
    with st.form("form"):
        question = st.text_input("Humano: ")
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Humano: {question}\nMarvin:",
            temperature=0.5,
            max_tokens=60,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0
        )
        # enviar a mensagem para o utilizador
        st.write(f"Marvin: {response['choices'][0]['text']}")
        st.form_submit_button("Enviar")
        pergunta = question
        resposta = response['choices'][0]['text']
        with open("chat_marv.txt", "a") as f:
            f.write(f"Humano: {pergunta} \n Marvin: {resposta}\n")
        # mostrar o historico
        with open("chat_marv.txt", "r") as f:
            st.text_area("Historico", value=f.read(), height=200)


def chat_bot_alexa():
    """Chat Bot com Alexa
    Returns: str: Chat bot response
    :param question: str: User question
    :parameter response: str: Chat bot response
    :parameter pergunta: str: User question
    :parameter resposta: str: Chat bot response
    :parameter f: str: Chat bot response
    :param bot: str: Chat bot name
    """
    # titulo
    st.title("Chat Bot Alexa")
    with st.form("form"):
        question = st.text_input("Humano: ")
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Humano: {question}\nAlexa:",
            temperature=0.5,
            max_tokens=60,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0
        )
        # enviar a mensagem para o utilizador
        st.write(f"Alexa: {response['choices'][0]['text']}")
        st.form_submit_button("Enviar")
        pergunta = question
        resposta = response['choices'][0]['text']
        with open("chat_alexa.txt", "a") as f:
            f.write(f"Humano: {pergunta} \n Alexa: {resposta}\n")
        # mostrar o historico
        with open("chat_alexa.txt", "r") as f:
            st.text_area("Historico", value=f.read(), height=200)


def chat_bot_js():
    """Chat Bot com JavaScript]
    Returns: str: Chat bot response
    :param question: str: User question
    :parameter response: str: Chat bot response
    :parameter pergunta: str: User question
    :parameter resposta: str: Chat bot response
    :parameter f: str: Chat bot response
    :param bot: str: Chat bot name
    """
    # titulo
    st.title("Chat Bot J.S.")
    with st.form("form"):
        question = st.text_input("Humano: ")
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Humano: {question}\nJ.S.:",
            temperature=0.5,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0
        )
        # enviar a mensagem para o utilizador
        st.write(f"J.S.: {response['choices'][0]['text']}")
        st.form_submit_button("Enviar")
        pergunta = question
        resposta = response['choices'][0]['text']
        with open("chat_js.txt", "a") as f:
            f.write(f"Humano: {pergunta} \n J.S.: {resposta}\n")
        # mostrar o historico
        with open("chat_js.txt", "r") as f:
            st.text_area("Historico", value=f.read(), height=200)


# função para limpar o historico
def confingurar_button():
    # configurar cor do botão
    # deixar o botão com vermelho
    # deixa o botão arredondado
    st.markdown(
        """
        <style>
        .reportview-container .main .block-container{
            max-width: 1000px;
            padding-top: 0.5rem;
            padding-right: 0.5rem;
            padding-left: 0.5rem;
            padding-bottom: 0.5rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# criar uma função para limpar o historico de cada chat
def limpar_historico():
    if st.button("Limpar historico"):
        with open("chat_amigos.txt", "w") as f:
            f.write("")
        with open("chat_marv.txt", "w") as f:
            f.write("")
        with open("chat_alexa.txt", "w") as f:
            f.write("")
        with open("chat_js.txt", "w") as f:
            f.write("")
        st.success("Historico limpo com sucesso!")


def main():
    """Main function
    :param bot: str: Chat bot name
    :param question: str: User question
    :parameter response: str: Chat bot response
    """
    confingurar_button()
    st.sidebar.title("Menu")
    menu = ["Chat Bot", "Chat Bot Amigos", "Chat Bot Marvin", "Chat Bot Alexa", "Chat Bot Javascript"]
    choice = st.sidebar.selectbox("Escolha uma opção", menu)
    # chatbot
    if choice == "Chat Bot":
        chat_bot()
    # chatbot amigos
    elif choice == "Chat Bot Amigos":
        chat_bot_amigos()
    # chatbot marvin
    elif choice == "Chat Bot Marvin":
        chat_bot_marv()
    # chatbot alexa
    elif choice == "Chat Bot Alexa":
        chat_bot_alexa()
    # chat bot javascript
    elif choice == "Chat Bot Javascript":
        chat_bot_js()
    else:
        st.write("Escolha uma opção no menu")
    # limpar historico
    limpar_historico()


if __name__ == "__main__":
    main()
