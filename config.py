#config.py
import os

DEBUG = True    # Turns on debugging features in Flask
RELOADER = True
SECRET_KEY = os.environ.get('SECRET_KEY')
STATIC_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/static'

#deployed db 
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
   SQLALCHEMY_DATABASE_URI= SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
