#criaçao de um programa que recomenda frases motivacionais para o usuario usar em seu dia a dia
#usar o streamlit para criar a interface

import streamlit as st
import pandas as pd
import random
#usar html e css para personalizar a pagina
st.markdown(
    """
    <style>
    .reportview-container { background: url("https://images.unsplash.com/photo-1519680772-3b7b1b0c5c1a?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZnJhdGhlcnMlMjBtb3ZpY2F0aW9uYWx8ZW58MHx8MHx8&ixlib=rb-1.2.1&w=1000&q=80") }
    </style>
"""
    , unsafe_allow_html=True)

#busca frase motivacional
#importa dataframe online
df_motivacional = pd.read_csv('https://raw.githubusercontent.com/TassioSales/Portifolio/main/Frases_motivacionais/motivacionais.csv', sep=';', encoding='utf-8')
df_demotivacional = pd.read_csv('https://raw.githubusercontent.com/TassioSales/Portifolio/main/Frases_motivacionais/frases_desmotivacionais.csv', sep=';', encoding='utf-8')
df_cantadas = pd.read_csv('https://raw.githubusercontent.com/TassioSales/Portifolio/main/Frases_motivacionais/cantadas.csv', sep=';', encoding='utf-8')

#Criando listas (frases motivacionais, desmotivacionais e cantadas)
frases_motivacionais = df_motivacional['Frases_Motivacionais'].tolist()
fraser_desmotivacionais = df_demotivacional['Frase_desmotivacionais'].tolist()
cantadas = df_cantadas['Cantadas'].tolist()


lista_emoji = [':smile:', ':grinning:',':grin:', ':joy:', ':smiley:', ':laughing:', ':satisfied:', ':innocent:', ':stuck_out_tongue_winking_eye:', ':wink:', ':blush:', ':slight_smile:', ':upside_down_face:', ':relaxed:', ':yum:', ':relieved:', ':heart_eyes:', ':kissing_heart:', ':kissing:', ':kissing_smiling_eyes:', ':kissing_closed_eyes:', ':stuck_out_tongue_closed_eyes:', ':stuck_out_tongue:', ':money_mouth_face:', ':nerd_face:', ':sunglasses:', ':hugging_face:', ':smirk:', ':no_mouth:', ':neutral_face:', ':expressionless:', ':unamused:', ':rolling_eyes:', ':thinking:', ':flushed:', ':disappointed:', ':worried:', ':angry:', ':rage:', ':pensive:', ':confused:', ':slight_frown:', ':frowning2:', ':persevere:', ':confounded:', ':tired_face:', ':weary:', ':triumph:', ':open_mouth:', ':scream:', ':fearful:', ':cold_sweat:', ':hushed:', ':frowning:', ':anguished:', ':cry:', ':disappointed_relieved:', ':sleepy:', ':sweat:', ':sob:', ':dizzy_face:', ':astonished:', ':zipper_mouth_face:', ':mask:', ':thermometer_face:', ':head_bandage:', ':sleeping:', ':zzz:', ':poop:', ':smiling_imp:', ':imp:', ':japanese_ogre:', ':japanese_goblin:', ':skull:', ':ghost:', ':alien:', ':robot:', ':smiley_cat:', ':smile_cat:', ':joy_cat:', ':heart_eyes_cat:', ':smirk_cat:', ':kissing_cat:', ':scream_cat:', ':crying_cat_face:', ':pouting_cat:', ':raised_hands:', ':clap:', ':wave:', ':thumbsup:', ':thumbsdown:', ':punch:', ':fist:', ':v:', ':ok_hand:', ':raised_hand:', ':open_hands:', ':muscle:', ':pray:', ':point_up:', ':point_up_2:', ':point_down:', ':point_left:', ':point_right:', ':middle_finger:', ':hand_splayed:', ':metal:', ':vulcan_salute:', ':writing_hand:', ':nail_care:', ':lips:', ':tongue:', ':ear:', ':nose:', ':eye:', ':eyes:', ':bust_in_silhouette']

##randomizando a lista
frase_moti = random.choice(frases_motivacionais)
frase_desmoti = random.choice(fraser_desmotivacionais)
cantadas = random.choice(cantadas)

#cria a interface
st.title('Recomendador de frases')
st.write('Escolha o tipo de frase que deseja receber')
st.write('')
st.write('')


#criar colunas
col1, col2 = st.columns([1, 1])
#diminuir a distancia
col1.write('')
col2.write('')

with col1:
    #cria um botao para recomendar frase motivacional
    if st.button('Frase motivacional'):
        st.text_area("Motivacional", frase_moti)
        st.write(random.choice(lista_emoji))
with col2:
    #cria um botao para recomendar frase desmotivacional
    if st.button('Frase desmotivacional'):
        st.text_area("Desmotivacional",frase_desmoti)
        st.write(random.choice(lista_emoji))

st.title('Gerador de Cantadas')
st.write('clique no botão para receber uma cantada')
st.write('')
st.write('')
#cria um botao para gerar uma cantada
if st.button('Gerar Cantada'):
    st.text_area('Cantada', cantadas)
    st.write(random.choice(lista_emoji))

#Obrigado por usar o programa
st.write('Obrigado por usar o programa')
st.write('Espero que tenha gostado')