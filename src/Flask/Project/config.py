import os


class Config(object):
	SECRET_KEY = 'PETMANUNAB'
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT =465
	MAIL_USE_SSL = True
	MAIL_USE_TLS = False
	MAIL_USERNAME = 'petmanagerclr@gmail.com'
	MAIL_PASSWORD = 'petman201912'



class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql://root:cosas1212@localhost/flask'
	SQLALCHEMY_TRACK_MODIFICATIONS = False



		
		