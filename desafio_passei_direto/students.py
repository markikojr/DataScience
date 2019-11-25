'''This program is going to load the data students.json in order to get 
features from University, course, state, city and login'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("------ Load the data ------")
#Load the data
input_file = "/home/markjr/Documents/PasseiDireto/python/students.json"

df = pd.read_json(input_file)

#SET THE NUMBER OF ROWS AND COLUMNS TO DISPLAY
pd.set_option('max_rows', 20, 'max_columns', 10)

time = 'RegisteredDate'

print("------ Check the data students.json ------")
#Check the data
print(df.head())
print(df.shape)
print(df.describe())
print(df.columns)

# Convert to timestamp
df[time] = pd.to_datetime(df[time])

# Select only date (without hours)
df['ymddate'] = df[time].dt.date

#Get some features
print("------ Check the date count ------")
print(df['ymddate'].value_counts())

print("------ Check the date sum ------")
print(df['ymddate'].value_counts().sum())

print("------ Check the min date ------")
print(np.min(df["ymddate"]))

print("------ Check the max date ------")
print(np.max(df["ymddate"]))

print("------ Check the sgnupSource count ------")
print(df['SignupSource'].value_counts())

print("------ Check the  university count ------")
print(df['UniversityName'].value_counts())

print("------ Check the state count ------")
print(df['State'].value_counts())
students.json
print("------ Check the city count ------")
print(df['City'].value_counts())

print("------ Check the coursename count ------")
print(df['CourseName'].value_counts())

print("------ Check the studentclient count ------")
print(df['StudentClient'].value_counts())

# Dates
nov = pd.Timestamp(2017,11,1)
dec = pd.Timestamp(2017,12,1)
jan = pd.Timestamp(2018,1,1)
feb = pd.Timestamp(2018,2,1)
out = pd.Timestamp(2017,10,1)
sept = pd.Timestamp(2017,9,1)

print("------ Check registrations per day from november 2017 on ------")
# From november on
Nov2017 = df[df['ymddate'] >= nov]
print(Nov2017.head())
print(Nov2017.shape)
print(Nov2017.columns)students.json
print(Nov2017.describe())
print("------ Check the date sum ------")
print(Nov2017['ymddate'].value_counts().sum())


print("------ Check registrations per day for sept, oct, nov, dec 2017 and jan 2018 ------")
# From september to october
sept2017 = df[(df['ymddate'] >= sept) & (df['ymddate'] < out)] 
print("September:",sept2017['ymddate'].value_counts().sum())
# From october to november
oct2017 = df[(df['ymddate'] >= out) & (df['ymddate'] < nov)] 
print("October:",oct2017['ymddate'].value_counts().sum())
# From november to december
Nov22017 = df[(df['ymddate'] >= nov) & (df['ymddate'] < dec)] 
print("November:",Nov22017['ymddate'].value_counts().sum())
# From december to january
dec2017 = df[(df['ymddate'] >= dec) & (df['ymddate'] < jan)] 
print("December:",dec2017['ymddate'].value_counts().sum())
# From from january to february
jan2018 = df[(df['ymddate'] >= jan) & (df['ymddate'] < feb)] 
print("January:",jan2018['ymddate'].value_counts().sum())

