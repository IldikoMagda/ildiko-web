from flask import Blueprint, render_template

__author__ = 'Ildiko'

trader_blueprint = Blueprint('trader', __name__, template_folder='templates')

@trader_blueprint.route('/', methods=['GET'])
def index(): 
    return render_template('trader/index.html')