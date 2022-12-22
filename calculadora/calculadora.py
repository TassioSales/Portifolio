import streamlit as st
import numpy as np

#função para pedir o primeiro numero ao usuario
def get_number():
    return st.number_input('Digite o primeiro número')

#função pedir o segundo numero ao usuario
def get_number2():
    return st.number_input('Digite o segundo número')


#função para pedir operação ao usuario
def get_operation():
    return st.selectbox('Escolha a operação',('soma','subtração','multiplicação','divisão'))

#função para somar dois numeros
def soma(a,b):
    return a+b

#função para subtrair dois numeros
def subtracao(a,b):
    return a-b

#função para multiplicar dois numeros
def multiplicacao(a,b):
    return a*b

#função para dividir dois numeros
def divisao(a,b):
    return a/b

#função para calcular a operação escolhida
def calcular(a,b,operacao):
    if operacao == 'soma':
        return soma(a,b)
    elif operacao == 'subtração':
        return subtracao(a,b)
    elif operacao == 'multiplicação':
        return multiplicacao(a,b)
    elif operacao == 'divisão':
        return divisao(a,b)
    
#função para mostrar o resultado
def mostrar_resultado(resultado):
    st.write('O resultado é: ', resultado)
    
#função principal
def main():
    st.title('Calculadora')
    a = get_number()
    b = get_number2()
    operacao = get_operation()
    resultado = calcular(a,b,operacao)
    mostrar_resultado(resultado)
    
    
if __name__ == '__main__':
    main()
    

