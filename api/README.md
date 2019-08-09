# Machine_Learning-Model-Flask-Deployment

## Description: 
Flask API demo project to show how Machine Learning Models are deployed on production

## Prerequisites:
- You must have python3 (Scikit Learn, Pandas) and Flask installed.
- Clone this repository to your computer.
- Access files .py inside folders.
- Make sure to check the correct path to access the data for each program.

## Project:

### Machine Learning Model: [model.py](https://github.com/markikojr/DataScience/blob/master/api/model.py)  
This contains code for our Machine Learning model to predict employee salaries on training data in 'hiring.csv' file.

### Flask API: [app.py](https://github.com/markikojr/DataScience/blob/master/api/app.py)  
This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.

### Request: [request.py](https://github.com/markikojr/DataScience/blob/master/api/request.py) 
This uses requests module to call APIs already defined in app.py and dispalys the returned value.

### HTML: [index.html](https://github.com/markikojr/DataScience/blob/master/api/templates/index.html) 
This folder contains the HTML template to allow user to enter employee detail and displays the predicted employee salary.

## Running the project
1) From the command line, execute: `python model.py` to create the model and the serialized version of model to model.pkl.
2) Execute: `python app.py` to start Flask API. Then navigate to URL generated. You should have a home page where you can insert values to predict salaries. 
3) You can also execute: `python request.py` to send direct POST requests to FLask API using Python's inbuilt request module Run the beow command to send the request with some pre-popuated values.

----------------------------
