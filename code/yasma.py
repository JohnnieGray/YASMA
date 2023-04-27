#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26, 2023

@author: Juan J Rodriguez
"""

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

MA = 1
LR = 2
     
def get_stock_data(ticker, start_date, end_date):
    """
    Download a stock's price data from Yahoo Finance between two specific dates.
    
    Args:
        ticker (str): Stock value Ticker to look for.
        start_date (str): Start date "YYYY-MM-DD" format.
        end_date (str): End date "YYYY-MM-DD" format.
    import matplotlib.pyplot as plt
    Returns:
        pandas.DataFrame: DataFrame with the share price data.
    """
    # Download a stock's price data from Yahoo Finance
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # DataFrame with the share price data.
    return data

def display_data(data, ticker, sd, ed, mode):
    # Close price
    plt.plot(data['Close'])    
    if (mode == MA):
        # Moving average (50 days)
        plt.plot(data['MA50'])    
        # Moving average (25 days)    
        plt.plot(data['MA25'])        
    elif (mode == LR)    :
        # Moving average (50 days)
        plt.plot(data['LR'])                    
    plt.title('{} close price between {} and {}'.format(ticker, sd, ed))
    plt.xlabel('Date')
    plt.ylabel('Close price')
    plt.show()
       
while True:
    print("Choose option:")
    print("1. Read data")
    print("2. Display data (text)")
    print("3. Display data MA (graphic)")
    print("4. Display data Linear Regression (graphic)")    
    print("5. Exit")

    option = input("Option: ")

    if option == "1":
        print("Reading data...")
        ticker = input("Ticker: ")
        s_date = input("Start date (YYYY-MM-DD): ")
        e_date = input("End date (YYYY-MM-DD): ")
        data = get_stock_data(ticker, s_date, e_date)        
        # MA 50 days
        data['MA50'] = data['Close'].rolling(window=50).mean()
        # MA 25 days
        data['MA25'] = data['Close'].rolling(window=25).mean()        
        # Calculate linear regression for the last 14 days
        n = len(data)
        X = pd.DataFrame({'X': range(n)})
        Y = data['Close'][-n:].values.reshape(-1, 1)
        reg = LinearRegression().fit(X, Y)
        data['LR'] = reg.predict(pd.DataFrame({'X': range(len(data)-n, len(data))}))
    elif option == "2":
        print("Displaying data (text)...")
        print(data)
    elif option == "3":
        print("Displaying data MA (graphic)...")
        display_data(data,ticker, s_date, e_date, MA)
    elif option == "4":
        print("Displaying data Linear Regression (graphic)...")
        display_data(data,ticker, s_date, e_date, LR)
    elif option == "5":
        print("Quit...")
        break
    else:
        print("Not valid option. Try it again.")
