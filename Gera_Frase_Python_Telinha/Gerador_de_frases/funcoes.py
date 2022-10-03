# criar menu tkinter
from tkinter import *
import pandas as pd
import random

# busca frase motivacional no arquivo csv
def frases_motivacionais():
    df_motivacional = pd.read_csv(
    'https://raw.githubusercontent.com/TassioSales/Portifolio/main/Gera_Frases_Python/motivacionais.csv', sep=';',encoding='utf-8')
    frase = random.choice(df_motivacional['Frases_Motivacionais'])
    #criar janela de mensagem
    janela_mensagem = Tk()
    janela_mensagem.title('Frase Motivacional')
    #adaptar tamanho da janela 
    janela_mensagem.geometry('800x100')
    janela_mensagem.configure(background='white')
    #criar label
    label = Label(janela_mensagem, text=frase, font=('Arial', 10), bg='white', fg='black')
    label.place(x=10, y=10)
    #criar botão sair
    botao_sair = Button(janela_mensagem, width=20, text='Sair', command=janela_mensagem.destroy)
    botao_sair.place(x=100, y=50)
    #centralizao botão de sair
    largura_janela = janela_mensagem.winfo_reqwidth()
    #iniciar janela
    janela_mensagem.mainloop()

def frase_desmotivacional():
    df_desmotivacional = pd.read_csv('https://raw.githubusercontent.com/TassioSales/Portifolio/main/Gera_Frases_Python/frases_desmotivacionais.csv',
    sep=';', encoding='utf-8')
    frase = random.choice(df_desmotivacional['Frase_desmotivacionais'])
    #criar janela de mensagem
    janela_mensagem = Tk()
    janela_mensagem.title('Frase Desmotivacional')
    #adaptar tamanho da janela 
    janela_mensagem.geometry('800x100')
    janela_mensagem.configure(background='white')
    #criar label
    label = Label(janela_mensagem, text=frase, font=('Arial', 10), bg='white', fg='black')
    label.place(x=10, y=10)
    #criar botão sair
    botao_sair = Button(janela_mensagem, width=20, text='Sair', command=janela_mensagem.destroy)
    botao_sair.place(x=100, y=50)
    #centralizao botão de sair
    largura_janela = janela_mensagem.winfo_reqwidth()
    #iniciar janela
    janela_mensagem.mainloop()

def cantadas():
    df_cantadas = pd.read_csv('https://raw.githubusercontent.com/TassioSales/Portifolio/main/Gera_Frases_Python/cantadas.csv', sep=';', encoding='utf-8')
    frase = random.choice(df_cantadas['Cantadas'])
    #criar janela de mensagem
    janela_mensagem = Tk()
    janela_mensagem.title('Cantadas')
    #criar janela
    janela_mensagem.geometry('800x100')
    janela_mensagem.configure(background='white')
    #criar label
    label = Label(janela_mensagem, text=frase, font=('Arial', 10), bg='white', fg='black')
    label.place(x=10, y=10)
    #criar botão sair
    botao_sair = Button(janela_mensagem, width=15, text='Sair', command=janela_mensagem.destroy)
    botao_sair.place(x=100, y=50)
    #botao de sair no centro da janela
    largura_janela = janela_mensagem.winfo_reqwidth()
    #iniciar janela
    janela_mensagem.mainloop()

def menu():
    #criar janela
    global janela
    janela = Tk()
    janela.title('Gerador de Frases Motivacionais')
    janela.geometry('360x200')
    janela.configure(background='white')
    #frase motivacional
    botao = Button(janela, width=20, text='Gerar Frase Motivacional', command=frases_motivacionais)
    botao.place(x=10, y=50)
    #criar botão sair
    botao_sair = Button(janela, width=20, text='Sair', command=janela.destroy)
    botao_sair.place(x=200, y=50)
    #frase desmotivacional
    botao = Button(janela, width=20, text='Gerar Frase Desmotivacional', command=frase_desmotivacional)
    botao.place(x=10, y=100)
    #cantadas
    botao = Button(janela, width=20, text='Gerar Cantadas', command=cantadas)
    botao.place(x=10, y=150)
    #iniciar janela
    janela.mainloop()

if __name__ == '__main__':
    menu()
