# Machine_Learning-Model-Flask

## Description: 
Flask API project to show how Machine Learning Models are built.

## Prerequisites:
- You must have python3 (Scikit Learn, Pandas) and Flask installed.
- Clone this repository to your computer.
- Access files .py inside folders.
- Make sure to check the correct path to access the data for each program.

## Project:

### Machine Learning Model: [model.py](https://github.com/markikojr/DataScience/blob/master/sentiment_classifier_api/model.py)  
This contains code for our Machine Learning model to predict whether a comment is positive or negative. Sentences come from three different websites: imdb.com, amazon.com and yelp.com

### Flask API: [app.py](https://github.com/markikojr/DataScience/blob/master/sentiment_classifier_api/app.py)  
This contains Flask APIs that receives the sentence through GUI or API calls, and predict the sentiment based on our model and returns it.

### HTML: [index.html](https://github.com/markikojr/DataScience/blob/master/sentiment:classifier_api/templates/index.html) 
This folder contains the HTML template to allow user to enter details and displays the predicted sentiment.

## Running the project
1) To create the model and the serialized version of model to model.pkl, execute: `python model.py`
2) To start Flask API execute: `python app.py` 
3) Then navigate to URL generated. You should have a home page where you can insert text. 

----------------------------
