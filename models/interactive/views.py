from flask import Blueprint, render_template

__author__ = 'Ildiko'


interactive_blueprint = Blueprint('interactive', __name__)


@interactive_blueprint.route('/', methods=['GET'])
def index(): 

    return render_template('interactive/index.html')