from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


db = SQLAlchemy()

class User(db.Model):
	__tablename__ ='userspet'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(94))

	def __init__(self, username, password):
		self.username = username
		self.password = self.__create_password(password)

	def __create_password(self, password):
		return generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password, password)

