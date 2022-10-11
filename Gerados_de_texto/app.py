# criar texto com frase digitada pelo usuário e usar o markovify para construir o texto
import spacy
import streamlit as st
import openai
import spacy

openai.api_key = st.secrets('API KEY')


# função para pedir frase ao usuário
def get_input():
    return input("Digite uma frase:")


# função para corrigir texto digitado pelo usuário
def corrige_texto(texto):
    nlp = spacy.load("pt_core_news_sm")
    doc = nlp(texto)
    texto = ""
    for token in doc:
        texto += token.text + " "
    return texto


# criar função para escolher idioma
def escolhe_idioma():
    # menu
    print("Escolha o idioma para tradução:")
    print("1 - Inglês")
    print("2 - Espanhol")
    print("3 - Francês")
    print("4 - Japanese")
    print("5 - Italiano")
    print("6 - Alemão")
    print("7 - Russo")
    print("8 - Português")
    print("9 - Chinês")
    print("10 - Holandês")
    print("11 - Sueco")
    print("12 - Dinamarquês")
    print("13 - Norueguês")
    print("14 - Finlandês")
    print("15 - Polonês")
    print("16 - Grego")
    print("17 - Turco")
    print("18 - Árabe")
    print("19 - Hebraico")
    print("20 - Coreano")
    print("21 - Hindi")
    print("22 - Urdu")
    print("23 - Libras")
    print("24 - Todos os idiomas")
    opt = input("Digite a opção desejada: ")
    if opt == "1":
        return "English"
    elif opt == "2":
        return "Spanish"
    elif opt == "3":
        return "French"
    elif opt == "4":
        return "Japanese"
    elif opt == "5":
        return "Italian"
    elif opt == "6":
        return "German"
    elif opt == "7":
        return "Russian"
    elif opt == "8":
        return "Portuguese"
    elif opt == "9":
        return "Chinese"
    elif opt == "10":
        return "Dutch"
    elif opt == "11":
        return "Swedish"
    elif opt == "12":
        return "Danish"
    elif opt == "13":
        return "Norwegian"
    elif opt == "14":
        return "Finnish"
    elif opt == "15":
        return "Polish"
    elif opt == "16":
        return "Greek"
    elif opt == "17":
        return "Turkish"
    elif opt == "18":
        return "Arabic"
    elif opt == "19":
        return "Hebrew"
    elif opt == "20":
        return "Korean"
    elif opt == "21":
        return "Hindi"
    elif opt == "22":
        return "Urdu"
    elif opt == "23":
        return "English, Spanish, French, Japanese, Italian, German, Russian, Portuguese, Chinese, Dutch, Swedish, " \
               "Danish, Norwegian, Finnish, Polish, Greek, Turkish, Arabic, Hebrew, Korean, Hindi, Urdu, Libras"


def tradutor_ingles(texto, idioma):
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Translate this into 1. {idioma}\n\n{texto} ?\n\n1.",
        temperature=0.3,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text


def main():
    texto = get_input()
    texto = corrige_texto(texto)
    idioma = escolhe_idioma()
    texto_traduzido = tradutor_ingles(texto, idioma)
    print(texto_traduzido)


if __name__ == "__main__":
    main()
