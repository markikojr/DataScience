'''
This program is going to load the data from web choosing start and end dates, save the data to .csv, 
check first rows, print some statistics and plot prices.
'''
import pandas_datareader.data as web
import datetime as dt 
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

# Define style
style.use('ggplot')

# Define start and end date
start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)

# Get data
df = web.DataReader('TSLA', 'yahoo', start, end)

# Save data
df.to_csv('tsla.csv')

# Return first rows of data
print(df.head())

# Describe data
print(df.describe())


# Plot 
df.plot()
plt.show()
