import os, urllib
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = "Waza my nigga"
    SESSION_COOKIE_SECURE = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://ivan:root@127.0.0.1/bdidgs801"
    SQLALCHEMY_TRACK_MODIFICATIONS = False