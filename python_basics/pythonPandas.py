#!/usr/bin/python 

#IMPORTING MODULES
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as pdr
import numpy as np

#OPENING THE DATA
df = pd.read_csv('/home/markjr/data_science/DataScience/DataScience-Python3/PastHires.csv', parse_dates=True, low_memory=True)

#CHANING STYLE TO BE COOL
style.use('ggplot')

#CHECKING THE DATA
print ("--------")
print ("CHECKING THE DATA")
print (df) #FULL DATA
#print(df.head()) #FIRST ELEMENTS
#print(df.tail()) #LAST ELEMENTS
#pd.set_option('max_rows', 10, 'max_columns', 4) #SET THE NUMBER OF ROWS AND COLUMNS TO DISPLAY

#DATA SHAPE, COLUMNS AND INDEX
print ("--------")
print ("DATA SHAPE, COLUMNS AND INDEX")
print (df.shape)
print (df.columns)
print (df.index)

#CHANGING THE CASE TO UPPER
print ("--------")
print ("DATA COLUMNS UPPER CASE")
df.columns = df.columns.str.upper()
print (df.columns)
print (df.head()) 

#RENAMING COLUMNS
print ("--------")
print ("DATA COLUMNS RENAMING")
df.rename(columns = {'EMPLOYED?':'EMPLOYED'}, inplace=True)
print (df.head())

#RENAMING ROWS INDEX
print ("--------")
print ("DATA ROWS INDEX RENAMING")
df.rename(index = {0:'ZERO'}, inplace=True)
print (df.head())

#CHECKING MISSING DATA AND CLEANING UP
print ("--------")
print ("CHECKING MISSING DATA")
print (df.isnull().values.any())
print (df.isnull().sum())
print (df.isnull().sum().sum())