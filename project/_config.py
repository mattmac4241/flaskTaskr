import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True
SECRET_KEY = '\x068\x98\x13\xc6|\xf2\xc2\xe7\x84X\xdf\xd7\xfd\xc9*G\xe7/{\x11\x96\xf7\xf2'
DATABASE_PATH = os.path.join(basedir,DATABASE)
SQLALCHEMY_DATABASE_URI = 'sqlite:////' + DATABASE_PATH
DEBUG = True
