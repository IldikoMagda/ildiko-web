from flask import Blueprint, render_template

__author__ = 'Ildiko'


about_blueprint = Blueprint('about', __name__)


@about_blueprint.route('/', methods=['GET'])
def index(): 

    return render_template('about/index.html')