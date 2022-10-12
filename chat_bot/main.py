import os
import openai
import streamlit as st

openai.api_key = st.secrets["api"]


def chat_bot():
    #titulo
    st.title("Chat Bot")
    with st.form("form"):
        question = st.text_input("Humano: ")
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
        # enviar a mensagem para o usuário
        st.write(f"IA: {response['choices'][0]['text']}")
        st.form_submit_button("Enviar")


def chat_bot_amigos():
    #titulo,
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
        # enviar a mensagem para o usuário
        st.write(f"Amigo IA: {response['choices'][0]['text']}")
        st.form_submit_button("Enviar")


def chat_bot_marv():
    #titulo
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
        # enviar a mensagem para o usuário
        st.write(f"Marvin: {response['choices'][0]['text']}")
        st.form_submit_button("Enviar")


def chat_bot_alexa():
    #titulo
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
        # enviar a mensagem para o usuário
        st.write(f"Alexa: {response['choices'][0]['text']}")
        st.form_submit_button("Enviar")


def chat_bot_js():
    #titulo
    st.title("Chato Javascript")
    with st.form("form"):
        question = st.text_input("Humano: ")
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=f"Humano: {question}\nJavascript:",
            temperature=0,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0,
            stop=["You:"]
        )
           # enviar a mensagem para o usuário
        st.write(f"Javascript: {response['choices'][0]['text']}")
        st.form_submit_button("Enviar")
        

def main():
    st.sidebar.title("Menu")
    menu = ["Chat Bot", "Chat Bot Amigos", "Chat Bot Marvin", "Chat Bot Alexa", "Chat Bot Javascript"]
    choice = st.sidebar.selectbox("Escolha uma opção", menu)
    if choice == "Chat Bot":
        chat_bot()
    elif choice == "Chat Bot Amigos":
        chat_bot_amigos()
    elif choice == "Chat Bot Marvin":
        chat_bot_marv()
    elif choice == "Chat Bot Alexa":
        chat_bot_alexa()
    elif choice == "Chat Bot Javascript":
        chat_bot_js()
    else:
        st.write("Escolha uma opção no menu")


if __name__ == "__main__":
    main()
