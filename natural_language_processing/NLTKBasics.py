# Installation of packages
import nltk
#nltk.download() # Need to apply just the first time

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

print("---------- Create data and apply tokenization:", "\n")

# Tokenize words
data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
print(word_tokenize(data))

print("---------- Apply tokenization to sentences:", "\n")

# Tokenize sentences
print(sent_tokenize(data))

print("---------- Apply tokenization and save to arrays:", "\n")

# NLTK in arrays
phrases = sent_tokenize(data)
words = word_tokenize(data)

print(phrases)
print(words)

print("---------- Remove stop words:", "\n")

# Remove stop words
stopWords = set(stopwords.words('english'))
wordsFiltered = []
 
for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)
 
print(wordsFiltered)

print("---------- Stop words length and contents:", "\n")

# Length and contents of stop words
print(len(stopWords))
print(stopWords)

print("---------- Apply stemming:", "\n")

# Stemming
words = ["game","gaming","gamed","games"]
ps = PorterStemmer()
 
for word in words:
    print(ps.stem(word))

print("---------- Apply lemmatization:", "\n")

# Lemmatization
lem = WordNetLemmatizer()

for word in words:
    print(lem.lemmatize(word))

print("---------- Apply tokenization and part-of-speech tagging:", "\n")

# Speech tagging
document = 'Whether you\'re new to programming or an experienced developer, it\'s easy to learn and use Python.'
sentences = nltk.sent_tokenize(document)
for sent in sentences:
    print(nltk.pos_tag(nltk.word_tokenize(sent)))

print("---------- Apply tokenization, part-of-speech tagging and filter type of word:", "\n")

# Filter based on the type of word
document = 'Today the Netherlands celebrates King\'s Day. To honor this tradition, the Dutch embassy in San Francisco invited me to'
sentences = nltk.sent_tokenize(document)

data = []
for sent in sentences:
    data = data + nltk.pos_tag(nltk.word_tokenize(sent))

for word in data:
    if 'NNP' in word[1]:
        print(word)
  
print("---------- Apply tokenization, get frequency distribution, most common and plot:", "\n")

# Frequency Distribution
text = """Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""
tokenized_word = word_tokenize(text)
print(tokenized_word)

fdist = FreqDist(tokenized_word)
print(fdist)
print(fdist.most_common(2))

fdist.plot(30,cumulative=False)
plt.show()
