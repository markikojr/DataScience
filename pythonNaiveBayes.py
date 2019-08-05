import os
import io
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#DEFINING FUNCTION TO READ EACH FILE IN A DIRECTORY
def readFiles(path):
    #GETTING ROOT, DIR(EMPTY) AND FILENAMES
    for root, dirnames, filenames in os.walk(path):
        #READING EACH FILENAME AND FORM COMPLETE PATH/FILE
        for filename in filenames:
            path = os.path.join(root, filename)
            inBody = False
            lines = []
            #OPENING PATH/FILE
            f = io.open(path, 'r', encoding='latin1')
            #READING EACH LINE OF FILE
            for line in f:
                if inBody:
                    lines.append(line) #ADDING EACH LINE TO THE LIST
                elif line == '\n':
                    inBody = True
            f.close()
            #ADDING EACH LINE OF FILE IN SEPARATED LINES
            message = '\n'.join(lines)
            yield path, message

#FUNCTION TO CREATE A DATAFRAME
def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    #READING OUTPUT FROM READFILES FUNCTION (PATH/FILE, MESSAGE)
    for filename, message in readFiles(path):
        #CREATING DICTIONARY
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    #CREATING DATAFRAME
    return DataFrame(rows, index=index)

#CREATING EMPTY DATAFRAME
data = DataFrame({'message': [], 'class': []})

#CALLING DATAFRAME FUNCTION TO FILL DATA
data = data.append(dataFrameFromDirectory('/home/markjr/data_science/DataScience/DataScience-Python3/emails/spam/', 'spam'))
data = data.append(dataFrameFromDirectory('/home/markjr/data_science/DataScience/DataScience-Python3/emails/ham/', 'ham'))

#INSPECTING DATA
print (data.shape)
print (data.head(10))

#CONVERT A COLLECTION OF TEXT DOCUMENTS TO A MATRIX OF TOKEN COUNTS
vectorizer = CountVectorizer()
#LEARN THE VOCABULARY DICTIONARY AND RETURN TERM-DOCUMENT MATRIX (HOW MANY TIMES EACH WORD OCCURS PUTTING THEM IN A MATRIX)
counts = vectorizer.fit_transform(data['message'].values)

#NAIVE BAYES CLASSIFIER FOR MULTINOMIAL MODELS 
classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)

#TESTING MODEL
#GENERATING SOME TEXT
examples = ['Free Viagra now!!!', "Hi Bob, how about a game of golf tomorrow?"]

#RETURNING TERM-DOCUMENT MATRIX 
example_counts = vectorizer.transform(examples)

#MAKING PREDICTIONS
predictions = classifier.predict(example_counts)
print(predictions)
