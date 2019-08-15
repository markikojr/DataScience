'''
This code will create a flask api (sentiment analysis) to receive comments and predict whether it's positive or negative.
'''

# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB

#CREATING AN INSTANCE OF THE FLASK CLASS
app = Flask(__name__)

#PATH TO LOAD THE LIST
directory = "/home/markjr/Documents/Data_science/sentiment_classifier_api/"

@app.route('/')
def home():
    return render_template('index.html')

#DECORATOR (WHERE THE URL IS '/predict', AND HANDLE POST REQUESTS)
@app.route('/predict',methods=['POST'])
def predict():
    '''
    Function for rendering results on HTML GUI
    '''
    #LOADING THE TRAIN_ INFO TO BUILD THE MODEL
    with open (directory + "outfile", "rb") as fp:
         train_ = pickle.load(fp)

    #DEFINING VECTORIZER
    vectorizer = CountVectorizer(binary = 'true')   
 
    #LOADING COMMENTS AND LABELS
    sentence = [train[0] for train in train_]
    label = [train[1] for train in train_]

    #FIT AND TRANSFORM COMMENTS
    sentence = vectorizer.fit_transform(sentence)

    #BUILDING THE MODEL
    classifier = BernoulliNB().fit(sentence, label)

    #ACCESSING COMMENTS FROM WEB API
    if request.method == 'POST': 
       comment = request.form['comment']
       data = [comment]

       #VECTORIZING
       vector = vectorizer.transform(data).toarray()

       #PREDICTING WITH MODEL
       prediction = classifier.predict(vector)
       output = prediction

       #TRANSLATING RESULT TO POSITIVE OR NEGATIVE
       m = ""
       for n in output:
           n = int(n)
           if n == 1: m = "Positve"
           else:      m = "Negative"

    #RENDERING .HTML
    return render_template('index.html', prediction_text = 'This comment "{}" is classified as {}.'.format(comment, m))

if __name__ == "__main__":
    app.run(debug=True)
