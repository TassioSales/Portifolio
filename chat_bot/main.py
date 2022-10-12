import os
import openai
import streamlit as st

openai.api_key = st.secrets["api"]


def chat_bot():
    while True:
        with st.form("form"):
            question = input("Humano: ")
            if question == 'quit':
                break
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
            #enviar a mensagem para o usuário
            st.write(f"IA: {response['choices'][0]['text']}")
            st.form_submit_button("Enviar")



def main():
    st.title("Chatbot")
    chat_bot()

if __name__ == "__main__":
    main()

