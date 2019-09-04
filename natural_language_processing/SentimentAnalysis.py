'''
This program uses vader algorithm for sentiment analysis on amazon reviews and calculates
accuracy, confusion matrix, recall, precision and F1 score.
'''

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# Loading vader
nltk.download('vader_lexicon')

# Loading data
df = pd.read_csv('/home/markjr/Documents/Data_science/natural_language_processing/amazonreviews.tsv', sep='\t')
print(df.head())

# Vader algorithm
sid = SentimentIntensityAnalyzer()

# Checking the data
print(df['label'].value_counts())

# Remove NaN values and empty sttings
df.dropna(inplace=True)

blanks = []  # start with an empty list

# Dealing with white space
for i,lb,rv in df.itertuples():  # iterate over the DataFrame
    if type(rv)==str:            # avoid NaN values
        if rv.isspace():         # test 'review' for whitespace
            blanks.append(i)     # add matching index numbers to the list

# Remove index with white space
df.drop(blanks, inplace=True)

# Checking the data
print(df['label'].value_counts())

# Creating column with vader scores
df['scores'] = df['review'].apply(lambda review: sid.polarity_scores(review))

# Creating column with compound score
df['compound']  = df['scores'].apply(lambda score_dict: score_dict['compound'])

# Check if is positive or negative
df['comp_score'] = df['compound'].apply(lambda c: 'pos' if c >=0 else 'neg')

# Checking the data
print(df.head())

# Get acurracy
print(accuracy_score(df['label'],df['comp_score']))

# Get precision, recall and F1 score
print(classification_report(df['label'],df['comp_score']))

# Get confusion matrix
print(confusion_matrix(df['label'],df['comp_score']))
