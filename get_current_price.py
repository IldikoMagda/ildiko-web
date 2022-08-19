### This will be a function that uses stocks on account and scrapes their most recent price ###
import yfinance as yf
from db import stocks_list, update_current_price

def current_prices_and_industries():
    list_of_tickers = stocks_list()
    new_price_list = []
    industries_list = []
    for each in list_of_tickers:
        stock = yf.Ticker(str(each))
        price = stock.info['currentPrice']
        industry = stock.info['industry']
        industries_list.append(industry)
        new_price_list.append(price)
    #update database currentprice column 
    for index, eachstock in enumerate(list_of_tickers):
        update_current_price(eachstock,new_price_list[index])
    return industries_list
