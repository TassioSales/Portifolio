#criar programa bara analisar o arquivo pdf ou txt fornecido pelo usuario
# e retornar o resultado da analise
# importar bibliotecas
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pdfplumber
from stop_word import stop_palavras
import re
import time
import os
from nltk.stem import RSLPStemmer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator
from wordcloud import WordCloud
import string
import heapq
import nltk



#função para pedir o arquivo ao usuario
def get_file():
    uploaded_file = st.file_uploader("Choose a file")
    if st.button('Upload'):
        if uploaded_file is not None:
            with open("arquivo.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())
            #mostra barra de processo de carregamento
            my_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.1)
                my_bar.progress(percent_complete + 1)
            st.success('Upload realizado com sucesso!')
            
def read_file_pdf():
    #ler o arquivo pdf
    with pdfplumber.open("arquivo.pdf") as pdf:
        #mostrar o texto do arquivo
        texto = ""
        for page in pdf.pages:
            texto += page.extract_text()
        return texto
   
#tratar o texto usando o regex
def limpar_texto(texto):
    texto = texto.lower()
    #remover pontuação
    texto = re.sub(r'[^\w\s]', '', texto)
    #remover numeros
    texto = re.sub(r'[0-9]', '', texto)
    #remover espaços em branco
    texto = texto.strip()
    #remover caracteres especiais
    texto = re.sub(r'[^\w\s]', '', texto)
    #remover acentos
    texto = re.sub(r'[áàâã]', 'a', texto)
    texto = re.sub(r'[éèê]', 'e', texto)
    texto = re.sub(r'[íì]', 'i', texto)
    texto = re.sub(r'[óòôõ]', 'o', texto)
    texto = re.sub(r'[úù]', 'u', texto)
    texto = re.sub(r'[ç]', 'c', texto)
    return texto
        
def remover_stop_words(texto):
    #remover as stop words
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    texto = texto.split()
    texto = [palavra for palavra in texto if palavra not in stop_palavras]
    texto = " ".join(texto)
    return texto

def retorna_texto():
    if os.path.exists("arquivo.pdf"):
        texto = read_file_pdf()
        texto = limpar_texto(texto)
        texto = remover_stop_words(texto)
        return texto
    
#mostar dataframe com as palavras e a quantidade de vezes que aparecem
def mostra_df():
    dados = retorna_texto()
    dados = dados.split()
    dados = pd.DataFrame(dados, columns=["Palavras"])
    dados = dados["Palavras"].value_counts()
    dados = pd.DataFrame(dados)
    dados = dados.rename(columns={"Palavras": "Quantidade"})
    dados = dados.reset_index()
    dados = dados.rename(columns={"index": "Palavras"})
    return dados


#mostrar o grafico de barras
def mostra_grafico_barras(dataframe):
    #criar grafico de barras somente com top 15 palavras
    dados = dataframe.head(15)
    fig = px.bar(dados, x="Palavras", y="Quantidade", color="Quantidade", title="Top 5 palavras")
    st.plotly_chart(fig)
    
#mostrar o grafico de pizza
def mostra_grafico_pizza(dataframe):
    #criar grafico de pizza somente com top 15 palavras
    dados = dataframe.head(5)
    fig = px.pie(dados, values="Quantidade", names="Palavras", title="Top 15 palavras")
    st.plotly_chart(fig)
    

    
#criar wordcloud com as palavras 
def mostra_grafico_nuvem():
    texto = retorna_texto()
    #remover palavras duplicadas
    texto = set(texto.split())
    texto = " ".join(texto)
    #remover palavras com menos de 3 letras
    texto = re.sub(r'\b\w{1,3}\b', '', texto)
    #remover palavras com mais de 15 letras
    texto = re.sub(r'\b\w{15,}\b', '', texto)
    wordcloud = WordCloud(width=800, height=500, max_font_size=110).generate(texto)
    st.image(wordcloud.to_array())
    
    
#analise de sentimento da pagina escolhida pelo usuario
def analise_sentimento():
    nltk.download('vader_lexicon')
    arquivo = retorna_texto()
    #pergunta ao usuario qual pagina ele quer analisar com valor padrao 1 minimo 1
    pagina = st.number_input("Qual página você quer analisar?", min_value=1, value=1)
    #mostrar o texto da pagina escolhida
    if os.path.exists("arquivo.pdf"):
        with pdfplumber.open("arquivo.pdf") as pdf:
            texto = pdf.pages[pagina].extract_text()
            st.write(texto)
            #se o texo estiver em portugues, traduzir para ingles
            if texto.isascii():
                texto = texto
            else:
                translator = Translator()
                texto = translator.translate(texto, dest="en").text
            #analise de sentimento
            sid = SentimentIntensityAnalyzer()
            ss = sid.polarity_scores(texto)
            st.write(ss)
            if ss["compound"] >= 0.05:
                st.success("O Sentimento dessa pagina e positivo")
            elif ss["compound"] <= -0.05:
                st.error("O Sentimento dessa pagina Negativo")
            else:
                st.warning("O Sentimento dessa pagina Neutro")
                
        
        

#criar função para gerar resumo do texto
def resumo_texto():
    nltk.download('all')
    arquivo = retorna_texto()
    #tokenize o texto
    text = ""
    for i in range(len(arquivo)):
        text = text + arquivo[i]
    text = text.split()
    st.write(text)
    
    
    
    
    
    
    
def main():
    #criar menu
    menu = ["Upload", "Mostrar Texto original", "Mostrar Texto tratado", "Mostrar DataFrame", "Mostrar Gráfico Barras", "Mostrar Gráfico Pizza", "Analise de Sentimento", "wordcloud", "Resumo"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Upload":
        st.title("Upload de arquivo")
        st.subheader("Por favor faça upload do arquivo PDF")
        get_file()
    elif choice == "Mostrar Texto original":
        st.title("Trecho do Texto original")        
        #procurar o arquivo usando arquivo.pdf ou arquivo.txt
        if os.path.exists("arquivo.pdf"):
            arquivo = "arquivo.pdf"
            #mostra a pagina 10 usando pdfplumber
            with pdfplumber.open(arquivo) as pdf:
                page = pdf.pages[10]
                st.write(page.extract_text())
    elif choice == "Mostrar Texto tratado":
        st.markdown("<h1 style='text-align: center; color: white;'>Trecho Tratado</h1>", unsafe_allow_html=True)
        texto = retorna_texto()
        st.write(texto)
        
    elif choice == "Mostrar DataFrame":
        st.markdown("<h1 style='text-align: center; color: white;'>Tabela</h1>", unsafe_allow_html=True)
        dataframe = mostra_df()
        #mostrar dataframe alinhado ao centro
        st.table(dataframe.style.set_properties(**{'text-align': 'center'}))
        
    elif choice == "Mostrar Gráfico Barras":
        st.markdown("<h1 style='text-align: center; color: white;'>Grafico Barra</h1>", unsafe_allow_html=True)
        dataframe = mostra_df()
        mostra_grafico_barras(dataframe)
        
    elif choice == "Mostrar Gráfico Pizza":
        st.markdown("<h1 style='text-align: center; color: white;'>Grafico Pizza</h1>", unsafe_allow_html=True)
        dataframe = mostra_df()
        mostra_grafico_pizza(dataframe)
        
    elif choice == "Analise de Sentimento":
        #criar um h1 no streamlit com o titulo Analise de Sentimento alinha ao centro
        st.markdown("<h1 style='text-align: center; color: white;'>Analise de Sentimento</h1>", unsafe_allow_html=True)
        analise_sentimento()
        
    elif choice == "wordcloud":
        st.markdown("<h1 style='text-align: center; color: white;'>Nuvem de palavras</h1>", unsafe_allow_html=True)
        dataframe = mostra_df()
        mostra_grafico_nuvem()
        
    elif choice == "Resumo":
        st.markdown("<h1 style='text-align: center; color: white;'>Resumo</h1>", unsafe_allow_html=True)
        #criar botao para gerar o resumo
        if st.button("Gerar Resumo", key="resumo", help="Clique aqui para gerar o resumo"):
            resumo_texto()

         
if __name__ == '__main__':
    main()