'''This program is going to load the data premium_payments.json in order to get 
features from payments and plan type'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("------ Load the data ------")
#Load the data
input_file = "/home/markjr/Documents/PasseiDireto/python/premium_payments.json"
df = pd.read_json(input_file)

'''
#SET THE NUMBER OF ROWS AND COLUMNS TO DISPLAY
#pd.set_option('max_rows', 20, 'max_columns', 10)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
'''
time = 'PaymentDate'

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

print("------ Check the plan type count ------")
print(df['PlanType'].value_counts())

# Dates
nov = pd.Timestamp(2017,11,1)
dec = pd.Timestamp(2017,12,1)
jan = pd.Timestamp(2018,1,1)
feb = pd.Timestamp(2018,2,1)
out = pd.Timestamp(2017,10,1)
sept = pd.Timestamp(2017,9,1)

print("------ Check payments per day from november 2017 on ------")
# From november on
Nov2017 = df[df['ymddate'] >= nov]
print(Nov2017.head())
print(Nov2017.shape)
print(Nov2017.columns)
print(Nov2017.describe())
print("------ Check the date sum ------")
print(Nov2017['ymddate'].value_counts().sum())

'''
print("------ Check payments per day for sept, oct, nov, dec 2017 and jan 2018 ------")
# From september to october
sept2017 = df[(df['ymddate'] >= sept) & (df['ymddate'] < out)] 
print("September:",sept2017['ymddate'].value_counts().sum())
print(sept2017['PlanType'].value_counts())
# From october to november
oct2017 = df[(df['ymddate'] >= out) & (df['ymddate'] < nov)] 
print("October:",oct2017['ymddate'].value_counts().sum())
print(oct2017['PlanType'].value_counts())
# From november to december
Nov22017 = df[(df['ymddate'] >= nov) & (df['ymddate'] < dec)] 
print("November:",Nov22017['ymddate'].value_counts().sum())
print(Nov22017['PlanType'].value_counts())
# From december to january
dec2017 = df[(df['ymddate'] >= dec) & (df['ymddate'] < jan)] 
print("December:",dec2017['ymddate'].value_counts().sum())
print(dec2017['PlanType'].value_counts())
# From from january to february
jan2018 = df[(df['ymddate'] >= jan) & (df['ymddate'] < feb)] 
print("January:",jan2018['ymddate'].value_counts().sum())
print(jan2018['PlanType'].value_counts()) 


date_list = [sept, out, nov, dec, jan, feb]
month_list = ["September", "October", "November", "December", "January", "February"]
my_list = [0,1,2,3,4,5,6]
# From from before to after
for i, m in zip(my_list, month_list):
     before = date_list[i]
     if before ==  date_list[-1]:
         break             	
     after = date_list[i+1]
     data = df[(df['ymddate'] >= before) & (df['ymddate'] < after)] 
     print(month_list[i],":",data['ymddate'].value_counts().sum())
     print(data['PlanType'].value_counts()) 
     del data
'''
print("------ Check payments per day for each month from 05/2016 to 06/2018 ------")
#Payments per day for each month from 05/2016 to 06/2018 
year_list = [2015, 2016, 2017, 2018]
month_list = ["January", "February", "march", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
my_list = [0,1,2,3,4,5,6,7,8,9,10,11]
my_list2 = [1,2,3,4,5,6,7,8,9,10,11,12]
my_list3 = []
my_list4 = []

# From from before to after
for y in year_list:
     for i, j in zip(my_list, my_list2):
            before = pd.Timestamp(y,j,1)
            if (before == pd.Timestamp(2018,7,1)):  
                 break   
            #if (before == pd.Timestamp(2016,4,1)):
            #     continue               
            #if (y == 2016 and i < 4) or (y == 2018 and i > 6) or (y == 2015 and j < 8):
            if (y == 2018 and i > 6) or (y == 2015 and j < 8):
                 continue   
            if j == 12:   
                 after = pd.Timestamp(y+1,1,1)    
                                                    	
            if j != 12: 
                 after = pd.Timestamp(y,j+1,1)
                     
            
            # monthly count    
            data = df[(df['ymddate'] >= before) & (df['ymddate'] < after)]
            my_list3.append(data['ymddate'].value_counts().sum())
            print(y, "in ",month_list[i],":",data['ymddate'].value_counts().sum())
            
            if (y == 2018 and j == 6):
                 before = pd.Timestamp(2018,6,7) 
            if (y == 2016 and j < 5):
                 continue
            # up to month count
            datanew = df[(df['ymddate'] <= before)] 
            my_list4.append(datanew['ymddate'].value_counts().sum())
            print(y, "up to ",month_list[i],":",datanew['ymddate'].value_counts().sum())
            #print(month_list[i],":",datanew['ymddate'].value_counts().sum())
            del datanew
                 
            del data
            


print("------ Check total payments from 05/2016 to 06/2018 ------")
print(sum(my_list3))
print(sum(my_list4))