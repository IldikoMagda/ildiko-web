### This script will genererate all neccesary data for account progress visualisation ### 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import get_current_price
from db import stocks_list, sum_share_value, sum_amount_spent
import plotly.express as px
import yfinance as yf
import datetime as DT

#update current prices on db 
#get_current_price 

#starting balance 
#for now is static, can be made dynamic if more added
starting_balance = 100
stocks_held = stocks_list()
number_of_stocks = len(stocks_held)
share_value = sum_share_value()
amount_spent = sum_amount_spent()
current_balance = starting_balance-amount_spent
account_value = current_balance +share_value

account_growth = round(account_value/ starting_balance, 3)
net_profit = round(current_balance + share_value-starting_balance, 3)


piechartdata = {'Industry':'Asset Percentage in Portfolio','Oil and Gas':1, 'Internet Content and Information':1}
#get data as frame 
#let's start with stock trend data

