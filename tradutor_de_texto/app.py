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
        st.write(e)


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
                   'Kinyarwanda', 'Chichewa', 'Yoruba', 'Zulu', 'Xhosa', 'Malagasy', 'Hausa', 'Igbo', 'Yiddish',
                   'Hebrew', 'Persian', 'Turkish', 'Greek', 'Polish', 'Romanian', 'Czech', 'Hungarian',
                   'Bulgarian', 'Serbian', 'Croatian', 'Slovak', 'Slovenian', 'Bosnian', 'Macedonian', 'Albanian',
                   'Finnish', 'Estonian', 'Lithuanian', 'Latvian', 'Afrikaans', 'Irish', 'Scottish', 'Welsh',
                   'Catalan', 'Basque', 'Galician', 'Maltese', 'Dutch', 'Danish', 'Norwegian', 'Swedish',
                   'Icelandic', 'Tagalog', 'Hawaiian', 'Maori']
        st.selectbox('Escolha o idioma:', idiomas)
        return idiomas
    except Exception as e:
        st.write(e)


# funçao para traduzir frase
def tradutor_ingles(texto, idioma):
    try:
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
    except Exception as e:
        st.write(e)


def main():
    try:
        st.title('Tradutor de Texto')
        frase = pedir_frase()
        idioma = escolha_idioma()
        traducao = tradutor_ingles(frase, idioma)
        st.write(traducao)
    except Exception as e:
        st.write(e)


if __name__ == '__main__':
    main()
