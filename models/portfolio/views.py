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
        return send_from_directory(STATIC_FOLDER, 'dissertation.docx', as_attachment=True)

        # file= os.path.join(path, 'dissertation.docx')
        # return send_file(file, as_attachement= True, attachment_filename="IldikoMagdaDissertation")
        #return send_file('FutureDissertationnewresults.docx',mimetype='docx',as_attachment=True,attachment_filename='IldikoMagdaBioinf')
        #return send_from_directory('dissertation.docx', FOLDER, as_attachement=True)
        #return print(file)
    
    except Exception as e:
        return str(e) and str(STATIC_FOLDER)

@portfolio_blueprint.route('/Website', methods=['GET'])
def website(): 

    return render_template('portfolio/website.html')

@portfolio_blueprint.route('/ProstateCancerResearch', methods=['GET'])
def cancerresearch(): 

    return render_template('portfolio/cancerresearch.html')