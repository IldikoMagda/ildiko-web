from flask import Blueprint, render_template
from visualise_account_progress import account_growth, starting_balance, net_profit, number_of_stocks
from visualise_account_progress import nr_gains_losses
from get_current_price import current_industries
from collections import Counter

__author__ = 'Ildiko'

trader_blueprint = Blueprint('trader', __name__, template_folder='templates')
@trader_blueprint.route('/', methods=['GET'])

def index():         
    #get current industries on portfolio 
    industries_list = current_industries()
    #dict of how many of each industry share we have, merge with header dict
    industries_starter = {'Industry':'Asset Percentage in Portfolio'}
    industries_coll= dict(Counter(industries_list))
    industries = {**industries_starter, **industries_coll}
    
    #number or gaining and loosing stock 
    gaining, loosing = nr_gains_losses()
    
    return render_template('trader/index.html', account_growth = account_growth,
                           starting_balance=starting_balance, net_profit=net_profit,
                           number_of_stocks= number_of_stocks,
                           industries =industries,
                           gaining = gaining, loosing = loosing)