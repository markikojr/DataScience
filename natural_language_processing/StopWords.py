# Perform standard imports:
import spacy
nlp = spacy.load('en_core_web_sm')

print("---------- Print default spacy stop words:", "\n")

# Print the set of spaCy's default stop words (remember that sets are unordered):
print(nlp.Defaults.stop_words)

print("---------- Print number of stop words:", "\n")

#Count number of stop words
print(len(nlp.Defaults.stop_words))

print("---------- Check if word is a stop word:", "\n")

# Check if word is_stop
print(nlp.vocab['myself'].is_stop)
print(nlp.vocab['mystery'].is_stop)

# Add the word to the set of stop words. Use lowercase!
nlp.Defaults.stop_words.add('btw')

# Set the stop_word tag on the lexeme
nlp.vocab['btw'].is_stop = True

print("---------- Print number of stop words and check if word is_stop:", "\n")

#Count number of stop words and check if added word is_stop
print(len(nlp.Defaults.stop_words))
print(nlp.vocab['btw'].is_stop)

# Remove the word from the set of stop words
nlp.Defaults.stop_words.remove('beyond')

# Remove the stop_word tag from the lexeme
nlp.vocab['beyond'].is_stop = False

print("---------- Print number of stop words and check if word is_stop:", "\n")

#Count number of stop words and check if added word is_stop
print(len(nlp.Defaults.stop_words))
print(nlp.vocab['beyond'].is_stop)
