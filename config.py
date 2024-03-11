import os, urllib
from sqlalchemy import create_engine


class Config(object):
    SECRET_KEY = "Waza my nigga"
    SESSION_COOKIE_SECURE = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:admin@localhost:3306/bdidgs801"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
