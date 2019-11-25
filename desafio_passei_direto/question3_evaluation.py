'''This program is going to load the data students.json, premium_payments.json 
and evaluations.json in order to merge them together and get features to compare
premium to nopremium data.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.nice(10)

print("------ Load the data ------")
#Load the data
input_file1 = "/home/markjr/Documents/PasseiDireto/python/students.json"
df = pd.read_json(input_file1)
input_file2 = "/home/markjr/Documents/PasseiDireto/python/premium_payments.json"
df2 = pd.read_json(input_file2)
#input_file3 = "/home/markjr/Documents/PasseiDireto/python/studyPlanViews.json"
#df3 = pd.read_json(input_file3)
#input_file4 = "/home/markjr/Documents/PasseiDireto/python/fileViews.json"
#df4 = pd.read_json(input_file4)
input_file3 = "/home/markjr/Documents/PasseiDireto/python/evaluations.json"
df3 = pd.read_json(input_file3)

'''
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
'''

#Check the data
print("------ Check the data students.json ------")
#Check the data
print(df.head())
#print(df)
print(df.shape)
print(df.columns)
print(df.describe())

print("------ Check the data premium_payments.json ------")
#Check the data
print(df2.head())
print(df2.shape)
print(df2.columns)
print(df2.describe())

print("------ Check the data evaluations.json ------")
#Check the data
print(df3.head())
print(df3.shape)
print(df3.columns)
print(df3.describe())

'''
print("------ Check the data fileViews.json ------")
#Check the data
print(df4.head())
print(df4.shape)
print(df4.columns)
print(df4.describe())
'''

'''
# Get counts for each day range (5 days, 10 days and so on...)
print(np.max(df["RD"]))
print(np.min(df["RD"]))
print(np.max(df2["VD"]))
print(np.min(df2["VD"]))
'''

print("------ Merge the data students.json to premium_payments.json based on id ------")
# Merge df to df2 (outer)
#premium = pd.merge(df[['Id','RegisteredDate']],
#                    df2[['StudentId','PaymentDate']], left_on='Id',
#                    right_on='StudentId',how = 'outer', indicator=True)
data = pd.merge(df, 
	               df2, left_on='Id', 
	               right_on='StudentId',how = 'outer', indicator=True)

print("------ Delete dataframe ------")
# Delete dataframe
del df
del df2

print("------ Check merged data ------")
print(data.head())
print(data.shape)

print("------ Merge the data students.json + premium_payments.json to evaluations.json based on id ------")
# Merge df to df2 (outer)
data2 = pd.merge(data, 
	               df3, left_on='Id', 
	               right_on='StudentId',how = 'inner', indicator='exists')

print("------ Delete dataframe ------")
# Delete dataframe
del data
del df3

print("------ Check merged data ------")
print(data2.head())
print(data2.shape)


print("------ Create dataframe for premium and nopremium data ------")
# Dataframe for each university
nopremium = data2[data2['_merge'] == "left_only" ] 
premium = data2[data2['_merge'] == "both" ] 


print("------ Check nopremium data ------")
# Check the data
print(nopremium.head())
print(nopremium['PaymentDate'])


#print(data)
print(nopremium.shape)
print(nopremium.columns.values)
print(nopremium.describe())

print("------ Check premium data ------")
# Check the data
print(premium.head())
print(premium.shape)

#Get features
print("------ Count university occurence ------")
# Count university occurrence
print("------ Check nopremium ------")
print(nopremium['UniversityName'].value_counts())
print("------ Check premium ------")
print(premium['UniversityName'].value_counts())
print("------  ------")

print("------ Count course occurence ------")
# Count university occurrence
print("------ Check nopremium ------")
print(nopremium['CourseName'].value_counts())
print("------ Check premium ------")
print(premium['CourseName'].value_counts())
print("------  ------")

print("------ Count state occurence ------")
# Count university occurrence
print("------ Check nopremium ------")
print(nopremium['State'].value_counts())
print("------ Check premium ------")
print(premium['State'].value_counts())
print("------  ------")

print("------ Count city occurence ------")
# Count university occurrence
print("------ Check nopremium ------")
print(nopremium['City'].value_counts())
print("------ Check premium ------")
print(premium['City'].value_counts())
print("------  ------")

print("------ Count SignupSource occurence ------")
# Count university occurrence
print("------ Check nopremium ------")
print(nopremium['SignupSource'].value_counts())
print("------ Check premium ------")
print(premium['SignupSource'].value_counts())
print("------  ------")

#Get features
print("------ Check the evaluation type count ------")
print("------ Check nopremium ------")
print(nopremium['EvaluationType'].value_counts())
print("------ Check premium ------")
print(premium['EvaluationType'].value_counts())
print("------  ------")

print("------ Check the evaluated object type count ------")
print("------ Check nopremium ------")
print(nopremium['EvaluatedObjectType'].value_counts())
print("------ Check premium ------")
print(premium['EvaluatedObjectType'].value_counts())
print("------  ------")


print("------ Check the dislike nopremium evaluated object type count ------")
dislikenp = nopremium[nopremium['EvaluationType'] == 'Dislike' ]
print("------ Check nopremium ------")
print(dislikenp['EvaluatedObjectType'].value_counts())
print(dislikenp['EvaluatedObjectType'].value_counts().sum())
print("------  ------")

print("------ Check the dislike premium evaluated object type count ------")
dislikep = premium[premium['EvaluationType'] == 'Dislike' ]
print("------ Check premium ------")
print(dislikep['EvaluatedObjectType'].value_counts())
print(dislikep['EvaluatedObjectType'].value_counts().sum())
print("------  ------")


'''
print("------ Count Topic occurence ------")
# Count university occurrence
print("------ Check nopremium ------")
print(nopremium['Topic'].value_counts())
print("------ Check nopremium ------")
print(premium['Topic'].value_counts())
print("------  ------")


print("------ Count Subject occurence ------")
# Count university occurrence
print("------ Check nopremium ------")
print(nopremium['Subject'].value_counts())
print("------ Check nopremium ------")
print(premium['Subject'].value_counts())
print("------  ------")
'''