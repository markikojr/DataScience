# -*- coding: utf-8 -*-
'''
This program creates a model using Naive Bayes  
to classify sentiment as positive or negative on sentences
'''

#IMPORTING LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

directory = "/home/markjr/Documents/Data_science/sentiment_classifier_api/"

#LOADING THE DATA
def data_from_source():

    with open(directory + "imdb_labelled.txt", "r") as text:
        data = text.read().split('\n')

    with open(directory + "amazon_cells_labelled.txt", "r") as text:
        data += text.read().split('\n')

    with open(directory + "yelp_labelled.txt", "r") as text:
        data += text.read().split('\n')

    return data

#CLEANING THE DATA
def cleaning(data):
    cleaned_data = []
    for d in data:
        if len(d.split("\t")) == 2 and d.split("\t")[1] != "":
            cleaned_data.append(d.split("\t"))

    return cleaned_data

#SPLITTING THE DATA
def split_data(data):
    total = len(data)
    percentage_train = 0.75
    train = []
    validation = []

    for indice in range(0, total):
        if indice < total * percentage_train:
            train.append(data[indice])
        else:
            validation.append(data[indice])

    return train, validation
    
#DATA PRE-PROCESSING    
def pre_processing():
    data = data_from_source()
    cleaned_data = cleaning(data)

    return split_data(cleaned_data)

#DATA PRE-PROCESSING (MODEL BUILDING)
def model_building(train_, vectorizer):
    sentence = [train[0] for train in train_]
    label = [train[1] for train in train_]
    sentence = vectorizer.fit_transform(sentence)

    return BernoulliNB().fit(sentence, label)

#RESULTS
def result(value):
    sentence, result = value
    result = "Positive sentence" if result[0] == '1' else "Negative sentence"
    print(sentence, ":", result)

#ANALYZER
def sentiment_analyzer(classifier, vectorizer, sentence):
    return sentence, classifier.predict(vectorizer.transform([sentence]))
    
#DATA PROCESSING
train_, validation = pre_processing()
vectorizer = CountVectorizer(binary = 'true')
classifier = model_building(train_, vectorizer)
print(vectorizer)
print(train_)

#SAVING TRAIN_ INFO TO OUTPUT FILE
with open(directory + "outfile", "wb") as fp:
    pickle.dump(train_, fp)

#RESULTS FOR SOME EXAMPLES
#result = classifier.predict(vectorizer.transform(["love this movie!"]))    
result( sentiment_analyzer(classifier, vectorizer,"this is the best movie"))
result( sentiment_analyzer(classifier, vectorizer,"this is the worst movie"))
result( sentiment_analyzer(classifier, vectorizer,"awesome!"))

#SAVING MODEL TO DISK
pickle.dump(classifier, open('model.pkl','wb'))

def metrics(train_, vectorizer):
    sentence = [train[0] for train in train_]
    label = [train[1] for train in train_]
    sentence = vectorizer.fit_transform(sentence)
    prediction = classifier.predict(sentence)
    accuracy = accuracy_score(label, prediction)
    cm = confusion_matrix(label, prediction)
    report = classification_report(label, prediction)

    return accuracy, cm, report 

accuracy, confusion_matrix_, report = metrics(train_, vectorizer)
#accuracy, confusion_matrix_, report = metrics(validation, vectorizer)

print("Accuracy: ", accuracy)
print("Confusion_matrix:", "\n", confusion_matrix_)
print("Other_metrics:", "\n", report)

#PRECENTAGE HITS
def validation_(validation):
    sentences = [val[0] for val in validation]
    label   =   [val[1] for val in validation]

    total = len(sentences)
    hits = 0

    for indice in range(0, total):
        result_ = sentiment_analyzer(classifier, vectorizer, sentences[indice])
        sentence, result = result_
        hits += 1 if result[0] == label[indice] else 0

    return hits * 100 / total

#TRUE POSITIVE, TRUE NEGATIVE, FALSE POSITIVE, FALSE NEGATIVE
def validation2_(validation):
    sentences = [val[0] for val in validation]
    label   =   [val[1] for val in validation]


    total = len(sentences)
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0

    for indice in range(0, total):
        result_ = sentiment_analyzer(classifier, vectorizer, sentences[indice])
        sentence, result = result_
        if result[0] == '0':
            true_negative += 1 if label[indice] == '0' else 0
            false_negative += 1 if label[indice] != '0' else 0
        else:
            true_positive += 1 if label[indice] == '1' else 0
            false_positive += 1 if label[indice] != '1' else 0

    return ( true_positive * 100 / total, 
             true_negative * 100 / total,
             false_positive * 100 / total,
             false_negative * 100 / total
           )

percentage_hits = validation_(validation)
true_positive,true_negative,false_positive,false_negative = validation2_(validation)

#PRINTTING METRICS
print("Model has", percentage_hits, "% hits")

print(true_positive, "% are true positives")
print(true_negative, "% are true negatives")

print(false_positive, "% are false positives")
print(false_negative, "% are false negatives")
