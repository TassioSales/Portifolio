#criaçao de um programa que recomenda frases motivacionais para o usuario usar em seu dia a dia
#usar o streamlit para criar a interface

import streamlit as st
import pandas as pd
import random


#busca frase motivacional
#importa dataframe online
df_motivacional = pd.read_csv('https://raw.githubusercontent.com/TassioSales/Portifolio/main/Frases_motivacionais/frases_motivacionais.csv', sep=';', encoding='utf-8')
df_demotivacional = pd.read_csv('https://raw.githubusercontent.com/TassioSales/Portifolio/main/Frases_motivacionais/frases_desmotivacionais.csv', sep=';', encoding='utf-8')


#cria uma lista com as frases
frases_motivacionais = df_motivacional['Frases_Motivacionais'].tolist()
fraser_desmotivacionais = df_demotivacional['Frase_desmotivacionais'].tolist()

lista_emoji = [':smile:', ':grinning:',':grin:', ':joy:', ':smiley:', ':laughing:', ':satisfied:', ':innocent:', ':stuck_out_tongue_winking_eye:', ':wink:', ':blush:', ':slight_smile:', ':upside_down_face:', ':relaxed:', ':yum:', ':relieved:', ':heart_eyes:', ':kissing_heart:', ':kissing:', ':kissing_smiling_eyes:', ':kissing_closed_eyes:', ':stuck_out_tongue_closed_eyes:', ':stuck_out_tongue:', ':money_mouth_face:', ':nerd_face:', ':sunglasses:', ':hugging_face:', ':smirk:', ':no_mouth:', ':neutral_face:', ':expressionless:', ':unamused:', ':rolling_eyes:', ':thinking:', ':flushed:', ':disappointed:', ':worried:', ':angry:', ':rage:', ':pensive:', ':confused:', ':slight_frown:', ':frowning2:', ':persevere:', ':confounded:', ':tired_face:', ':weary:', ':triumph:', ':open_mouth:', ':scream:', ':fearful:', ':cold_sweat:', ':hushed:', ':frowning:', ':anguished:', ':cry:', ':disappointed_relieved:', ':sleepy:', ':sweat:', ':sob:', ':dizzy_face:', ':astonished:', ':zipper_mouth_face:', ':mask:', ':thermometer_face:', ':head_bandage:', ':sleeping:', ':zzz:', ':poop:', ':smiling_imp:', ':imp:', ':japanese_ogre:', ':japanese_goblin:', ':skull:', ':ghost:', ':alien:', ':robot:', ':smiley_cat:', ':smile_cat:', ':joy_cat:', ':heart_eyes_cat:', ':smirk_cat:', ':kissing_cat:', ':scream_cat:', ':crying_cat_face:', ':pouting_cat:', ':raised_hands:', ':clap:', ':wave:', ':thumbsup:', ':thumbsdown:', ':punch:', ':fist:', ':v:', ':ok_hand:', ':raised_hand:', ':open_hands:', ':muscle:', ':pray:', ':point_up:', ':point_up_2:', ':point_down:', ':point_left:', ':point_right:', ':middle_finger:', ':hand_splayed:', ':metal:', ':vulcan_salute:', ':writing_hand:', ':nail_care:', ':lips:', ':tongue:', ':ear:', ':nose:', ':eye:', ':eyes:', ':bust_in_silhouette']

#frase motivacional aleatoria
frase_moti = random.choice(frases_motivacionais)
frase_desmoti = random.choice(fraser_desmotivacionais)

#cria a interface
st.title('Recomendador de frases')
st.write('Escolha o tipo de frase que deseja receber')
st.write('')
st.write('')

#cria um botao para recomendar frase motivacional
if st.button('Frase motivacional'):
    st.write(frase_moti)
    st.write(random.choice(lista_emoji))

#cria um botao para recomendar frase desmotivacional
if st.button('Frase desmotivacional'):
    st.write(frase_desmoti)
    st.write(random.choice(lista_emoji))

#mudar a posição do botao no streamlit para ficar ao lado
st.markdown("""
<style>
.reportview-container .main footer {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)



#Obrigado por usar o programa
st.write('Obrigado por usar o programa')


    







