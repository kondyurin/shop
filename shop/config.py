import os
import locale


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
prefix = 'sqlite:///'
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


class BaseConfig():
    SQLALCHEMY_DATABASE_URI = \
        prefix + os.path.join(basedir, 'dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'abrikos'