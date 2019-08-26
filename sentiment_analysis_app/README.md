# Machine_Learning-Model-Flask-Deployment to Heroku

## Description: 
Machine Learning Flask API project (Sentiment Analysis) deployed to Heroku on production

## Prerequisites:
- You must have python3 (Scikit Learn, Pandas), Flask and Heroku installed.
- Clone this repository to your computer.
- Access files .py inside folders.
- Make sure to check the correct path to access the data for each program.

## Project:

### Machine Learning Model: [model.py](https://github.com/markikojr/DataScience/blob/master/sentimentanalysisapp/model.py)  
This contains code for our Machine Learning model to predict whether a comment is positive or negative. Sentences come from three different websites: imdb.com, amazon.com and yelp.com

### Flask API: [app.py](https://github.com/markikojr/DataScience/blob/master/sentimentanalysisapp/app.py)  
This contains Flask APIs that receives the sentence through GUI or API calls, and predict the sentiment based on our model and returns it.

### HTML: [index.html](https://github.com/markikojr/DataScience/blob/master/sentimentanalysisapp/templates/index.html) 
This folder contains the HTML template to allow user to enter details and displays the predicted sentiment.

### Application can be found here: [App](https://sentimentanalysisapplication.herokuapp.com)  
This contains the app deployed to heroku.

## Running the project
1) To create the model and the serialized version of model to model.pkl, execute: `python model.py`
2) To start Flask API execute: `python app.py` 
3) Then navigate to URL generated. You should have a home page where you can insert text to predict.
4) Preparing heroku using git. Execute `git init`, `git add .`, and `git commit -m "creating app"`.
5) Login to heroku: `heroku login`
6) Create app: `heroku apps:create appname`. Name should be unique.
7) Deploy: `git push heroku master`
8) Dyno: `heroku ps:scale web=1`
9) Open app: `heroku open` 

----------------------------
