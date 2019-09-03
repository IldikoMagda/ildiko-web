from flask import Blueprint, render_template

__author__ = 'Ildiko'


contact_blueprint = Blueprint('contact', __name__)


@contact_blueprint.route('/', methods=['GET'])
def index(): 

    return render_template('contact/index.html')