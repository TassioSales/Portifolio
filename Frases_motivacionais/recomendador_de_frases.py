#criaçao de um programa que recomenda frases motivacionais para o usuario usar em seu dia a dia
#usar o streamlit para criar a interface

import streamlit as st
import pandas as pd


#busca frase motivacional
#importa dataframe online
df = pd.read_csv('https://raw.githubusercontent.com/TassioSales/Portifolio/main/Frases_motivacionais/frases_motivacionaiss.csv', sep=';', encoding='utf-8')

lista_emoji = [':smile:', ':grinning:',':grin:', ':joy:', ':smiley:', ':laughing:', ':satisfied:', ':innocent:', ':stuck_out_tongue_winking_eye:', ':wink:', ':blush:', ':slight_smile:', ':upside_down_face:', ':relaxed:', ':yum:', ':relieved:', ':heart_eyes:', ':kissing_heart:', ':kissing:', ':kissing_smiling_eyes:', ':kissing_closed_eyes:', ':stuck_out_tongue_closed_eyes:', ':stuck_out_tongue:', ':money_mouth_face:', ':nerd_face:', ':sunglasses:', ':hugging_face:', ':smirk:', ':no_mouth:', ':neutral_face:', ':expressionless:', ':unamused:', ':rolling_eyes:', ':thinking:', ':flushed:', ':disappointed:', ':worried:', ':angry:', ':rage:', ':pensive:', ':confused:', ':slight_frown:', ':frowning2:', ':persevere:', ':confounded:', ':tired_face:', ':weary:', ':triumph:', ':open_mouth:', ':scream:', ':fearful:', ':cold_sweat:', ':hushed:', ':frowning:', ':anguished:', ':cry:', ':disappointed_relieved:', ':sleepy:', ':sweat:', ':sob:', ':dizzy_face:', ':astonished:', ':zipper_mouth_face:', ':mask:', ':thermometer_face:', ':head_bandage:', ':sleeping:', ':zzz:', ':poop:', ':smiling_imp:', ':imp:', ':japanese_ogre:', ':japanese_goblin:', ':skull:', ':ghost:', ':alien:', ':robot:', ':smiley_cat:', ':smile_cat:', ':joy_cat:', ':heart_eyes_cat:', ':smirk_cat:', ':kissing_cat:', ':scream_cat:', ':crying_cat_face:', ':pouting_cat:', ':raised_hands:', ':clap:', ':wave:', ':thumbsup:', ':thumbsdown:', ':punch:', ':fist:', ':v:', ':ok_hand:', ':raised_hand:', ':open_hands:', ':muscle:', ':pray:', ':point_up:', ':point_up_2:', ':point_down:', ':point_left:', ':point_right:', ':middle_finger:', ':hand_splayed:', ':metal:', ':vulcan_salute:', ':writing_hand:', ':nail_care:', ':lips:', ':tongue:', ':ear:', ':nose:', ':eye:', ':eyes:', ':bust_in_silhouette']

#cria uma lista com as frases
frases = df['Frase_motivacionais'].tolist()

#criar uma função para gerar uma frase aleatoria
def gerar_frase():
    return random.choice(frases)

#cria a interface
st.title('Gerador de frases motivacionais')
st.write('Clique no botão abaixo para gerar uma frase motivacional')
#cria um botão centralizado
if st.button('Gerar frase'):
    frase = gerar_frase()
    st.write(frase)
    #mostra um emoji aleatorio
    st.write(random.choice(lista_emoji))
    #aumenta o tamanho da fonte no streamlit
    st.markdown('<style>h1{font-size: 50px;}</style>', unsafe_allow_html=True)
    #centraliza o texto no streamlit
    st.markdown('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)







