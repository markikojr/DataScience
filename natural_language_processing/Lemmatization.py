'''
This program shows some basics about Lemmatization using spacy library
'''

# Perform standard imports:
import spacy
nlp = spacy.load('en_core_web_sm')

print("---------- Create doc1 and apply tokenization, Part-or-speech tag and lemmatization:", "\n")

# Creating doc1
doc1 = nlp(u"I am a runner running in a race because I love to run since I ran today")

# Apply tokenization, Part-or-speech tag and lemmatization
for token in doc1:
    print(token.text, '\t', token.pos_, '\t', token.lemma, '\t', token.lemma_)

print("---------- Define function to apply tokenization, Part-or-speech tag and lemmatization and better display:", "\n")

# Defining function to apply tokenization, Part-or-speech tag and lemmatization and better display
def show_lemmas(text):
    for token in text:
        print(f'{token.text:{12}} {token.pos_:{6}} {token.lemma:<{22}} {token.lemma_}')   

print("---------- Create doc2 and apply function:", "\n")

# Create doc2 and apply function
doc2 = nlp(u"I saw eighteen mice today!")
show_lemmas(doc2)

print("---------- Create doc3 and apply function:", "\n")

# Create doc3 and apply function
doc3 = nlp(u"I am meeting him tomorrow at the meeting.")
show_lemmas(doc3)

print("---------- Create doc4 and apply function:", "\n")

# Create doc4 and apply function
doc4 = nlp(u"That's an enormous automobile")
show_lemmas(doc4)
