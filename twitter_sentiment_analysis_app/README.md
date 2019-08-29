# Twitter-Data-Mining-Flask-Deployment to Heroku

## Description: 
 Flask API project (Twitter Sentiment Analysis) deployed to Heroku on production

## Prerequisites:
- You must have python3 (Scikit Learn, Pandas, Tweepy and NLTK), Flask and Heroku installed.
- Clone this repository to your computer.
- Access files .py inside folders.
- Make sure to check the correct path to access the data for each program.

## Project:

### Flask API: [app.py](https://github.com/markikojr/DataScience/blob/master/twitter_sentiment_analysis_app/app.py)  
This contains Flask APIs that receives the search, startdate, enddate and number of tweets through GUI, predicts the sentiment based on model and returns whether a tweet is positive, negative or neutral.

### Home HTML: [home.html](https://github.com/markikojr/DataScience/blob/master/twitter_sentiment_analysis_app/templates/home.html) 
This folder contains the HTML template to allow user to enter details and predict sentiment.

### Results HTML: [results.html](https://github.com/markikojr/DataScience/blob/master/twitter_sentiment_analysis_app/templates/results.html) 
This folder contains the HTML template to display the predicted sentiment.

### Application can be found here: [App](https://twitteranalysisapplication.herokuapp.com)  
This contains the app deployed to heroku.

## Running the project
1) Create an account and create Twitter API Authentication Credentials. More info:[Credentials](https://realpython.com/twitter-bot-python-tweepy)  
2) To start Flask API execute: `python app.py`. Make sure to change the twitter credencials. 
3) Then navigate to URL generated. You should have a home page where you can insert text to predict.
4) Preparing heroku using git. Execute `git init`, `git add .`, and `git commit -m "creating app"`.
5) you should have Procfile, requirements.txt and nltk.txt files to run the project
6) Login to heroku: `heroku login`. You should go to Heroku home page and create account first.
7) Create app: `heroku apps:create appname`. Name should be unique.
8) Deploy: `git push heroku master`
9) Dyno: `heroku ps:scale web=1`
10) Open app: `heroku open` 

----------------------------
