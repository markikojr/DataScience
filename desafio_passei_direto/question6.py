'''This program is going to load the data students.json and fileViews.json in order to get 
merge them in a single dataframe to get features from university and files'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.nice(10)

print("------ Load the data ------")
#Load the data
input_file1 = "/home/markjr/Documents/PasseiDireto/python/students.json"
df = pd.read_json(input_file1)
input_file2 = "/home/markjr/Documents/PasseiDireto/python/fileViews.json"
df2 = pd.read_json(input_file2)

'''
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
'''

print("------ Check the data students.json ------")
#Check the data
print(df.head())
#print(df)
print(df.shape)
print(df.columns)
print(df.describe())

print("------ Check the data fileViews.json ------")
#Check the data
print(df2.head())
print(df2.shape)
print(df2.columns)
print(df2.describe())

print("------ Count university occurence ------")
# Count university occurrence
print(df['UniversityName'].value_counts())


# Convert to timestamp
df['RegisteredDate'] = pd.to_datetime(df['RegisteredDate'])
df2['ViewDate'] = pd.to_datetime(df2['ViewDate'])

# Select only date (without hours)
df['RD'] = df['RegisteredDate'].dt.date
df2['VD'] = df2['ViewDate'].dt.date

# Check the data
print(df.head())
print(df2.head())

# Get counts for each day range (5 days, 10 days and so on...)
print(np.max(df["RD"]))
print(np.min(df["RD"]))
print(np.max(df2["VD"]))
print(np.min(df2["VD"]))

print("------ Merge the data students.json to fileViews.json based on id ------")
# Merge df to df2 (inner by default)
data = pd.merge(df, df2, left_on='Id', right_on='StudentId')

print("------ Delete dataframe ------")
# Delete dataframe
del df
del df2

print("------ Check merged data ------")
# Check the data
print(data.head())
#print(data)
print(data.shape)
print(data.columns.values)
print(data.describe())

print("------ Create dataframe for each university ------")
# Dataframe for each university
Estacio = data[data['UniversityName'] == "ESTÁCIO"] 
Unip = data[data['UniversityName'] == "UNIP"]
Unopar = data[data['UniversityName'] == "UNOPAR"]
Uninter = data[data['UniversityName'] == "UNINTER"]
Ead = data[data['UniversityName'] == "ESTÁCIO EAD"] 

#Get features 
print("------ Check Estacio data ------")
print(Estacio[['Id','UniversityName','FileName']].head())
print("------ Count file occurence ------")
print(Estacio['FileName'].value_counts())
print(Estacio['FileName'].value_counts().sum())

print("------ Check Unip data ------")
print(Unip[['Id','UniversityName','FileName']].head())
print("------ Count file occurence ------")
print(Unip['FileName'].value_counts())
print(Unip['FileName'].value_counts().sum())

print("------ Check Unopar data ------")
print(Unopar[['Id','UniversityName','FileName']].head())
print("------ Count file occurence ------")
print(Unopar['FileName'].value_counts())
print(Unopar['FileName'].value_counts().sum())

print("------ Check Uninter data ------")
print(Uninter[['Id','UniversityName','FileName']].head())
print("------ Count file occurence ------")
print(Uninter['FileName'].value_counts())
print(Uninter['FileName'].value_counts().sum())

print("------ Check Estacio EAD data ------")
print(Ead[['Id','UniversityName','FileName']].head())
print("------ Count file occurence ------")
print(Ead['FileName'].value_counts())
print(Ead['FileName'].value_counts().sum())




