'''
Question1:
This program is going to load the premium_students.json data in order to get 
the probabilities from Registered/Subscription relation from clients and plot the result
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

#Load the data
input_file = "/home/markjr/Documents/PasseiDireto/python/premium_students.json"
df = pd.read_json(input_file)

time = 'RegisteredDate'

#Check the data
print(df.head())
print(df.shape)

# Convert to timestamp
df['RegisteredDate'] = pd.to_datetime(df['RegisteredDate'])
df['SubscriptionDate'] = pd.to_datetime(df['SubscriptionDate'])

# Select only date (without hours)
df['RD'] = df['RegisteredDate'].dt.date
df['SD'] = df['SubscriptionDate'].dt.date

# Get days from registration to subscription
df['Range'] = (df['SD'] - df['RD']).dt.days

# Check the data
print(df.head())
print(df.shape)
print(df.describe())

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

# Define counts
N0_5 = N5_10 = N10_15 = N15_30 = N30_60 = N60_90 = N90_120 = N120_150 = N150_180 =  N180_ = 0

# Define total
N = 6260

# Get counts for each day range (5 days, 10 days and so on...)
N0_5 = np.sum((df["Range"]<5))
N5_10 = np.sum((df["Range"]>5) & (df["Range"]<10))
N10_15 = np.sum((df["Range"]>10) & (df["Range"]<15))
N15_30 = np.sum((df["Range"]>15) & (df["Range"]<30))
N30_60 = np.sum((df["Range"]>30) & (df["Range"]<60))
N60_90 = np.sum((df["Range"]>60) & (df["Range"]<90))
N90_120 = np.sum((df["Range"]>90) & (df["Range"]<120))
N120_150 = np.sum((df["Range"]>120) & (df["Range"]<150))
N150_180 = np.sum((df["Range"]>150) & (df["Range"]<180))
N180_ = np.sum(df["Range"]>180)

# Max difference in days
nmax = df['Range'].max()
print("Higher difference in days:",nmax)

# Print results
print("Number of counts for 0-5 days range:",     N0_5, "Probability:",     N0_5/N )
print("Number of counts for 5-10 days range:",    N5_10, "Probability:",    N5_10/N )
print("Number of counts for 10-15 days range:",   N10_15, "Probability:",   N10_15/N )
print("Number of counts for 15-30 days range:",   N15_30, "Probability:",   N15_30/N )
print("Number of counts for 30-60 days range:",   N30_60, "Probability:",   N30_60/N )
print("Number of counts for 60-90 days range:",   N60_90, "Probability:",   N60_90/N )
print("Number of counts for 90-120 days range:",  N90_120, "Probability:",  N90_120/N )
print("Number of counts for 120-150 days range:", N120_150, "Probability:", N120_150/N )
print("Number of counts for 150-180 days range:", N150_180, "Probability:", N150_180/N )
print("Number of counts for 180- days range:",    N180_, "Probability:",    N180_/N )

# Sum
nsum = N0_5/N+N5_10/N+N10_15/N+N15_30/N+N30_60/N+N60_90/N+N90_120/N+N120_150/N+N150_180/N+N180_/N
print("Sum:",nsum)

# Plot 
names = [5, 10, 15, 30, 60, 90, 120, 150, 180, 217]
values = [100*N0_5/N, 100*N5_10/N, 100*N10_15/N, 100*N15_30/N, 100*N30_60/N, 100*N60_90/N, 100*N90_120/N, 100*N120_150/N, 100*N150_180/N, 100*N180_/N]

plt.plot(names, values, 'ro', linestyle='-')
#plt.bar(names, values,width=20 )
plt.title("Usuário Premium", fontsize=20)
plt.ylabel("Probabilidade (%)", fontsize=15)
plt.xlabel("Intervalo (Dias)", fontsize=15)
plt.xticks(names)
#plt.grid()
plt.show()
