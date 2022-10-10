# criar programa que crie cpf e cnpj
# -*- coding: utf-8 -*-

import streamlit as st
from random import randint


# criar função para gerar cpf
def gerar_cpf():
    """Função para gerar um número de CPF válido
    return: strings com 11 dígitos
    
"""
    # criar lista para armazenar os 9 primeiros digitos
    numero = str(randint(100000000, 999999999))
    # criar lista para armazenar os 2 ultimos digitos
    novo_cpf = numero  # 9 primeiros digitos
    reverso = 10  # contador reverso
    total = 0  # soma dos digitos
    # criar laço para gerar os 9 primeiros digitos
    for index in range(19):
        if index > 8:  # primeiro indice vai de 0 a 9
            index -= 9  # segundo indice vai de 9 a 18
        total += int(novo_cpf[index]) * reverso  # valor total da multiplicação
        reverso -= 1  # decrementar o contador reverso
        if reverso < 2:  # quando o contador chegar a 2
            reverso = 11  # reiniciar o contador
            d = 11 - (total % 11)  # digito verificador
            if d > 9:  # se o digito for > 9 o valor é 0
                d = 0
            total = 0  # reiniciar o total
            novo_cpf += str(d)  # concatenar o digito gerado no novo cpf
    return novo_cpf


# criar função para gerar cnpj
def gerar_cnpj():
    """Função para gerar um número de CNPJ válido
    return: strings com 14 dígitos"""
    # criar lista para armazenar os 12 primeiros digitos
    numero = str(randint(100000000000, 999999999999))
    # criar lista para armazenar os 2 ultimos digitos
    novo_cnpj = numero  # 12 primeiros digitos
    reverso = 5  # contador reverso
    total = 0  # soma dos digitos
    # criar laço para gerar os 12 primeiros digitos
    for index in range(16):
        if index > 11:  # primeiro indice vai de 0 a 11
            index -= 12  # segundo indice vai de 12 a 15
        total += int(novo_cnpj[index]) * reverso  # valor total da multiplicação
        reverso -= 1  # decrementar o contador reverso
        if reverso < 2:  # quando o contador chegar a 2
            reverso = 9  # reiniciar o contador
            d = 11 - (total % 11)  # digito verificador
            if d > 9:  # se o digito for > 9 o valor é 0
                d = 0
            total = 0  # reiniciar o total
            novo_cnpj += str(d)  # concatenar o digito gerado no novo cnpj
    return novo_cnpj


def valida_cpf(cpf):
    """Função para validar um número de CPF
    return:
        True para CPF válido
        False para CPF inválido"""
    # criar lista para armazenar os 9 primeiros digitos
    if len(cpf) != 11:# se o tamanho da lista for diferente de 11
        return False
    else:
        novo_cpf = cpf[:-2] # 9 primeiros digitos
        reverso = 10 # contador reverso
        total = 0 # soma dos digitos
        for index in range(19): # criar laço para gerar os 9 primeiros digitos
            if index > 8: # primeiro indice vai de 0 a 9
                index -= 9 # segundo indice vai de 9 a 18
            total += int(novo_cpf[index]) * reverso # valor total da multiplicação
            reverso -= 1 # decrementar o contador reverso
            if reverso < 2: # quando o contador chegar a 2
                reverso = 11 # reiniciar o contador
                d = 11 - (total % 11) # digito verificador
                if d > 9: # se o digito for > 9 o valor é 0
                    d = 0
                total = 0
                novo_cpf += str(d) # concatenar o digito gerado no novo cpf
        sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf) # verificar se todos os digitos são iguais
        if cpf == novo_cpf and not sequencia: # se o cpf for igual ao novo cpf e não for uma sequencia
            return True # cpf é valido
        else:
            return False # cpf é invalido


def valida_cnpj(cnpj):
    """Função para validar um número de CNPJ
    return:
        True para CNPJ válido
        False para CNPJ inválido"""
    # criar lista para armazenar os 12 primeiros digitos
    if len(cnpj) != 14: # se o tamanho da lista for diferente de 14
        return False # cnpj é invalido
    else: # se o tamanho da lista for igual a 14
        novo_cnpj = cnpj[:-2] # 12 primeiros digitos
        reverso = 5 # contador reverso
        total = 0 # soma dos digitos
        for index in range(16): # criar laço para gerar os 12 primeiros digitos
            if index > 11: # primeiro indice vai de 0 a 11
                index -= 12 # segundo indice vai de 12 a 15
            total += int(novo_cnpj[index]) * reverso # valor total da multiplicação
            reverso -= 1 # decrementar o contador reverso
            if reverso < 2: # quando o contador chegar a 2
                reverso = 9 # reiniciar o contador
                d = 11 - (total % 11) # digito verificador
                if d > 9: # se o digito for > 9 o valor é 0
                    d = 0
                total = 0
                novo_cnpj += str(d) # concatenar o digito gerado no novo cnpj
        sequencia = novo_cnpj == str(novo_cnpj[0]) * len(cnpj) # verificar se todos os digitos são iguais
        if cnpj == novo_cnpj and not sequencia: # se o cnpj for igual ao novo cnpj e não for uma sequencia
            return True # cnpj é valido
        else:
            return False # cnpj é invalido


def main():
    # criar variavel para armazenar o cpf gerado
    cpf = gerar_cpf()
    # criar variavel para armazenar o cnpj gerado
    cnpj = gerar_cnpj()
    # criar variavel para armazenar o cpf validado
    cpf_validado = valida_cpf(cpf)
    # criar variavel para armazenar o cnpj validado
    cnpj_validado = valida_cnpj(cnpj)
    # crir menu para o usuario usando streamlit
    menu = ['CPF', 'CNPJ']
    with st.form('form1'):
        escolha = st.selectbox('Escolha uma opção', menu)
        submit = st.form_submit_button('Enviar')
    if submit:
        if escolha == 'CPF':
            st.write(f'CPF gerado: {cpf}')
            st.write(f'CPF validado: {cpf_validado}')
        else:
            st.write(f'CNPJ gerado: {cnpj}')
            st.write(f'CNPJ validado: {cnpj_validado}')
    


    

if __name__ == '__main__':
    # executar a função main
    main()
