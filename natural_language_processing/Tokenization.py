'''
This program shows some basics about tokenization such as token, named entities
noun chunks and built-in visualizers.
'''

# Import spaCy and load the language library
import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

print("---------- Create string, Doc object and get tokens:", "\n")

# Create a string that includes opening and closing quotation marks
mystring = '"We\'re moving to L.A.!"'
print(mystring, "\n")

# Create Doc object and explore tokens
doc = nlp(mystring)

# Get tokens
for token in doc:
    print(token.text, end=' | ')

print("\n")

print("---------- Create doc2 and get tokens: ", "\n")

#spaCy will isolate punctuation that does not form an integral part of a word. Quotation marks, commas, and punctuation at the end of a sentence will be assigned their own token. However, punctuation that exists as part of an email address, website or numerical value will be kept as part of the token.
doc2 = nlp(u"We're here to help! Send snail-mail, email support@oursite.com or visit us at http://www.oursite.com!")

for t in doc2:
    print(t)

print("---------- Create doc3 and get tokens: ", "\n")

doc3 = nlp(u'A 5km NYC cab ride costs $10.30')

for t in doc3:
    print(t)

print("---------- Create doc4 and get tokens: ", "\n")

#Punctuation that exists as part of a known abbreviation will be kept as part of the token.
doc4 = nlp(u"Let's visit St. Louis in the U.S. next year.")

for t in doc4:
    print(t)

print("---------- Count tokens in doc4:", "\n")

#Counting tokens
print(len(doc4))    

print("---------- Create doc5 and get tokens by index position: ", "\n")

#Tokens can be retrieved by index position and slice
doc5 = nlp(u'It is better to give than to receive.')

# Retrieve the third token:
print(doc5[2])
# Retrieve three tokens from the middle:
print(doc5[2:5])
# Retrieve the last four tokens:
print(doc5[-4:])

print("---------- Create doc8, get tokens, entities and number of entities: ", "\n")

#Named Entities (The language model recognizes that certain words are organizational names while others are locations, and still other combinations relate to money, dates, etc. Named entities are accessible through the ents property of a Doc object.)
doc8 = nlp(u'Apple to build a Hong Kong factory for $6 million')

for token in doc8:
    print(token.text, end=' | ')

print('\n----')

for ent in doc8.ents:
    print(ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_)))

#Counting entities
print(len(doc8.ents)) 

print("---------- Create doc9, get noun chunks: ", "\n")

#Noun Chunks ("base noun phrases")
doc9 = nlp(u"Autonomous cars shift insurance liability toward manufacturers.")

for chunk in doc9.noun_chunks:
    print(chunk.text)

print("---------- Create doc10, get noun chunks: ", "\n")

doc10 = nlp(u"Red cars do not carry higher insurance rates.")

for chunk in doc10.noun_chunks:
    print(chunk.text) 

print("---------- Create doc11, get noun chunks: ", "\n")

doc11 = nlp(u"He was a one-eyed, one-horned, flying, purple people-eater.")

for chunk in doc11.noun_chunks:
    print(chunk.text) 

print("---------- Visualizing dependency/entity: ", "\n")
#Built-in Visualizers (After running the cell, click the link created)
doc = nlp(u'Apple is going to build a U.K. factory for $6 million.')
#displacy.serve(doc, style='dep')
displacy.serve(doc, style='ent')
