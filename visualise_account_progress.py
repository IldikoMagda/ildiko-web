### This script will genererate all neccesary data for account progress visualisation ###

from re import sub
from db import stocks_list, sum_share_value, sum_amount_spent
from db import boughat_list, return_current_prices_list
from get_current_price import current_prices

#starting balance 
#for now is static, can be made dynamic if more added
starting_balance = 150
stocks_held = stocks_list()
number_of_stocks = len(stocks_held)
share_value = sum_share_value()
amount_spent = sum_amount_spent()
current_balance = starting_balance-amount_spent
account_value = current_balance +share_value

account_growth = round(account_value/ starting_balance, 3)
net_profit = round(current_balance + share_value-starting_balance, 3)

#number of stocks in gain and loss: 
#find current price, find boughtat
def nr_gains_losses():
    nr_gaining_stock = 0 
    nr_loosing_stock = 0
    boughtat = boughat_list()
    #dynamically  fetch from yf takes longer to run:
    #currentprices = current_prices()
    
    #static:
    #currentprices = [43.99, 38.22, 36.54]
    
    #fetch from own db 
    current_prices = return_current_prices_list()
    subtracted = list()
    #subtract current price - boughtat
    for item1, item2, in zip(current_prices, boughtat):
        subtracted.append(item1 - item2 )
    print(subtracted)
    #count stocks in gain and in loss
    for i in subtracted:
        if i >= 0: 
            nr_gaining_stock += 1
        else: 
            nr_loosing_stock += 1
    return nr_gaining_stock, nr_loosing_stock

