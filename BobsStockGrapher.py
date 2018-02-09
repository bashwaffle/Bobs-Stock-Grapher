#import necessary modules

import requests
import json
import pandas as pd
import numpy as np
import urllib, json
import matplotlib.pyplot as plt
import os


ticker = 'msft' 

#these are the API parameters from https://www.alphavantage.co/documentation/

alpha_url= 'https://www.alphavantage.co/query?'
time_series_function= 'function=TIME_SERIES_DAILY'
stock_symbol= '&symbol={}'.format(ticker)
outputsize= '&outputsize=full'
api_datatype= '&datatype=csv'
api_time_interval= '&interval=60min'
alpha_apikey= '&apikey={}'.format(API_key)

#Concatenate the API request
request1 = alpha_url + time_series_function + stock_symbol + api_datatype + outputsize + alpha_apikey
print(request1)

#Can pandas take the url and read straight to DF
url_to_df = pd.read_csv(request1)
print(url_to_df)

#Add a datetime column
url_to_df['datetime'] = pd.to_datetime(url_to_df['timestamp'])

#plot closing price by day
plt.plot(url_to_df['datetime'], url_to_df['close'])
plt.xlabel('Date')
plt.ylabel('Price')

plt.show()
