'''
This code will create a flask api (twitter sentiment analysis) to receive tweets 
and predict whether it's positive, neutral or negative. It is going to use vader
to predict sentiment.
'''

# -*- coding: utf-8 -*-
from textblob import TextBlob as tb
import tweepy
import numpy as np
from numpy import median
from numpy import mean
import pandas as pd
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#Set up vader analyzer
analyzer = SentimentIntensityAnalyzer()
nltk.download('vader_lexicon')

#Get vader scores
def get_vader_score(sentence):
    score = analyzer.polarity_scores(sentence)

    return score['compound'], score['pos'], score['neg'], score['neu']

#CREATING AN INSTANCE OF THE FLASK CLASS
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

#DECORATOR (WHERE THE URL IS '/predict', AND HANDLE POST REQUESTS)
@app.route('/predict',methods=['POST'])
def predict():

    #Define key and token
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    #Handle authority
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #Define subject/person, number of tweets, start/end date(year-month-day)
    politician_name = "emmanuelmacron"
    search = "Brazil"
    number_of_tweets = 200
    end_date = '2019-08-02'

    #ACCESSING COMMENTS FROM WEB API
    if request.method == 'POST': 
       search           = request.form['search']
       end_date         = request.form['end_date']
       number_of_tweets = request.form['ntweets']
       number_of_tweets = int(number_of_tweets)

       #Use this to check tweets from a person
       #tweets = tweepy.Cursor(api.user_timeline, screen_name=politician_name, count = 100).items(number_of_tweets)

       #Use this to check tweets about a person or something
       tweets = tweepy.Cursor(api.search, q=search, lang="en", until=end_date).items(number_of_tweets)

       #Create dictionary
       user_dict = {'tweets': []}

       #Number of positives, negatives and neutrals
       pos = 0
       neg = 0
       neu = 0

       #Get tweets, vader scores, user name, location, save json
       try:  
          for tweet in tweets:  
              tweet_dict = {}
              tweet_dict['created'] = tweet.created_at
              tweet_dict['text'] = tweet.text
              tweet_dict['location'] = tweet.user.location
              tweet_dict['user'] = tweet.user.screen_name
              compound, positive, negative, neutral = get_vader_score(tweet.text) #vader scores
              tweet_dict['score'] = compound
              tweet_dict['Pos'] = positive
              tweet_dict['Neg'] = negative
              tweet_dict['Neu'] = neutral
              user_dict['tweets'].append(tweet_dict)

              n = compound
              float(n)
              if n >= 0.05:
                 pos+=1
              elif n <= -0.05:
                 neg+=1
              else:
                 neu+=1

          #Get number of positives, negatives and neutrals
          number_of_positives = pos        
          number_of_negatives = neg        
          number_of_neutrals = neu        
          #Get number of tweets and score average(positive: compound score >= 0.05, neutral: -0.05 < compound score < 0.05, negative: compound score <= -0.05)
          num_of_tweets = len(user_dict['tweets'])
          num_of_tweets = int(num_of_tweets)
          mean_score = mean([tweet['score'] for tweet in user_dict['tweets']])

       except tweepy.TweepError:  
              time.sleep(60)

    #RENDERING .HTML
    return render_template('results.html', search = search, end_date = end_date, mean_score = mean_score ,num_of_tweets = num_of_tweets, tweet_dict = user_dict, number_of_positives = number_of_positives, number_of_negatives = number_of_negatives, number_of_neutrals = number_of_neutrals)

if __name__ == "__main__":
    app.run(debug=True)
