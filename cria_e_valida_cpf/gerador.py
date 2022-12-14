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
    # escrever o novo cpf com os caracteres formatados
    return f'{novo_cpf[:3]}.{novo_cpf[3:6]}.{novo_cpf[6:9]}-{novo_cpf[9:11]}'


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
            # escrever o novo cnpj com os caracteres formatados
    return f'{novo_cnpj[:2]}.{novo_cnpj[2:5]}.{novo_cnpj[5:8]}/{novo_cnpj[8:12]}-{novo_cnpj[12:14]}'


def valida_cpf(cpf):
    """Função para validar um número de CPF
    return:
        True para CPF válido
        False para CPF inválido"""
    # remover caracteres especiais
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    # criar lista para armazenar os 9 primeiros digitos
    if len(cpf) != 11:  # se o tamanho da lista for diferente de 11
        return False
    else:
        novo_cpf = cpf[:-2]  # 9 primeiros digitos
        reverso = 10  # contador reverso
        total = 0  # soma dos digitos
        for index in range(19):  # criar laço para gerar os 9 primeiros digitos
            if index > 8:  # primeiro indice vai de 0 a 9
                index -= 9  # segundo indice vai de 9 a 18
            total += int(novo_cpf[index]) * reverso  # valor total da multiplicação
            reverso -= 1  # decrementar o contador reverso
            if reverso < 2:  # quando o contador chegar a 2
                reverso = 11  # reiniciar o contador
                d = 11 - (total % 11)  # digito verificador
                if d > 9:  # se o digito for > 9 o valor é 0
                    d = 0
                total = 0
                novo_cpf += str(d)  # concatenar o digito gerado no novo cpf
        sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)  # verificar se todos os digitos são iguais
        if cpf == novo_cpf and not sequencia:  # se o cpf for igual ao novo cpf e não for uma sequencia
            st.write(f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}')
            st.success('CPF Válido')
        else:
            st.write(f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}')
            st.error('CPF Inválido')


def valida_cnpj(cnpj):
    """Função para validar um número de CNPJ
    return:
        True para CNPJ válido
        False para CNPJ inválido"""
    # remover caracteres especiais
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('-', '')
    cnpj = cnpj.replace('/', '')
    # criar lista para armazenar os 12 primeiros digitos
    if len(cnpj) != 14:  # se o tamanho da lista for diferente de 14
        return False  # cnpj é invalido
    else:  # se o tamanho da lista for igual a 14
        novo_cnpj = cnpj[:-2]  # 12 primeiros digitos
        reverso = 5  # contador reverso
        total = 0  # soma dos digitos
        for index in range(16):  # criar laço para gerar os 12 primeiros digitos
            if index > 11:  # primeiro indice vai de 0 a 11
                index -= 12  # segundo indice vai de 12 a 15
            total += int(novo_cnpj[index]) * reverso  # valor total da multiplicação
            reverso -= 1  # decrementar o contador reverso
            if reverso < 2:  # quando o contador chegar a 2
                reverso = 9  # reiniciar o contador
                d = 11 - (total % 11)  # digito verificador
                if d > 9:  # se o digito for > 9 o valor é 0
                    d = 0
                total = 0
                novo_cnpj += str(d)  # concatenar o digito gerado no novo cnpj
        sequencia = novo_cnpj == str(novo_cnpj[0]) * len(cnpj)  # verificar se todos os digitos são iguais
        if cnpj == novo_cnpj and not sequencia:  # se o cnpj for igual ao novo cnpj e não for uma sequencia
            st.write(f' O CNPJ: {cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}')
            st.success('CNPJ Válido')
        else:
            st.write(f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}')
            st.error('CNPJ Inválido')


def main():
    # variavel para armazenar o cpf
    cpf = gerar_cpf()
    # variavel para armazenar o cnpj
    cnpj = gerar_cnpj()
    # titulo
    st.title('Validador de CPF e CNPJ')
    # subtitulo
    menu = ['Validar CPF', 'Validar CNPJ', 'Gerar']
    choice = st.sidebar.selectbox('Menu', menu) # menu lateral
    if choice == 'Validar CPF': # no menu lateral selecionar a opção Validar cpf
        st.subheader('Validar CPF') # subtitulo
        cpf_input = st.text_input('CPF', 'Digite o CPF') # campo para digitar o cpf_input   
        if st.button('Validar'): # botão para validar o cpf_input
            valida_cpf(cpf_input) # chamar a função valida_cpf
    elif choice == 'Validar CNPJ': # no menu lateral selecionar a opção Validar cnpj
        st.subheader('Validar CNPJ') # subtitulo
        cnpj_input = st.text_input('CNPJ', 'Digite o CNPJ') # campo para digitar o cnpj_input
        if st.button('Validar'): # botão para validar o cnpj_input
            valida_cnpj(cnpj_input) # chamar a função valida_cnpj
    # no menu lateral selecionar a opção Gerar
    elif choice == 'Gerar': # no menu lateral selecionar a opção Gerar
        st.subheader('Gerar CPF e CNPJ') # subtitulo
        if st.button('Gerar CPF'): # botão para gerar o cpf_input
            st.text_area('CPF Gerado:', cpf, height=100) # campo para exibir o cpf gerado
            st.success('CPF Gerado com Sucesso') # mensagem de sucesso
            st.success('O CPF gerado é válido') # mensagem de sucesso
        if st.button('Gerar CNPJ'): # botão para gerar o cnpj_input
            st.text_area('CNPJ Gerado:', cnpj, height=100) # campo para exibir o cnpj gerado
            st.success('CNPJ Gerado com Sucesso') # mensagem de sucesso
            st.success('O CNPJ gerado é válido') # mensagem de sucesso

if __name__ == '__main__':
    # chamar a função main
    main()
