'''
This program shows some basics about Stemming nltk library and compares Porter
Stemmer to Snowball Stemmer
'''
# Import the toolkit and the full Porter Stemmer library
import nltk
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer

print("---------- Create string vector and apply porterstemmer method:", "\n")

#PorterStemmer method
p_stemmer = PorterStemmer()

words = ['run','runner','running','ran','runs','easily','fairly','consolingly']

for word in words:
    print(word+' --> '+p_stemmer.stem(word))

print("---------- Apply snowballstemmer method:", "\n")

# The Snowball Stemmer requires that you pass a language parameter
s_stemmer = SnowballStemmer(language='english')    

for word in words:
    print(word+' --> '+s_stemmer.stem(word))

print("---------- Create sentence and apply porterstemmer method:", "\n")

phrase = 'I am meeting him tomorrow at the meeting'
for word in phrase.split():
    print(word+' --> '+p_stemmer.stem(word))    
