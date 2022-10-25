import nltk
from bases import stop_palavras
from bases import sentimentos
import re
from nrclex import NRCLex 


base = sentimentos
stopwords = stop_palavras
#pedir o texto para o usuário

text = "I am very happy"

emotion = NRCLex(text)

print('\n', emotion.words) 
print('\n', emotion.sentences) 
print('\n', emotion.affect_list) 
print('\n', emotion.affect_dict) 
print('\n', emotion.raw_emotion_scores) 
print('\n', emotion.top_emotions) 
print('\n', emotion.affect_frequencies) 


    
    
