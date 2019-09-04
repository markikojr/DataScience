'''
This program shows how to check the degree of similarities
'''

# Import spaCy and load the language library
import spacy
nlp = spacy.load('en_core_web_md')

# Word vector example
#print(nlp(u'lion').vector)

#doc = nlp(u'The quick brown fox jumped over the lazy dogs.')
#print(doc.vector)

# Create a three-token Doc object:
tokens = nlp(u'lion cat pet')

# Iterate through token combinations:
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


