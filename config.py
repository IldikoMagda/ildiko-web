#config.py

import os
DEBUG = True    # Turns on debugging features in Flask
RELOADER = True


SECRET_KEY = 'development key'
STATIC_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/static'