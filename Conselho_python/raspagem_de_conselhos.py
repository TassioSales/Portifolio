# criar webscraping para raspagem de dados de conselhos do dia a dia e colocar em um arquivo csv
# -*- coding: utf-8 -*-
import requests
import streamlit as st
import random

link = 'https://br.pinterest.com/eunicealvesmelo/conselhos-importantes-para-o-dia-a-dia/'


# funçao para fazer a requisição
def requisicao(link):
    requisita = requests.get(link)
    return requisita


# funçao para fazer a raspagem
def raspagem(requisita):
    # raspagem de dados
    dados = requisita.text
    #pegar somente os links das imagens
    dados = dados.split('src="')
    dados = dados[1:]
    dados = [i.split('"')[0] for i in dados]
    return dados




if __name__ == '__main__':
    requisita = requisicao(link)
    dados = raspagem(requisita)
    print(dados)
