'''
This program is going to load data from web (Apple, Google and Microsoft) and apply comparisons to the 
market (SPY data), calculate metrics, moving averages, create regime and signal based on the moving 
average crossover, create a portifolio and backtest from historical data.
'''
import pandas_datareader.data as web 
import pandas as pd
import quandl
import datetime
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
from matplotlib.dates import date2num
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
from mpl_finance import candlestick_ohlc
import numpy as np

# Authentication for quandl (account needed)
quandl.ApiConfig.api_key = ""

# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2016,1,1)
end = datetime.date.today()

#Apple data
#--------------------------
# Let's get Apple stock data; Apple's ticker symbol is AAPL
s = "AAPL"

# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date
apple = quandl.get("WIKI/" + s, start_date=start, end_date=end)

# Print info
print("Info from Apple:")
print(type(apple))
print(apple.head())

# Plot the adjusted closing price of AAPL
fig1, ax1 = plt.subplots()
apple["Adj. Close"].plot(grid = True, ax = ax1) 
ax1.set_xlabel('Date')
ax1.set_ylabel('Price ($)')
ax1.set_title("Adj. Close")
#--------------------------

# Defining function to compare open, close, high, low prices
#--------------------------
def pandas_candlestick_ohlc(dat, stick = "day", adj = False, otherseries = None):
    """
    :param dat: pandas DataFrame object with datetime64 index, and float columns "Open", "High", "Low", and "Close", likely created via DataReader from "yahoo"
    :param stick: A string or number indicating the period of time covered by a single candlestick. Valid string inputs include "day", "week", "month", and "year", ("day" default), and any numeric input indicates the number of trading days included in a period
    :param adj: A boolean indicating whether to use adjusted prices
    :param otherseries: An iterable that will be coerced into a list, containing the columns of dat that hold other series to be plotted as lines
 
    This will show a Japanese candlestick plot for stock data stored in dat, also plotting other series if passed.
    """
    mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
    alldays = DayLocator()              # minor ticks on the days
    dayFormatter = DateFormatter('%d')      # e.g., 12
 
    # Create a new DataFrame which includes OHLC data for each period specified by stick input
    fields = ["Open", "High", "Low", "Close"]
    if adj:
        fields = ["Adj. " + s for s in fields]
    transdat = dat.loc[:,fields]
    transdat.columns = pd.Index(["Open", "High", "Low", "Close"])
    if (type(stick) == str):
        if stick == "day":
            plotdat = transdat
            stick = 1 # Used for plotting
        elif stick in ["week", "month", "year"]:
            if stick == "week":
                transdat["week"] = pd.to_datetime(transdat.index).map(lambda x: x.isocalendar()[1]) # Identify weeks
            elif stick == "month":
                transdat["month"] = pd.to_datetime(transdat.index).map(lambda x: x.month) # Identify months
            transdat["year"] = pd.to_datetime(transdat.index).map(lambda x: x.isocalendar()[0]) # Identify years
            grouped = transdat.groupby(list(set(["year",stick]))) # Group by year and other appropriate variable
            plotdat = pd.DataFrame({"Open": [], "High": [], "Low": [], "Close": []}) # Create empty data frame containing what will be plotted
            for name, group in grouped:
                plotdat = plotdat.append(pd.DataFrame({"Open": group.iloc[0,0],
                                            "High": max(group.High),
                                            "Low": min(group.Low),
                                            "Close": group.iloc[-1,3]},
                                           index = [group.index[0]]))
            if stick == "week": stick = 5
            elif stick == "month": stick = 30
            elif stick == "year": stick = 365
 
    elif (type(stick) == int and stick >= 1):
        transdat["stick"] = [np.floor(i / stick) for i in range(len(transdat.index))]
        grouped = transdat.groupby("stick")
        plotdat = pd.DataFrame({"Open": [], "High": [], "Low": [], "Close": []}) # Create empty data frame containing what will be plotted
        for name, group in grouped:
            plotdat = plotdat.append(pd.DataFrame({"Open": group.iloc[0,0],
                                        "High": max(group.High),
                                        "Low": min(group.Low),
                                        "Close": group.iloc[-1,3]},
                                       index = [group.index[0]]))
 
    else:
        raise ValueError('Valid inputs to argument "stick" include the strings "day", "week", "month", "year", or a positive integer')
 
 
    # Set plot parameters, including the axis object ax used for plotting
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    if plotdat.index[-1] - plotdat.index[0] < pd.Timedelta('730 days'):
        weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
        ax.xaxis.set_major_locator(mondays)
        ax.xaxis.set_minor_locator(alldays)
    else:
        weekFormatter = DateFormatter('%b %d, %Y')
    ax.xaxis.set_major_formatter(weekFormatter)
 
    ax.grid(True)
    ax.set_ylabel('Price ($)')
    ax.set_title("Open, Close, High and Low Comparison")
    

    # Create the candelstick chart
    candlestick_ohlc(ax, list(zip(list(date2num(plotdat.index.tolist())), plotdat["Open"].tolist(), plotdat["High"].tolist(),
                      plotdat["Low"].tolist(), plotdat["Close"].tolist())),
                      colorup = "black", colordown = "red", width = stick * .4)
 
    # Plot other series (such as moving averages) as lines
    if otherseries != None:
        if type(otherseries) != list:
            otherseries = [otherseries]
        dat.loc[:,otherseries].plot(ax = ax, lw = 1.3, grid = True)
 
    ax.xaxis_date()
    ax.autoscale_view()
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
 
    #plt.show()
#--------------------------

# Call function to compare open, close, high and low
pandas_candlestick_ohlc(apple, adj=True, stick="month")

# Compare Adj. Close for Apple, Google and Microsoft
#--------------------------
# Get Microsoft and Google data
microsoft, google = (quandl.get("WIKI/" + s, start_date=start, end_date=end) for s in ["MSFT", "GOOG"])
 
# DataFrame consisting of the adjusted closing price of these stocks, first by making a list of these objects and using the join method
stocks = pd.DataFrame({"AAPL": apple["Adj. Close"],
                      "MSFT": microsoft["Adj. Close"],
                      "GOOG": google["Adj. Close"]})

# Print some info and plot
print("Info (Adj. Close) from Apple, Microsoft and Google:")
print(stocks.head())

# Plot Comparison
fig2, ax2 = plt.subplots()
stocks.plot(grid = True, ax = ax2)
ax2.set_xlabel('Date')
ax2.set_ylabel('Price ($)')
ax2.set_title("Adj. Close")

# Plot Comparison
fig3, ax3 = plt.subplots()
stocks.plot(secondary_y = ["AAPL", "MSFT"], grid = True, ax = ax3)
ax3.set_xlabel('Date')
ax3.set_ylabel('Price ($)')
ax3.set_title("Adj. Close")
#--------------------------

# Stock returns
#--------------------------
# df.apply(arg) will apply the function arg to each column in df, and return a DataFrame with the result
# Recall that lambda x is an anonymous function accepting parameter x; in this case, x will be a pandas Series object
# Stock’s return since the beginning of the period of interest
stock_return = stocks.apply(lambda x: x / x[0])
# Print some info 
print("Info (Return Since Beginning) from Apple, Microsoft and Google:")
print(stock_return.head() - 1)

# Plot result
fig4, ax4 = plt.subplots()
stock_return.plot(grid = True, ax = ax4).axhline(y = 1, color = "black", lw = 2)
ax4.set_xlabel('Date')
ax4.set_ylabel('Return ')
ax4.set_title("Return Since Beginning")
#--------------------------

# Log difference
#--------------------------
stock_change = stocks.apply(lambda x: np.log(x) - np.log(x.shift(1))) # shift moves dates back by 1.
print("Info (Log Difference) from Apple, Microsoft and Google:")
print(stock_change.head())

fig5, ax5 = plt.subplots()
stock_change.plot(grid = True, ax = ax5).axhline(y = 0, color = "black", lw = 2)
ax5.set_xlabel('Date')
ax5.set_ylabel('Difference ')
ax5.set_title("Log Difference")
#--------------------------

# Comparing stocks with the overall market (SPY - the market)
#--------------------------
# Get data from market (SPY)
spyder = web.DataReader("SPY", "yahoo", start, end)

# Join to stocks and print info
stocks = stocks.join(spyder.loc[:, "Adj Close"]).rename(columns={"Adj Close": "SPY"})
print("Info (Adj. Close) from Apple, Microsoft, Google and Market(SPY):")
print(stocks.head())

# Calculate return from beginning
stock_return = stocks.apply(lambda x: x / x[0])

# Calculate log difference
stock_change = stocks.apply(lambda x: np.log(x) - np.log(x.shift(1)))

# Plot return from beginning comparison
fig6, ax6 = plt.subplots()
stock_return.plot(grid = True, ax = ax6).axhline(y = 1, color = "black", lw = 2)
ax6.set_xlabel('Date')
ax6.set_ylabel('Return ')
ax6.set_title("Return Since Beginning")

# Plot log difference
fig7, ax7 = plt.subplots()
stock_change.plot(grid = True, ax = ax7).axhline(y = 0, color = "black", lw = 2)
ax7.set_xlabel('Date')
ax7.set_ylabel('Difference ')
ax7.set_title("Log Difference")
#--------------------------

# Classical risk metrics
#--------------------------
# Annual percentage rate (APR)
stock_change_apr = stock_change * 252 * 100    # There are 252 trading days in a year; the 100 converts to percentages
print("Annual Percentage Rate (APR):")
print(stock_change_apr.tail())

# Treasury bills (risk free rate)
tbill = quandl.get("FRED/TB3MS", start_date=start, end_date=end)
print("Treasury Bills (risk free rate):")
print(tbill.tail())

fig8, ax8 = plt.subplots()
tbill.plot(ax = ax8)
ax8.set_xlabel('Date')
ax8.set_ylabel('Rate')
ax8.set_title("U.S. Treasury Bill Rate")

# Get the most recent Treasury Bill rate
rrf = tbill.iloc[-1, 0]    
print("Most Recent Treasury Bills Rate:")
print(rrf)

# How much each stock is correlated to SPY
smcorr = stock_change_apr.drop("SPY", 1).corrwith(stock_change_apr.SPY)    
print("Correlation Between Stocks and Market:")
print(smcorr)                                                                           

# Standard deviation for stocks (volatility) 
sy = stock_change_apr.drop("SPY", 1).std()

# Standard deviation for market (volatility)
sx = stock_change_apr.SPY.std()

# Print volatility
print("Volatility From Stocks:")
print(sy)
print("Volatility From Market:")
print(sx)

# Sample means - most recent bill rate
ybar = stock_change_apr.drop("SPY", 1).mean() - rrf
xbar = stock_change_apr.SPY.mean() - rrf
print("Mean - Most Recent Bill Rate (Stocks):")
print(ybar)
print("Mean - Most Recent Bill Rate (Market):")
print(xbar)

# Beta and alpha (Beta is how much a stock moves in relation to the market; alpha is average excess return over the market)
beta = smcorr * sy / sx
alpha = ybar - beta * xbar
print("Stock Moves In Relation To The Market:")
print(beta)
print("Average Excess Return Over The Market:")
print(alpha)

#Sharpe ratio for stocks (A large Sharpe ratio indicates that the stock's excess returns are large relative to the stock's volatilitly)
sharpe = (ybar - rrf)/sy
print("Sharpe Ratio (Stocks):")
print(sharpe)

#Sharpe ratio for market
print("Sharpe Ratio (Market):")
print((xbar - rrf)/sx)
#--------------------------

# Moving Average
#--------------------------
# Moving averge 20 days
apple["20d"] = np.round(apple["Adj. Close"].rolling(window = 20, center = False).mean(), 2)

# Call Function to compare variables
pandas_candlestick_ohlc(apple.loc['2016-01-04':'2016-12-31',:], otherseries = "20d", adj=True)

# Change date to get from 2010 in order to avoid empty average
start = datetime.datetime(2010,1,1)

# Get Apple date from 2010
apple = quandl.get("WIKI/AAPL", start_date=start, end_date=end)

# Moving averge 20, 50 and 200 days
apple["20d"] = np.round(apple["Adj. Close"].rolling(window = 20, center = False).mean(), 2)
apple["50d"] = np.round(apple["Adj. Close"].rolling(window = 50, center = False).mean(), 2)
apple["200d"] = np.round(apple["Adj. Close"].rolling(window = 200, center = False).mean(), 2)

# Call Function to compare variables
pandas_candlestick_ohlc(apple.loc['2016-01-04':'2016-12-31',:], otherseries = ["20d", "50d", "200d"], adj=True)
#--------------------------

# Trading strategy (moving average crossover)
#--------------------------
apple['20d-50d'] = apple['20d'] - apple['50d']
print("Apple (Moving Average):")
print(apple.tail())

# Regime
# Where a condition is checked for each component of a vector, and the first argument passed is used when the condition holds, and the other otherwise
apple["Regime"] = np.where(apple['20d-50d'] > 0, 1, 0)
# We have 1's for bullish regimes and 0's for everything else. 
# Replace bearish regimes's values with -1, and to maintain the rest of the vector, the second argument is apple["Regime"]
apple["Regime"] = np.where(apple['20d-50d'] < 0, -1, apple["Regime"])

# Plot result
fig9, ax9 = plt.subplots()
#apple.loc['2016-01-04':'2016-12-31',"Regime"].plot(ylim = (-2,2), ax = ax9).axhline(y = 0, color = "black", lw = 2)
apple["Regime"].plot(ylim = (-2,2), ax = ax9).axhline(y = 0, color = "black", lw = 2)
ax9.set_xlabel('Date')
ax9.set_ylabel('Regime Value')
ax9.set_title("Regime")

# Print regime counts
print("Regime Counts:")
print(apple["Regime"].value_counts())

# To ensure that all trades close out, I temporarily change the regime of the last row to 0
regime_orig = apple.loc[:, "Regime"].iloc[-1]
apple.loc[:, "Regime"].iloc[-1] = 0

# Define signal (The sign function returns -1 if x < 0, 0 if x==0, 1 if x > 0)
apple["Signal"] = np.sign(apple["Regime"] - apple["Regime"].shift(1))

# Restore original regime data
apple.loc[:, "Regime"].iloc[-1] = regime_orig
print("Apple Regime and Signal:")
print(apple.tail(10))

# Plot result
fig10, ax10 = plt.subplots()
#apple.loc['2016-01-04':'2016-12-31',"Signal"].plot(ylim = (-2,2), ax = ax10).axhline(y = 0, color = "black", lw = 2)
apple["Signal"].plot(ylim = (-2,2), ax = ax10).axhline(y = 0, color = "black", lw = 2)
ax10.set_xlabel('Date')
ax10.set_ylabel('Signal Value')
ax10.set_title("Signal")

# Print signal counts
print("Apple Signal Counts:")
print(apple["Signal"].value_counts())

# Print prices of the stock at every buy 
print("Apple Price For Every Buy:")
print(apple.loc[apple["Signal"] == 1, "Close"])

# Print prices of the stock at every sell 
print("Apple Price For Every Sell:")
print(apple.loc[apple["Signal"] == -1, "Close"])

# Create a DataFrame with trades, including the price at the trade and the regime under which the trade is made.
apple_signals = pd.concat([
        pd.DataFrame({"Price": apple.loc[apple["Signal"] == 1, "Adj. Close"],
                     "Regime": apple.loc[apple["Signal"] == 1, "Regime"],
                     "Signal": "Buy"}),
        pd.DataFrame({"Price": apple.loc[apple["Signal"] == -1, "Adj. Close"],
                     "Regime": apple.loc[apple["Signal"] == -1, "Regime"],
                     "Signal": "Sell"}),
    ])
apple_signals.sort_index(inplace = True)

# Print data frame including the price at the trade and the regime under which the trade is made.
print("Apple Price, Regime and Signal:")
print(apple_signals)

# Let's see the profitability of long trades
apple_long_profits = pd.DataFrame({
        "Price": apple_signals.loc[(apple_signals["Signal"] == "Buy") &
                                  apple_signals["Regime"] == 1, "Price"],
        "Profit": pd.Series(apple_signals["Price"] - apple_signals["Price"].shift(1)).loc[
            apple_signals.loc[(apple_signals["Signal"].shift(1) == "Buy") & (apple_signals["Regime"].shift(1) == 1)].index
        ].tolist(),
        "End Date": apple_signals["Price"].loc[
            apple_signals.loc[(apple_signals["Signal"].shift(1) == "Buy") & (apple_signals["Regime"].shift(1) == 1)].index
        ].index
    })

# Print data frame the profitability of long trades
print("Apple Price, Profit and End Date:")
print(apple_long_profits)

# We need to get the low of the price during each trade.
tradeperiods = pd.DataFrame({"Start": apple_long_profits.index,
                            "End": apple_long_profits["End Date"]})
apple_long_profits["Low"] = tradeperiods.apply(lambda x: min(apple.loc[x["Start"]:x["End"], "Adj. Low"]), axis = 1)

# Print result
print("Apple Price, Profit, End Date and Low Price:")
print(apple_long_profits)
#--------------------------

# Backtest
#--------------------------
# Now we have all the information needed to simulate this strategy in apple_adj_long_profits
cash = 1000000
apple_backtest = pd.DataFrame({"Start Port. Value": [],
                         "End Port. Value": [],
                         "End Date": [],
                         "Shares": [],
                         "Share Price": [],
                         "Trade Value": [],
                         "Profit per Share": [],
                         "Total Profit": [],
                         "Stop-Loss Triggered": []})
port_value = .1  # Max proportion of portfolio bet on any trade
batch = 100      # Number of shares bought per batch
stoploss = .2    # % of trade loss that would trigger a stoploss
for index, row in apple_long_profits.iterrows():
    batches = np.floor(cash * port_value) // np.ceil(batch * row["Price"]) # Maximum number of batches of stocks invested in
    trade_val = batches * batch * row["Price"] # How much money is put on the line with each trade
    if row["Low"] < (1 - stoploss) * row["Price"]:   # Account for the stop-loss
        share_profit = np.round((1 - stoploss) * row["Price"], 2)
        stop_trig = True
    else:
        share_profit = row["Profit"]
        stop_trig = False
    profit = share_profit * batches * batch # Compute profits
    # Add a row to the backtest data frame containing the results of the trade
    apple_backtest = apple_backtest.append(pd.DataFrame({
                "Start Port. Value": cash,
                "End Port. Value": cash + profit,
                "End Date": row["End Date"],
                "Shares": batch * batches,
                "Share Price": row["Price"],
                "Trade Value": trade_val,
                "Profit per Share": share_profit,
                "Total Profit": profit,
                "Stop-Loss Triggered": stop_trig
            }, index = [index]))
    cash = max(0, cash + profit)

# Print data frame simulate this strategy in apple_adj_long_profits
print("Apple BackTest:")
print(apple_backtest)

# Plot results
fig11, ax11 = plt.subplots()
apple_backtest["End Port. Value"].plot(ax = ax11)
ax11.set_xlabel('Date')
ax11.set_ylabel('Cash ($)')
ax11.set_title("Portifolio Increase")
#--------------------------

# Plot results
plt.show()
