#criar programa para analisar sentimento de frases digitadas pelo usuario
#utilizar o algoritmo de Naive Bayes
#utilizar o dataset do NLTK
#utilizar o classificador do NLTK
#utilizar o modulo de tokenizacao do NLTK
#utilizar o modulo de stopwords do NLTK
#utilizar o modulo de stemmer do NLTK
#utilizar o modulo de lematizacao do NLTK
#utilizar o modulo de wordnet do NLTK

#bibliotecas
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import WordNetLemmatizer
import streamlit as st

#funcao para tokenizar
def tokenizar(texto):
    token = word_tokenize(texto)
    return token

#funcao para remover stopwords
def remover_stopwords(texto):
    stop_words = set(stopwords.words('english'))
    palavras = word_tokenize(texto)
    palavras_filtradas = []
    for w in palavras:
        if w not in stop_words:
            palavras_filtradas.append(w)
    return palavras_filtradas

#funcao para lematizar
def lematizar(texto):
    lemmatizer = WordNetLemmatizer()
    palavras = word_tokenize(texto)
    palavras_lematizadas = []
    for w in palavras:
        palavras_lematizadas.append(lemmatizer.lemmatize(w))
    return palavras_lematizadas

#funcao para stemizar
def stemizar(texto):
    stemmer = PorterStemmer()
    palavras = word_tokenize(texto)
    palavras_stemizadas = []
    for w in palavras:
        palavras_stemizadas.append(stemmer.stem(w))
    return palavras_stemizadas

#funcao para classificar
def classificar(texto):
    all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
    word_features = list(all_words)[:2000]
    def document_features(document):
        document_words = set(document)
        features = {}
        for word in word_features:
            features['contains({})'.format(word)] = (word in document_words)
        return features
    featuresets = [(document_features(d), c) for (d,c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    return classifier.classify(document_features(texto))

#funcao para analisar sentimento
def analisar_sentimento(texto):
    texto = texto.lower()
    texto = remover_stopwords(texto)
    texto = lematizar(texto)
    texto = stemizar(texto)
    texto = classificar(texto)
    return texto

if __name__ == "__main__":
    st.title("Analisador de Sentimento")
    st.subheader("Digite uma frase para analisar o sentimento")
    texto = st.text_input("Digite a frase")
    if st.button("Analisar"):
        resultado = analisar_sentimento(texto)
        st.success(resultado)
