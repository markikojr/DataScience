'''
This program is going to load the .csv data, check first rows, print some statistics, 
create a new column with moving average window, check and plot prices, comparing 'Adj Close'
to the 'moving average' and 'volume'.
'''
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

# Define style
style.use('ggplot')

# Get data
df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)

# Return first rows of data
print(df.head())

# Describe data
print(df.describe())

# Create new column moving average
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
#df.dropna(inplace=True)

# Check the data
print(df.head())

# Plot 
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=5, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()

