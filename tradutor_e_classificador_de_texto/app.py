#biblioteca para classificar o tipo de texto
from langdetect import detect
#biblioteca para traduzir o texto
from googletrans import Translator
#biblioteca para ambiente web
import streamlit as st
#biblioteca para classificar o tipo de texto em poesia ou prosa ou poema etc..
from textblob import TextBlob


#função para pedir texto para o usuário
def get_text():
    text = st.text_area("Digite o texto a ser traduzido")
    return text

#menu de idiomas para tradução
def get_lang():
    try:
        lang = st.selectbox("Selecione o idioma",("Alemão","Português","Inglês","Espanhol","Francês","Italiano","Japonês","Coreano","Chinês"))
        if lang == "Alemão":
            return "de"
        elif lang == "Português":
            return "pt"
        elif lang == "Inglês":
            return "en"
        elif lang == "Espanhol":
            return "es"
        elif lang == "Francês":
            return "fr"
        elif lang == "Italiano":
            return "it"
        elif lang == "Japonês":
            return "ja"
        elif lang == "Coreano":
            return "ko"
        elif lang == "Chinês":
            return "zh-CN"
    except Exception as e:
        print("Erro ao selecionar idioma",e)

#funçao para detectar o idioma do texto
def detect_lang(text):
    try:
        lang = detect(text)
        if lang == "de":
            return "Alemão"
        elif lang == "pt":
            return "Português"
        elif lang == "en":
            return "Inglês"
        elif lang == "es":
            return "Espanhol"
        elif lang == "fr":
            return "Francês"
        elif lang == "it":
            return "Italiano"
        elif lang == "ja":
            return "Japonês"
        elif lang == "ko":
            return "Coreano"
        elif lang == "zh-CN":
            return "Chinês"
    except Exception as e:
        print("Erro ao detectar idioma",e)
        
#função para traduzir o texto apartir do idioma selecionado e idioma detectado do texto
def translate_text(text,lang):
    try:
        translator = Translator()
        translated_text = translator.translate(text,dest=lang)
        return translated_text.text
    except Exception as e:
        print("Erro ao traduzir texto",e)
        
        
#função para mostrar o texto antiguo e o texto traduzido
def show_text(text,translated_text):
    st.write("Texto original:",text)
    st.write("Texto traduzido:",translated_text)
    
#função para classificar o tipo de texto
def classify_text(text):
    try:
        blob = TextBlob(text)
        if blob.detect_language() == "en":
            return blob.tags
        else:
            return blob.translate(to="en").tags
    except Exception as e:
        print("Erro ao classificar texto",e)
        
        
#função para mostrar o tipo de texto
def show_classified_text(text):
    try:
        classified_text = classify_text(text)
        st.write("Tipo de texto:",classified_text)
    except Exception as e:
        print("Erro ao mostrar texto classificado",e)
        
        
#função principal
def main():
    st.title("Tradutor de Textos")
    text = get_text()
    lang = get_lang()
    if text:
        translated_text = translate_text(text,lang)
        show_text(text,translated_text)
        show_classified_text(text)
        
        
if __name__ == "__main__":
    main()
    
