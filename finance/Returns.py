'''
This program is going to load the .csv, and get stock returns: daily, monthly, quarter,
daily log, cumulative daily and plot them.
'''
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

# Define style
style.use('ggplot')

# Get data
df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)

# Check data
print(df.head())

# Daily returns
daily_close = df[['Adj Close']]
daily_pct_change = daily_close.pct_change()
daily_pct_change.fillna(0, inplace=True)
print(daily_pct_change)

# Daily log returns
daily_log_returns = np.log(daily_close.pct_change()+1)
daily_log_returns.fillna(0, inplace=True)
print(daily_log_returns)

# Resample `df` to business months, take last observation as value 
monthly = df.resample('BM').apply(lambda x: x[-1])
monthly_pct_change = monthly.pct_change()
monthly_pct_change.fillna(0, inplace=True)
print(monthly_pct_change)
monthly_close = monthly_pct_change[['Adj Close']]

# Resample `df` to quarters, take the mean as value per quarter
quarter = df.resample("4M").mean()
quarter_pct_change = quarter.pct_change()
quarter_pct_change.fillna(0, inplace=True)
print(quarter_pct_change)
quarter_close = quarter_pct_change[['Adj Close']]

# Calculate the cumulative daily returns
cum_daily_return = (1 + daily_pct_change).cumprod()
print(cum_daily_return)

# Plot the daily returns
daily_pct_change.plot(figsize=(12,8))

# Plot the daily log returns
daily_log_returns.plot(figsize=(12,8))

# Plot the monthly returns
monthly_close.plot(figsize=(12,8))

# Plot the quarter returns
quarter_close.plot(figsize=(12,8))

# Plot the cumulative daily returns
cum_daily_return.plot(figsize=(12,8))

# Plot the distribution of `daily_pct_c`
daily_pct_change.hist(bins=50)

# Show the plot
plt.show()
