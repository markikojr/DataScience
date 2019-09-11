'''
This Program is going to load the .csv with 'Adj Close' for each company, create columns looking the next 7 days
of percentage change, create a classifier (whether to buy, sell or hold a stock) based on requirement, create a 
column with labels (buy:1, sell:-1 and hold:0), define features as the percentage change for each company, split
the data X(features) and y(labels) in train and test data, apply machine learning models to fit the train data
and predict on test data. Model uses the VotingClassifier which combines all the algorithms response.
'''
from collections import Counter
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn import svm, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier

# Function to get companies names and data looking 7 days 
def process_data_for_labels(ticker):
    # How many days to look 
    hm_days = 7
    # Load the data with all sp500 companies
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    # Get companies names
    tickers = df.columns.values.tolist()
    # Fill na as 0
    df.fillna(0, inplace=True)

    # Loop over the days
    for i in range(1, hm_days+1):
        # Create column with percentage change from day i to today's price
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    # Fill na as 0 
    df.fillna(0, inplace=True)

    # Return names and data
    return tickers, df

# Function to check if one should buy, sell or hold a stock
def buy_sell_hold(*args):
    # Loop over arguments
    cols = [c for c in args]
    # Set up requirement
    requirement = 0.02
    # Check whether label is 1:buy, -1:sell and 0:hold
    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1
    return 0    

# Function to extract features
def extract_featuresets(ticker):
    # Get companies names and data
    tickers, df = process_data_for_labels(ticker) # Call the function to load tickers 

    # Create target (labels)
    df['{}_target'.format(ticker)] = list(map( buy_sell_hold, # This is the function to classifiy
                                               df['{}_1d'.format(ticker)],          # Those                           
                                               df['{}_2d'.format(ticker)],          #                           
                                               df['{}_3d'.format(ticker)],          #                          
                                               df['{}_4d'.format(ticker)],          # Are                           
                                               df['{}_5d'.format(ticker)],          #                       
                                               df['{}_6d'.format(ticker)],          #                           
                                               df['{}_7d'.format(ticker)]           # Parameters                         
                                               ))
    # Access labels values
    vals = df['{}_target'.format(ticker)].values.tolist()
    # Convert to string
    str_vals = [str(i) for i in vals]
    # Print the spread count
    print('Data spread:', Counter(str_vals))

    # Fill na as 0
    df.fillna(0, inplace=True)
    # Convert inf to nan and dropna
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)

    # Get Percentage change for all companies 
    df_vals = df[[ticker for ticker in tickers]].pct_change()
    # Convert inf to nan and dropna
    df_vals = df.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)

    # Features
    X = df_vals.values 

    # Labels
    y = df['{}_target'.format(ticker)].values

    # Return features, labels and data
    return X, y, df

# Function to do machine learning where X is the pct_change and y labels(buy, sell and hold)
def do_ml(ticker):
    # Get features, labels and data
    X, y, df = extract_featuresets(ticker) # Call the function to get features and labels

    # Split train and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

    # Build the model (votingclassifier will vote and choose classification)
    #clf = neighbors.KNeighborsClassifier()
    clf = VotingClassifier([('lsvc', svm.LinearSVC()),
                            ('knn', neighbors.KNeighborsClassifier()),
                            ('rfor', RandomForestClassifier())])

    # Fit the train data
    clf.fit(X_train, y_train)
    # Get accuracy from test data
    confidence = clf.score(X_test, y_test)
    # Predict test data
    predictions = clf.predict(X_test)
    # Print results
    print('Predicted Spread:', Counter(predictions))
    print('Accuracy:', confidence)
    print(df.head())

    # Return accuracy
    return confidence

# Call the function for machine learning
do_ml('BAC')
