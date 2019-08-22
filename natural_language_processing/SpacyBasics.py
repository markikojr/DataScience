'''
This program shows some spacy basics a Python library that parses and 
"understands" large volumes of text.
'''

# Import spaCy and load the language library
import spacy
nlp = spacy.load('en_core_web_sm')

# Create a Doc object
doc = nlp(u'Tesla is looking at buying U.S. startup for $6 million')

# Print each token separately (tokenization, part-of-speech tagging, dependencies)
for token in doc:
    print(token.text, token.pos_, token.dep_)

#We can check to see what components currently live in the pipeline
print(nlp.pipeline)
print(nlp.pipe_names)

#Original text
print(doc)

#part of text (token)
print(doc[0])

#part-of-speech
print(doc[0].pos_)
print(spacy.explain('PROPN'))

#Dependencies
print(doc[0].dep_)
print(spacy.explain('nsubj'))

#type of text
print(type(doc))

doc2 = nlp(u"Tesla isn't   looking into startups anymore.")

# Lemmas (the base form of the word):
print(doc2[4].text)
print(doc2[4].lemma_)

# Simple Parts-of-Speech & Detailed Tags:
print(doc2[4].pos_)
print(doc2[4].tag_ + ' / ' + spacy.explain(doc2[4].tag_))

# Word Shapes:
print(doc2[0].text+': '+doc2[0].shape_)
print(doc[5].text+' : '+doc[5].shape_)

# Boolean Values:
print(doc2[0].is_alpha)
print(doc2[0].is_stop)

doc3 = nlp(u'Although commmonly attributed to John Lennon from his song "Beautiful Boy", \
the phrase "Life is what happens to us while we are making other plans" was written by \
cartoonist Allen Saunders and published in Reader\'s Digest in 1957, when Lennon was 17.')

#A span is a slice of Doc object in the form Doc[start:stop]
life_quote = doc3[16:30]
print(life_quote)
print(type(life_quote))

doc4 = nlp(u'This is the first sentence. This is another sentence. This is the last sentence.')

#Certain tokens inside a Doc object may also receive a "start of sentence" tag
for sent in doc4.sents:
    print(sent)

print(doc4[6].is_sent_start)
