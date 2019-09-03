#app.py 
from flask import Flask, render_template


from models.about.views import about_blueprint
from models.interactive.views import interactive_blueprint
from models.portfolio.views import portfolio_blueprint
from models.contact.views import contact_blueprint


app = Flask(__name__)
app.config.from_object('config')



@app.route("/")
def home():
    return render_template('index.html')


app.register_blueprint(about_blueprint, url_prefix="/about")
app.register_blueprint(interactive_blueprint, url_prefix="/interactive")
app.register_blueprint(portfolio_blueprint, url_prefix="/portfolio")
app.register_blueprint(contact_blueprint, url_prefix="/contact")