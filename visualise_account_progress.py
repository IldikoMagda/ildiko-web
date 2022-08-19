### This script will genererate all neccesary data for account progress visualisation ###

from db import stocks_list, sum_share_value, sum_amount_spent

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

