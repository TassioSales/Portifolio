import os
import openai
import streamlit as st

openai.api_key = st.secrets["api"]


def chat_bot():
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
        


def main():
    st.title("Chat Bot")
    st.sidebar.title("Menu")
    menu = st.sidebar.radio("Menu", ["Chat Bot", "Chat Bot Amigos", "Chat Bot Marvin"])
    if menu == "Chat Bot":
        chat_bot()
    elif menu == "Chat Bot Amigos":
        chat_bot_amigos()
    elif menu == "Chat Bot Marvin":
        chat_bot_marv()

if __name__ == "__main__":
    main()
