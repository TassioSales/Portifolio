# criar script para tradução de texto

# imports
import streamlit as st
import openai
import spacy
from lista_de_idiomas import lista_idiomas_ordenada

openai.api_key = st.secrets['api']


# funçao para pedir frase para cliente
def pedir_frase():
    try:
        return st.text_input('Digite sua Frase: ')
    except Exception as e:
        st.write(e)


# funçao para pedir idioma para cliente
def escolha_idioma():
    try:
        # Criar lista de idiomas
        idiomas = lista_idiomas_ordenada
        idioma = st.selectbox('Escolha seu idioma', idiomas)
        return idioma
    except Exception as e:
        st.write(e)


# funçao para traduzir frase
def tradutor(texto, idioma):
    try:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Translate this into 1. {idioma}\n\n{texto}\n\n1.",
            temperature=0.3,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].text
    except Exception as e:
        st.write(e)


def main():
    try:
        with st.spinner('Carregando...'):
            with st.form('form'):
                st.title('Tradutor de Texto')
                st.write('Escolha seu idioma e digite sua frase para ser traduzida')
                idioma = escolha_idioma()
                texto = pedir_frase()
                submit_button = st.form_submit_button("Traduzir")
                if submit_button:
                    if texto == '':
                        st.write('Digite uma frase para ser traduzida')
                    else:
                        traducao = tradutor(texto, idioma)
                        st.text_area('Tradução', traducao)
    except Exception as e:
        st.write(e)


if __name__ == '__main__':
    main()
