import streamlit as st
import pandas as pd
import random as rd
import os


# função para validar o cpf digitado pelo usuário
def validar_cpf(cpf):
    # verificar se o cpf tem 11 dígitos
    if len(cpf) != 11:
        return False
    # verificar se o cpf é composto por números
    if not cpf.isnumeric():
        return False
    # verificar se o cpf é válido
    if cpf == '00000000000' or cpf == '11111111111' or cpf == '22222222222' or cpf == '33333333333' or \
            cpf == '44444444444' or cpf == '55555555555' or cpf == '66666666666' or cpf == '77777777777' or \
            cpf == '88888888888' or cpf == '99999999999':
        return False
    # verificar se o cpf é válido
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto
    if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
        return True
    else:
        return False


# função para cadastrar um novo funcionário
def cadastrar_funcionario():
    nome = st.text_input('Nome')
    idade = st.number_input('Idade')
    salario = st.number_input('Salário')
    departamento = st.text_input('Departamento')
    endereco = st.text_input('Endereço')
    cpf = st.text_input('CPF')
    # somente cadastrar se o cpf for válido
    if not validar_cpf(cpf):
        st.warning('CPF inválido')
    else:
        matricula = rd.randint(1000, 9999)
        funcionario = {'Nome': nome, 'Idade': idade, 'Salário': salario, 'Departamento': departamento,
                       'Endereço': endereco, 'CPF': cpf, 'Matrícula': matricula}
        return funcionario


# criar dataframe com os dados do funcionário
def criar_dataframe(funcionario):
    df = pd.DataFrame(funcionario, index=[0])
    return df


# criar arquivo csv com o dataframe
def criar_arquivo_csv(df):
    ##verificar se o arquivo já existe
    if os.path.isfile('funcionarios.csv'):
        df.to_csv('funcionarios.csv', mode='a', header=False, index=False)
        # verificar se o funcionário já está cadastrado
        if df['Matrícula'].isin(pd.read_csv('funcionarios.csv')['Matrícula']).any():
            st.write('Funcionário já cadastrado')
        else:
            st.write('Funcionário cadastrado com sucesso')
    else:
        df.to_csv('funcionarios.csv', index=False)
        st.write('Funcionário cadastrado com sucesso')


def cadastrar():
    try:
        # chamar função para cadastrar funcionário
        funcionario = cadastrar_funcionario()
        # verificar se existe algum campo vazio
        if st.button('Cadastrar'):
            if funcionario['Nome'] == '' or funcionario['Idade'] == '' or funcionario['Salário'] == '' or \
                    funcionario['Departamento'] == '' or funcionario['Endereço'] == '' or funcionario['CPF'] == '':
                # criar mensagem de alerta
                st.warning('Preencha todos os campos')
            else:
                # chamar função para criar dataframe
                df = criar_dataframe(funcionario)
                # chamar função para criar arquivo csv
                criar_arquivo_csv(df)
    except Exception as e:
        st.error(e)
        st.warning('Preencha todos os campos')


def listar():
    st.dataframe(pd.read_csv('funcionarios.csv'))


# função para pesquisa de funcionário por matrícula ou nome ou cpf
def pesquisar():
    # criar botao para pesquisar
    if st.button('Pesquisar'):
        # criar caixa de texto para digitar a matrícula ou o nome ou o cpf
        pesquisa = st.text_input('Digite a matrícula, o nome ou o cpf')
        # verificar se a pesquisa é vazia
        if pesquisa == '':
            # criar mensagem de alerta
            st.warning('Digite a matrícula, o nome ou o cpf')
        else:
            # verificar se o arquivo existe
            if os.path.isfile('funcionarios.csv'):
                # ler arquivo csv
                df = pd.read_csv('funcionarios.csv')
                # verificar se a pesquisa é um número
                if pesquisa.isnumeric():
                    # verificar se a matrícula existe
                    if df['Matrícula'].isin([int(pesquisa)]).any():
                        # criar dataframe com os dados do funcionário
                        df_funcionario = df[df['Matrícula'] == int(pesquisa)]
                        # criar tabela com os dados do funcionário
                        st.table(df_funcionario)
                    else:
                        # criar mensagem de alerta
                        st.warning('Matrícula não encontrada')
                else:
                    # verificar se o nome existe
                    if df['Nome'].isin([pesquisa]).any():
                        # criar dataframe com os dados do funcionário
                        df_funcionario = df[df['Nome'] == pesquisa]
                        # criar tabela com os dados do funcionário
                        st.table(df_funcionario)
                    else:
                        # criar mensagem de alerta
                        st.warning('Nome não encontrado')
            else:
                # criar mensagem de alerta
                st.warning('Arquivo não encontrado')


def main():
    st.title('Cadastro de Funcionários')
    st.sidebar.title('Menu')
    opcao = st.sidebar.selectbox('Selecione uma opção', ['Cadastrar', 'Listar', 'Pesquisar'])
    if opcao == 'Cadastrar':
        st.title('Cadastrar Funcionário')
        #criar botão para cadastrar
        cadastrar()
    elif opcao == 'Listar':
        listar()
    elif opcao == 'Pesquisar':
        pesquisar()


if __name__ == '__main__':
    main()
