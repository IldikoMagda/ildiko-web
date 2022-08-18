from flask import Blueprint, render_template
from visualise_account_progress import account_growth, starting_balance, net_profit, number_of_stocks
from visualise_account_progress import piechartdata
from get_current_price import current_prices


__author__ = 'Ildiko'

trader_blueprint = Blueprint('trader', __name__, template_folder='templates')

table_header = ['Symbol ', 'Purchased at ', 'Current Price ']

@trader_blueprint.route('/', methods=['GET'])
def index(): 
    current_prices()
    return render_template('trader/index.html', account_growth = account_growth,
                           starting_balance=starting_balance, net_profit=net_profit,
                           number_of_stocks= number_of_stocks, piechartdata = piechartdata)