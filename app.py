###app.py ###
from flask import Flask, render_template


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

app.secret_key = 'd3vkey3318'
 
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'ildikomagda.web@gmail.com'
app.config["MAIL_PASSWORD"] = 'devkey2341'
 
#mail.init_app(app)


@app.route("/")
def home():
    return render_template('index.html')


app.register_blueprint(about_blueprint, url_prefix="/about")
#app.register_blueprint(interactive_blueprint, url_prefix="/interactive")
app.register_blueprint(portfolio_blueprint, url_prefix="/portfolio")
app.register_blueprint(trader_blueprint, url_prefix="/TheLazyTrader")
#app.register_blueprint(contact_blueprint, url_prefix="/contact")