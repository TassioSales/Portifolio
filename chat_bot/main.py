import os
import openai
import streamlit as st

openai.api_key = st.secrets["api"]


def chat_bot():
    st.write("Hello, I am a chatbot. Ask me anything!")
    user_input = st.text_input("You: ")
    if user_input:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_input,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["\n", " Human:", " AI:"],
        )
        st.write("AI:", response.choices[0].text)





def main():
    st.title("Chatbot")
    chat_bot()

if __name__ == "__main__":
    main()

