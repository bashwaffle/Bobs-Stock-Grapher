# Import relevant modules

import requests
import json
import pandas as pd
import numpy as np
import urllib, json
import matplotlib.pyplot as plt
import os
import sys
import sqlite3 as db
    
# Request API key from user
API_key = input("Enter your API Key Here: ")

# Define a function to perform API request, and generate DF
# Will be used to iterate over different ticker symbols

def API_pull(ticker, interval='60min'):
    """ Will concatenate Alpha Vantage API request URL based on desired ticker and interval
    API_pull(ticker='msft', interval='60min')   """

    alpha_url= 'https://www.alphavantage.co/query?'
    time_series_function= 'function=TIME_SERIES_DAILY'
    stock_symbol= '&symbol={}'.format(ticker)
    outputsize= '&outputsize=full'
    api_datatype= '&datatype=csv'
    api_time_interval= '&interval={}'.format(interval)
    alpha_apikey= '&apikey={}'.format(API_key)

    #Concatenate the API request
    request1 = alpha_url + time_series_function + stock_symbol + api_datatype + outputsize + alpha_apikey
    print(request1)

    #Use pandas to take the url and read straight to DF
    url_to_df = pd.read_csv(request1)
    print(url_to_df)

    #Add a datetime column
    url_to_df['datetime'] = pd.to_datetime(url_to_df['timestamp'])
    print(url_to_df.head())

# Run API_pull function over a list of stocks

stocks = ['aapl', 'tsla', 'msft', 'nflx', 'luv', 'ibm', 'sq', 'stx', 'dal', 'aon']

# Database path
DB_path = str(r"C:\Users\bobti\Desktop\BobsStockGrapher\Bobs-Stock-Grapher\BobsStockDB.db")

# Establish a connection to database
conn = db.connect(DB_path)

# Use a for loop to run API pull on list of stocks, and add to DB
for stock in stocks:
    
    #Store API_pull data as a dataframe
    DF = API_pull(ticker=stock)
    
    #Add dataframe to SQL database
    DF.io.sql.to_sql(name=stock, con=conn, if_exists='fail')



