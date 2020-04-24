import os


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
prefix = 'sqlite:///'


class BaseConfig():
    SQLALCHEMY_DATABASE_URI = \
        prefix + os.path.join(basedir, 'dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'abrikos'