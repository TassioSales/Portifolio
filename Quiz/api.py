#criar quiz usando https://the-trivia-api.com/

import streamlit as st
import requests
import json
import random
import time
from googletrans import Translator


#função para escolher a categoria
def get_categories():
    url = 'https://opentdb.com/api_category.php'
    response = requests.get(url)
    data = response.json()
    return data['trivia_categories']

#função para escolher a dificuldade
def get_difficulty():
    return ['easy', 'medium', 'hard']

#função para escolher o tipo de pergunta
def get_type():
    return ['multiple', 'boolean']

#função para escolher a quantidade de perguntas
def get_amount():
    return [3, 5, 10, 15, 20]

#função para criar o quiz
def create_quiz(category, difficulty, type, amount):
    url = 'https://opentdb.com/api.php?'
    url += 'amount=' + str(amount)
    url += '&category=' + str(category)
    url += '&difficulty=' + str(difficulty)
    url += '&type=' + str(type)
    response = requests.get(url)
    data = response.json()
    return data['results']

#criar um arquivo json para salvar as perguntas
def create_dict(quiz):
    questions = {}
    for i in range(len(quiz)):
        questions['Pergunta ' + str(i + 1)] = {
            'question': quiz[i]['question'],
            'correct_answer': quiz[i]['correct_answer'],
            'answers': quiz[i]['incorrect_answers']
        }
        questions['Pergunta ' + str(i + 1)]['answers'].append(quiz[i]['correct_answer'])
        random.shuffle(questions['Pergunta ' + str(i + 1)]['answers'])
    return questions
                   
#função para mostrar as perguntas e respostas
def show_questions(questions):
  #mostra todas as perguntas sem as respostas estarem marcadas e salva as respostas
    answers = {}
    for i in range(len(questions)):
        #traduzir as perguntas e respostas
        translator = Translator()
        question = translator.translate(questions['Pergunta ' + str(i + 1)]['question'], dest='pt').text
        answers['Pergunta ' + str(i + 1)] = st.radio(question, questions['Pergunta ' + str(i + 1)]['answers'])
    return answers

#função para mostrar o resultado
def show_result(questions, answers):
    correct = 0
    for i in range(len(questions)):
        if questions['Pergunta ' + str(i + 1)]['correct_answer'] == answers['Pergunta ' + str(i + 1)]:
            correct += 1
    st.write('Você acertou ' + str(correct) + ' de ' + str(len(questions)) + ' perguntas')
    st.write('Sua pontuação é ' + str(correct * 100 / len(questions)) + '%')
    #mostra as perguntas e respostas corretas
    for i in range(len(questions)):
        #criar uma caixa para mostrar as perguntas e respostas corretas
        st.subheader('Pergunta ' + str(i + 1))
        st.write('Pergunta: ' + questions['Pergunta ' + str(i + 1)]['question'])
        st.write('Resposta correta: ' + questions['Pergunta ' + str(i + 1)]['correct_answer'])
        st.write('Sua resposta: ' + answers['Pergunta ' + str(i + 1)])
        st.write('----------------------------------------')

    
#função principal
def main():
    #criar menu de navegação criar quiz, perguntas e respostas, resultado
    menu = ['Criar Quiz', 'Perguntas e Respostas', 'Resultado']
    choice = st.sidebar.selectbox('Menu', menu)
    #criar quiz
    if choice == 'Criar Quiz':
        st.subheader('Criar Quiz')
        categories = get_categories()
        category_names = []
        category_ids = []
        for i in range(len(categories)):
            category_names.append(categories[i]['name'])
            category_ids.append(categories[i]['id'])
        category_dict = dict(zip(category_names, category_ids))
        category = st.selectbox('Escolha uma categoria', category_names)
        difficulty = st.selectbox('Escolha a dificuldade', get_difficulty())
        type = st.selectbox('Escolha o tipo de pergunta', get_type())
        amount = st.selectbox('Escolha a quantidade de perguntas', get_amount())
        if st.button('Criar Quiz'):
            quiz = create_quiz(category_dict[category], difficulty, type, amount)
            questions = create_dict(quiz)
            with open('questions.json', 'w') as json_file:
                json.dump(questions, json_file)
    #mostrar perguntas e respostas
    elif choice == 'Perguntas e Respostas':
        st.subheader('Perguntas e Respostas')
        with open('questions.json', 'r') as json_file:
            questions = json.load(json_file)
        answers = show_questions(questions)
        if st.button('Salvar Respostas'):
            with open('answers.json', 'w') as json_file:
                json.dump(answers, json_file)
    #mostrar resultado
    elif choice == 'Resultado':
        st.subheader('Resultado')
        with open('questions.json', 'r') as json_file:
            questions = json.load(json_file)
        with open('answers.json', 'r') as json_file:
            answers = json.load(json_file)
        show_result(questions, answers)
        
        
if __name__ == '__main__':
    main()