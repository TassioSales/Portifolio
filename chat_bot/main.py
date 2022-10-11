import os
import openai
import streamlit as st

openai.api_key = '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'


def chat_bot():
    while True:
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
        # Print the response from the API.
        print("IA: " + response['choices'][0]['text'])


def main():
    st.title("Chat Bot")
    st.write("Chat Bot")
    chat_bot()


if __name__ == "__main__":
    main()
    
