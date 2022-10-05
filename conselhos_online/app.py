import requests
import traceback
import streamlit as st
from google_trans import google_translator
from fake_useragent import UserAgent


# função para gerar conselho aleatório
def get_random_advice():
    """
    Get random advice from https://api.adviceslip.com/

    Returns:
        str: Random advice
    """
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    response.raise_for_status()
    advice = response.json()["slip"]["advice"]
    return advice


# função para traduzir o conselho
def translate_advice(advice, language):
    """
    Translate advice to selected language

    Args:
        advice (str): Advice to translate
        language (str): Language to translate to

    Returns:
        str: Translated advice
    """
    translator = google_translator()
    try:
        translated_advice = translator.translate(advice, lang_tgt=language)
    except Exception:
        st.error(traceback.format_exc())
        st.error("Error translating advice")
        translated_advice = advice
    return translated_advice


def main():
    st.title("Advice Generator")
    st.markdown("## Get random advice in your language")
    language = st.selectbox("Select language", ["en", "es", "fr", "de", "it"])
    advice = get_random_advice()
    translated_advice = translate_advice(advice, language)
    st.success(translated_advice)


if __name__ == "__main__":
    main()
