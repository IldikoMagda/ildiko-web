###app.py ###
from flask import Flask, render_template
from sqlalchemy import create_engine
import psycopg2

from models.about.views import about_blueprint
#from models.interactive.views import interactive_blueprint
from models.portfolio.views import portfolio_blueprint
from models.trader.views import trader_blueprint

#import on flask mail doesn't work
#from models.contact.views import contact_blueprint
#from flask_mail import Message, Mail

#mail = Mail()
app = Flask(__name__)
app.config.from_object('config')
DB_URI = app.config['SQLALCHEMY_DATABASE_URI']
db = create_engine(DB_URI)
db.execute("CREATE TABLE IF NOT EXIST stocks (stock_name text, stock_price_purchase int, currentprice int)")

db.execute("INSERT INTO stocks(stock_name, stock_price_purchase, current_price) VALUES('TWTR', 38.23, 42.52)")


@app.route("/")
def home():
    return render_template('index.html')


app.register_blueprint(about_blueprint, url_prefix="/about")
#app.register_blueprint(interactive_blueprint, url_prefix="/interactive")
app.register_blueprint(portfolio_blueprint, url_prefix="/portfolio")
app.register_blueprint(trader_blueprint, url_prefix="/TheLazyTrader")
#app.register_blueprint(contact_blueprint, url_prefix="/contact")