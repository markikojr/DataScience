'''
This program creates a model to predict employee salaries from the 'hiring.csv' data
and creates a serialized version of model to a model.pkl.
The data contains informations such as 'experience', 'test_score', 'interview_score' and 'salary'
'''

#IMPORTING LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#LOADING THE DATA
dataset = pd.read_csv('/home/markjr/Documents/Data_science/api/hiring.csv')

#DEALING WITH NAN VALUES (IN THIS CASE REPRESENTING NO EXPERIENCE)
dataset['experience'].fillna(0, inplace=True)

#DEALING WITH NAN VALUES FILLNA WITH MEAN
dataset['test_score'].fillna(dataset['test_score'].mean(), inplace=True)

#FEATURES(EXPERIENCE, TEST_SCORE AND INTERVIEW_SCORE)
X = dataset.iloc[:, :3]

#CONVERTING WORDS TO INTEGER VALUE(EXPERIENCE FEATURE)
def convert_to_int(word):
    word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
                'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
    return word_dict[word]

X['experience'] = X['experience'].apply(lambda x : convert_to_int(x))

#SALARY
y = dataset.iloc[:, -1]

#SPLITTING TRAIN AND TEST
#SINCE WE HAVE A VERY SMALL DATASET, WE WILL TRAIN OUR MODEL WITH ALL AVAILABLE DATA

#FITTING MODEL WITH TRAIN DATA
regressor.fit(X, y)

#SAVING MODEL TO DISK
pickle.dump(regressor, open('model.pkl','wb'))

#LOADING MODEL
model = pickle.load(open('model.pkl','rb'))

#MAKING SOME PREDICTION
print(model.predict([[2, 9, 6]])) #EXPERIENCE-2, TEST_SCORE-9, INTERVIEW_SCORE-6