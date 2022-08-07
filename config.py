#config.py
import os

DEBUG = True    # Turns on debugging features in Flask
RELOADER = True
SECRET_KEY = os.environ.get('SECRET_KEY')
STATIC_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/static'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

#SQLALCHEMY_DATABASE_URI ='postgresql://avilfoahpxfsqz:9318aba21014bffd3e1aa3a7d37898441c23062aa1e255d014162c8006e4937d@ec2-99-81-16-126.eu-west-1.compute.amazonaws.com:5432/d3hlo07lpplj11'