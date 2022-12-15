from datetime import datetime, timedelta
import streamlit as st
import pandas as pd
import random as rd
import os
import requests


# função para validar o cpf digitado pelo utilizador
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


# criar funçao para pesquisar o cep digitado pelo utilizador e retornar o endereço
def pesquisar_cep(cep):
    try:
        # verificar se o cep tem 8 dígitos
        if len(cep) != 8:
            return False
        # verificar se o cep é composto por números
        if not cep.isnumeric():
            return False
        # verificar se o cep é válido
        if cep == '00000000' or cep == '11111111' or cep == '22222222' or cep == '33333333' or \
                cep == '44444444' or cep == '55555555' or cep == '66666666' or cep == '77777777' or \
                cep == '88888888' or cep == '99999999':
            return False
        # pesquisar o cep no site dos correios
        url = 'https://viacep.com.br/ws/' + cep + '/json/'
        r = requests.get(url)
        if r.status_code == 200:
            endereco = r.json()
            return endereco['logradouro'] + ', ' + endereco['bairro'] + ', ' + endereco['localidade'] + ', ' + endereco[
                'uf']
        else:
            return False
    except Exception as e:
        st.error(e)


def criar_arquivo_csv(df):
    if not os.path.isfile('funcionarios.csv'):
        # criar o arquivo csv
        df.to_csv('funcionarios.csv', index=False)
        st.write('Funcionário cadastrado com sucesso')
    ##verificar se o arquivo já existe
    else:
        # se o arquivo já existir, ler o arquivo
        df_funcionario = pd.read_csv('funcionarios.csv', sep=';', encoding='utf-8')
        # verificar se o cpf já está cadastrado e se a matrícula já está cadastrada
        if df['CPF'].isin(df_funcionario['CPF']).any() == False and df['Matrícula'].isin(
                df_funcionario['Matrícula']).any() == False:
            # adicionar o novo funcionário ao arquivo csv
            df_funcionario = df_funcionario.append(df, ignore_index=True)
            df_funcionario.to_csv('funcionarios.csv', sep=';', encoding='utf-8', index=False)
            st.write('Funcionário cadastrado com sucesso')
        else:
            if df['CPF'].isin(df_funcionario['CPF']).any():
                st.write('CPF já cadastrado')
            if df['Matrícula'].isin(df_funcionario['Matrícula']).any():
                st.write('Matrícula já cadastrada')


# função para cadastrar um novo funcionário
def salvar_funcionario(df, df_funcionario):
    # verificar se cpf e matrícula são válidos e unicos e se o cep é válido
    if validar_cpf(df['CPF']) and df['Matrícula'].isin(df_funcionario['Matrícula']).any() == False and \
            pesquisar_cep(df['CEP']) != False:
        # criar arquivo csv se não existir
        criar_arquivo_csv(df)
    else:
        if not validar_cpf(df['CPF']):
            st.write('CPF inválido')
        if df['Matrícula'].isin(df_funcionario['Matrícula']).any():
            st.write('Matrícula já cadastrada')
        if not pesquisar_cep(df['CEP']):
            st.write('CEP inválido')


def cadastrar_funcionario():
    # criar um dataframe para armazenar os dados do funcionário
    df = pd.DataFrame(
        columns=['Matrícula', 'Nome', 'CPF', 'CEP', 'Identidade', 'Endereço', 'Salário', 'Data de admissão',
                 'Data de demissão', 'Motivo da demissão', 'Status', 'Data de cadastro',
                 'Data de atualização', 'Sexo', 'Estado civil', 'Data de nascimento', 'Idade',
                 'Tempo de empresa', 'Naturalida', 'Nacionalidade', 'Escolaridade', 'Cargo',
                 'Departamento', 'Setor', 'Função', 'Horário de trabalho', 'Turno de trabalho',
                 'Tipo de contratação', 'Tipo de jornada', 'Tipo de regime', 'Tipo de salário',
                 'Tipo de trabalho', 'Tipo de vínculo', 'Tipo de admissão', 'Tipo de demissão',
                 'Tipo de desligamento', 'Tipo de movimentação', 'CNH', 'Tipo de CNH', 'Categoria de CNH',
                 'Validade de CNH', 'PIS', 'CTPS', 'Série CTPS', 'Data de emissão CTPS', 'Data de expedição CTPS',
                 'CNPJ', 'Data de emissão CNPJ', 'Data de expedição CNPJ', 'Data de validade CNPJ'])
    # perguntar os dados do funcionário
    matricula = st.text_input('Matrícula')
    nome = st.text_input('Nome')
    cpf = st.text_input('CPF')
    cep = st.text_input('CEP')
    identidade = st.text_input('Identidade')
    # pesquisar o endereço pelo cep informado somente se o cep for válido e se o cep não estiver vazio
    if pesquisar_cep(cep) != False and cep != '':
        endereco = pesquisar_cep(cep)
        # mostrar o endereço no campo endereço
        endereco = st.text_input('Endereço', value=endereco)
    else:
        endereco = st.text_input('Endereço')
        salario = st.text_input('Salário')
        data_admissao = st.text_input('Data de admissão')
        data_demissao = st.text_input('Data de demissão')
        motivo_demissao = st.text_input('Motivo da demissão')
        status = st.text_input('Status')
        # preencher a data de cadastro com a data atual
        data_cadastro = datetime.now().strftime('%d/%m/%Y')
        # preencher a data de atualização com a data atual
        data_atualizacao = datetime.now().strftime('%d/%m/%Y')
        # criar campo para escolher o sexo
        sexo = st.selectbox('Sexo',
                            ['Masculino', 'Feminino', 'Binário', 'Não binário', 'Gênero fluido', 'Gay', 'Lésbica',
                             'Bissexual', 'Pansexual', 'Travesti', 'Transgênero', 'queer', 'Intersexual', 'Outro'])
        # caso o sexo seja outro, perguntar qual o sexo
        if sexo == 'Outro':
            sexo = st.text_input('Qual o seu sexo?')
        # criar campo para estado civel
        estado_civel = st.selectbox('Estado civel', ['Solteiro(a)', 'Casado(a)', 'Viuvo(a)', 'União Estavel', 'Outro'])
        if estado_civel == "Outro":
            estado_civel =st.text_input('Qual estado civel')






def listar():
    st.dataframe(pd.read_csv('funcionarios.csv'))


# função para pesquisa de funcionário por matrícula ou nome, ou cpf
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
    st.sidebar.title('Menu')
    opcao = st.sidebar.selectbox('Selecione uma opção', ['Cadastrar', 'Listar', 'Pesquisar'])
    if opcao == 'Cadastrar':
        cadastrar_funcionario()
    elif opcao == 'Listar':
        listar()
    elif opcao == 'Pesquisar':
        pesquisar()


if __name__ == '__main__':
    main()
