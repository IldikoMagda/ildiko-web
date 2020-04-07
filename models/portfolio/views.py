from flask import Blueprint, render_template, send_file, send_from_directory
import config
import os

__author__ = 'Ildiko'


portfolio_blueprint = Blueprint('portfolio', __name__)

#contains abs path to uploaded file
STATIC_FOLDER = config.STATIC_FOLDER

@portfolio_blueprint.route('/', methods=['GET'])
def index(): 

    return render_template('portfolio/index.html')

@portfolio_blueprint.route('/MachineLearning', methods=['GET','POST'])
def machinelearning(): 

    return render_template('portfolio/machinelearning.html')

@portfolio_blueprint.route('/WebApp', methods=['GET'])
def webapp(): 

    return render_template('portfolio/webapp.html')

@portfolio_blueprint.route('portfolio/download', methods=['GET'])
def download():
    try:
        return send_from_directory(STATIC_FOLDER, 'IldikoMagda_BioinformaticsDissertation.pdf', as_attachment=True)
    except Exception as e:
        return str(e) and str(STATIC_FOLDER)

@portfolio_blueprint.route('/Website', methods=['GET'])
def website(): 

    return render_template('portfolio/website.html')

@portfolio_blueprint.route('/ProstateCancerResearch', methods=['GET'])
def cancerresearch(): 

    return render_template('portfolio/cancerresearch.html')