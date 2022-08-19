from flask import Blueprint, render_template
from visualise_account_progress import account_growth, starting_balance, net_profit, number_of_stocks
from get_current_price import current_prices_and_industries
from collections import Counter


__author__ = 'Ildiko'

trader_blueprint = Blueprint('trader', __name__, template_folder='templates')

table_header = ['Symbol ', 'Purchased at ', 'Current Price ']
#industries = {'Industry':'Asset Percentage in Portfolio','Telecom services':1, 'Internet Content and Information':1, 'Pharmaceutical Retailer':1}

@trader_blueprint.route('/', methods=['GET'])
def index(): 
    industries_list = current_prices_and_industries()
    #dict of how many of each industry share we have
    industries_starter = {'Industry':'Asset Percentage in Portfolio'}
    industries_coll= dict(Counter(industries_list))
    industries = {**industries_starter, **industries_coll}
    print(industries)
    # industries['Industry'] = 'Asset Percentage in Portfolio'
    # print(industries)
    return render_template('trader/index.html', account_growth = account_growth,
                           starting_balance=starting_balance, net_profit=net_profit,
                           number_of_stocks= number_of_stocks,
                           industries =industries)