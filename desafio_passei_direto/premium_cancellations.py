'''This program is going to load the data premium_cancellations.json in order to get 
features from cancellation'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("------ Load the data ------")
#Load the data
input_file = "/home/markjr/Documents/PasseiDireto/python/premium_cancellations.json"
df = pd.read_json(input_file)

'''
#SET THE NUMBER OF ROWS AND COLUMNS TO DISPLAY
#pd.set_option('max_rows', 20, 'max_columns', 10)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
'''
time = 'CancellationDate'

print("------ Check the data ------")
#Check the data
print(df.head())
#print(df)
print(df.shape)
print(df.describe())
print(df.columns)
#df.dropna(inplace=True)

# Convert to timestamp
df[time] = pd.to_datetime(df[time])

# Select only date (without hours)
df['ymddate'] = df[time].dt.date

#Get features
print("------ Check the date count ------")
print(df['ymddate'].value_counts())

print("------ Check the date sum ------")
print(df['ymddate'].value_counts().sum())

print("------ Check the min date ------")
print(np.min(df["ymddate"]))

print("------ Check the max date ------")
print(np.max(df["ymddate"]))

print("------ Check the duplicated cancellations ------")
print(df['StudentId'].value_counts())



print("------ Check cancellations per day from november 2017 on ------")
# From november on
Nov2017 = df[df['ymddate'] >= pd.Timestamp(2017,11,1)]
print(Nov2017.head())
print(Nov2017.shape)
print(Nov2017.columns)
print(Nov2017.describe())
print("------ Check the date sum ------")
print(Nov2017['ymddate'].value_counts().sum())


print("------ Check cancellations per day for each month from 05/2016 to 06/2018 ------")
#Cancellations per day for each month from 05/2016 to 06/2018 
year_list = [2016, 2017, 2018]
month_list = ["January", "February", "march", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
my_list = [0,1,2,3,4,5,6,7,8,9,10,11]
my_list2 = [1,2,3,4,5,6,7,8,9,10,11,12]
my_list3 = []

# From from before to after
for y in year_list:
     for i, j in zip(my_list, my_list2):
            before = pd.Timestamp(y,j,1)
            if (before == pd.Timestamp(2018,7,1)):  
                 break   
            if (before == pd.Timestamp(2016,4,1)):
                 continue               
            if (y == 2016 and i < 4) or (y == 2018 and i > 6):
                 continue   
            if j == 12:   
                 after = pd.Timestamp(y+1,1,1)                                           	
            else: 
                 after = pd.Timestamp(y,j+1,1)
                
            data = df[(df['ymddate'] >= before) & (df['ymddate'] < after)] 
            my_list3.append(data['ymddate'].value_counts().sum())
            print(y, month_list[i],":",data['ymddate'].value_counts().sum())
            
            del data


print("------ Check cancellations for each month from 05/2016 to 06/2018 sum ------")
print(sum(my_list3))