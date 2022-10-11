# criar script para tradução de texto

# imports
import streamlit as st
import openai
import spacy

openai.api_key = "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"


# funçao para pedir frase para cliente
def pedir_frase():
    try:
        return st.text_input('Digite sua Frase: ')
    except Exception as e:
        print(e)

# funçao para tratamento de texto em portugues
def tratamento_texto(texto):
    nlp = spacy.load('pt_core_news_sm')
    doc = nlp(texto)
    return doc


# funçao para pedir idioma para cliente
def escolha_idioma():
    try:
        idiomas = ['Portuguese', 'Spanish', 'French', 'German', 'Italian', 'Russian', 'Japanese', 'Chinese', 'Korean',
                   'Arabic', 'Hindi', 'Bengali', 'Punjabi', 'Urdu', 'Tamil', 'Telugu', 'Marathi', 'Gujarati', 'Kannada',
                   'Malayalam', 'Odia', 'Thai', 'Vietnamese', 'Indonesian', 'Malay', 'Burmese', 'Khmer', 'Lao',
                   'Tibetan', 'Amharic', 'Oromo', 'Somali', 'Swahili', 'Kinyarwanda', 'Chichewa', 'Yoruba', 'Zulu',
                   'Xhosa', 'Malagasy', 'Hausa', 'Igbo', 'Yiddish', 'Hebrew', 'Persian', 'Turkish', 'Greek',
                   'Polish', 'Romanian', 'Czech', 'Hungarian', 'Bulgarian', 'Serbian', 'Croatian', 'Slovak',
                   'Slovenian', 'Bosnian', 'Macedonian', 'Albanian', 'Finnish', 'Estonian', 'Lithuanian', 'Latvian',
                   'Afrikaans', 'Irish', 'Scottish', 'Welsh', 'Catalan', 'Basque', 'Galician', 'Maltese', 'Dutch',
                   'Danish', 'Norwegian', 'Swedish', 'Icelandic', 'Tagalog', 'Hawaiian', 'Maori', 'Indonesian',
                   'Malay', 'Burmese', 'Khmer', 'Lao', 'Tibetan', 'Amharic', 'Oromo', 'Somali', 'Swahili',
                   'Kinyarwanda','Chichewa', 'Yoruba', 'Zulu', 'Xhosa', 'Malagasy', 'Hausa','Igbo', 'Yiddish',
                   'Hebrew', 'Persian', 'Turkish', 'Greek', 'Polish', 'Romanian', 'Czech', 'Hungarian',
                   'Bulgarian', 'Serbian', 'Croatian', 'Slovak', 'Slovenian', 'Bosnian', 'Macedonian', 'Albanian',
                   'Finnish', 'Estonian', 'Lithuanian', 'Latvian', 'Afrikaans', 'Irish', 'Scottish', 'Welsh',
                   'Catalan', 'Basque', 'Galician', 'Maltese', 'Dutch', 'Danish', 'Norwegian', 'Swedish',
                   'Icelandic', 'Tagalog', 'Hawaiian', 'Maori']
        return st.selectbox('Escolha o idioma:', idiomas)
    except Exception as e:
        print(e)


# funçao para traduzir frase
def tradutor_ingles(texto, idioma):
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
    st.title('Tradutor de Texto')
    st.write('Tradutor de Texto')
    st.write('Escolha o idioma e digite a frase para tradução')
    idioma = escolha_idioma()
    texto = pedir_frase()
    if st.button('Traduzir'):
        texto_tratado = tratamento_texto(texto)
        traducao = tradutor_ingles(texto_tratado, idioma)
        st.write(traducao)

if __name__ == '__main__':
    main()


