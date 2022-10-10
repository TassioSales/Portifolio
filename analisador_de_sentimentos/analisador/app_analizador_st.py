#função para traduzri texto 

def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))

#pedir frase ao usuário
def pedir_frase():
    frase = input('Digite uma frase:')
    return frase

def main():
    frase = pedir_frase()
    if frase:
        frase_traduzida = translate_text('pt', frase)
        print(u"Detected source language: {}".format(frase_traduzida))
        print(frase_traduzida)  

if __name__ == "__main__":
    main()


def main():
    frase = pedir_frase()
    if frase:
        frase_traduzida = translate_text('pt', frase)
        print(u"Detected source language: {}".format(frase_traduzida))
        print(frase_traduzida)
    