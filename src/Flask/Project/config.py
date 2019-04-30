import os


class Config(object):
	SECRET_KEY = 'PETMANUNAB'

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql://root:cosas1212@localhost/flask'
	SQLALCHEMY_TRACK_MODIFICATIONS = False



		
		