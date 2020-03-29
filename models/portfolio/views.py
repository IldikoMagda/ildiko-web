from flask import Blueprint, render_template

__author__ = 'Ildiko'


portfolio_blueprint = Blueprint('portfolio', __name__)


@portfolio_blueprint.route('/', methods=['GET'])
def index(): 

    return render_template('portfolio/index.html')

@portfolio_blueprint.route('/MachineLearning', methods=['GET'])
def machinelearning(): 

    return render_template('portfolio/machinelearning.html')

@portfolio_blueprint.route('/WebApp', methods=['GET'])
def webapp(): 

    return render_template('portfolio/webapp.html')

@portfolio_blueprint.route('/Website', methods=['GET'])
def website(): 

    return render_template('portfolio/website.html')

@portfolio_blueprint.route('/ProstateCancerResearch', methods=['GET'])
def cancerresearch(): 

    return render_template('portfolio/cancerresearch.html')