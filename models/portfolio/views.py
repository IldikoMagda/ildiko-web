from flask import Blueprint, render_template, send_file, send_from_directory

__author__ = 'Ildiko'

import os

portfolio_blueprint = Blueprint('portfolio', __name__)


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
        root_dir = os.path.dirname(os.getcwd())
        path = os.path.join(root_dir, 'static')
        print(path)
        print(root_dir)
        #return send_from_directory(path, filename='dissertation.docx')

        file= os.path.join(path, 'dissertation.docx')
        return send_file(file, attachment_filename="IldikoMagdaDissertation")
        #return send_file('FutureDissertationnewresults.docx',mimetype='docx',as_attachment=True,attachment_filename='IldikoMagdaBioinf')
        #return send_from_directory('dissertation.docx', FOLDER, as_attachement=True)
        #return print(file)
    
    except Exception as e:
        return str(e) and str(path)

@portfolio_blueprint.route('/Website', methods=['GET'])
def website(): 

    return render_template('portfolio/website.html')

@portfolio_blueprint.route('/ProstateCancerResearch', methods=['GET'])
def cancerresearch(): 

    return render_template('portfolio/cancerresearch.html')