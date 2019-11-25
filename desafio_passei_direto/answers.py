'''This program is going to load the data answers.json in order to get 
features about answers and login'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("------ Load the data ------")
#Load the data
input_file = "/home/markjr/Documents/PasseiDireto/python/answers.json"
df = pd.read_json(input_file)

'''
#SET THE NUMBER OF ROWS AND COLUMNS TO DISPLAY
pd.set_option('max_rows', 20, 'max_columns', 10)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
'''
time = 'AnswerDate'

print("------ Check the data ------")
#Check the data
print(df.head())
#print(df)
print(df.shape)
print(df.describe())
print(df.columns)

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

print("------ Check the studentclient count ------")
print(df['StudentClient'].value_counts())

# Dates
nov = pd.Timestamp(2017,11,1)
dec = pd.Timestamp(2017,12,1)
jan = pd.Timestamp(2018,1,1)
feb = pd.Timestamp(2018,2,1)
out = pd.Timestamp(2017,10,1)
sept = pd.Timestamp(2017,9,1)

print("------ Check answers per day from november 2017 on ------")
# From november on
Nov2017 = df[df['ymddate'] >= nov]
print(Nov2017.head())
print(Nov2017.shape)
print(Nov2017.columns)
print(Nov2017.describe())
print("------ Check the date sum ------")
print(Nov2017['ymddate'].value_counts().sum())


print("------ Check answers per day for sept, oct, nov, dec 2017 and jan 2018 ------")
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
 
print("------ Check answers for each month from 02/2017 to 06/2018 ------")
#answers for each month from 02/2017 to 06/2018 
year_list = [2017, 2018]
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
            if (before == pd.Timestamp(2017,1,1)):
                 continue               
            #if (y == 2017 and i < 2) or (y == 2018 and i > 6):
            #    continue   
            if j == 12:   
                 after = pd.Timestamp(y+1,1,1)                                           	
            else: 
                 after = pd.Timestamp(y,j+1,1)
            #print(before)    
            #print(after)    
            data = df[(df['ymddate'] >= before) & (df['ymddate'] < after)] 
            my_list3.append(data['ymddate'].value_counts().sum())
            print(y, month_list[i],":",data['ymddate'].value_counts().sum())
            
            del data


print("------ Check answers for each month from 02/2017 to 06/2018 sum ------")
print(sum(my_list3))




