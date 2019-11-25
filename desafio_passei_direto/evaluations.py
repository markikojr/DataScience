'''This program is going to load the data evaluations.json in order to get 
features from evaluation, evaluation object and access type'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("------ Load the data ------")
#Load the data
input_file = "/home/markjr/Documents/PasseiDireto/python/evaluations.json"
df = pd.read_json(input_file)

'''
#SET THE NUMBER OF ROWS AND COLUMNS TO DISPLAY
#pd.set_option('max_rows', 20, 'max_columns', 10)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
'''

print("------ Check the data ------")
#Check the data
print(df.head())
#print(df)
print(df.shape)
print(df.describe())
print(df.columns)

#Get features
print("------ Check the evaluation type count ------")
print(df['EvaluationType'].value_counts())

print("------ Check the evaluated object type count ------")
print(df['EvaluatedObjectType'].value_counts())

print("------ Check the student client count ------")
print(df['StudentClient'].value_counts())

print("------ Check the dislike evaluated object type count ------")
dislike = df[df['EvaluationType'] == 'Dislike' ]
print(dislike['EvaluatedObjectType'].value_counts())
print(dislike['EvaluatedObjectType'].value_counts().sum())







