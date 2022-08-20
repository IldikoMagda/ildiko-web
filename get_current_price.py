### This will be a function that uses stocks on account and scrapes their most recent price ###
import yfinance as yf
from db import stocks_list
from cachetools import TTLCache

TTLCache(maxsize=200, ttl=21600)
def current_prices():
    list_of_tickers = stocks_list()
    new_price_list = []
    for each in list_of_tickers:
        stock = yf.Ticker(str(each))
        price = stock.info['currentPrice']
        new_price_list.append(price)
    return new_price_list

TTLCache(maxsize=200, ttl=21600)
def current_industries():
    list_of_tickers=stocks_list()
    industries_list = []
    for each in list_of_tickers:
        stock = yf.Ticker(str(each))
        industry = stock.info['industry']
        industries_list.append(industry)
    return industries_list
    