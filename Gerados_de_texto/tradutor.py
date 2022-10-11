import spacy
import traceback
import streamlit as st
import openai
import spacy

openai.api_key = "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"


# função para pedir frase ao usuário
def get_input():
    try:
        return st.text_input("Digite uma frase:")
    except:
        traceback.print_exc()
        return None


def corrige_texto(texto):
    nlp = spacy.load("pt_core_news_sm")
    doc = nlp(texto)
    texto = ""
    for token in doc:
        texto += token.text + " "
    return texto


# criar função para escolher idioma
def escolhe_idioma():
    try:
        with st.expander("Escolha o idioma para tradução:"):
            opt = st.selectbox("Escolha o idioma para tradução:", ["English", "Spanish", "French", "Japanese",
                                                                   "Italian", "German", "Russian", "Portuguese",
                                                                   "Chinese", "Dutch", "Swedish", "Danish",
                                                                   "Norwegian", "Finnish", "Polish", "Greek",
                                                                   "Turkish", "Arabic", "Hebrew", "Korean",
                                                                   "Hindi", "Urdu", "Libras", "Todos os idiomas"])
        return opt
    except:
        traceback.print_exc()
        return None


# função para traduzir texto
def traduz_texto(texto, idioma):
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=texto,
            temperature=0.9,
            max_tokens=5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[idioma]
        )
        return response["choices"][0]["text"]
    except:
        traceback.print_exc()
        return None

def main():
    #titulo
    st.title("Tradutor de Texto")
    #subtitulo
    st.subheader("Traduza textos para diversos idiomas")
    #texto
    st.write("Digite um texto e escolha o idioma para tradução")
    #pedir frase ao usuário
    texto = get_input()
    #corrigir texto
    texto = corrige_texto(texto)
    #escolher idioma
    idioma = escolhe_idioma()
    #traduzir texto
    traducao = traduz_texto(texto, idioma)
    #criar botão mostrar tradução
    if st.button("Mostrar tradução"):
        st.write(traducao)


if __name__ == "__main__":
    main()
