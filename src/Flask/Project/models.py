from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from sqlalchemy.orm import relationship



db = SQLAlchemy()

class User(db.Model):
	__tablename__ ='userspet'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(94))
	listas = db.relationship('Lista')


	def __init__(self, username, password):
		self.username = username
		self.password = self.__create_password(password)

	def __create_password(self, password):
		return generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password, password)


class Lista(db.Model):
	__tablename__ ='Lista'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	dosis = db.Column(db.Float(6,2))
	ml = db.Column(db.Float(6,2))
	hora = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('userspet.id'))


class Lista_ini(db.Model):
	__tablename__ ='Lista_ini'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	dosis = db.Column(db.Float(6,2))
	ml = db.Column(db.Float(6,2))
	hora = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('userspet.id'))

class Lista_flot(db.Model):
	__tablename__ ='Lista_flot'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	dosis = db.Column(db.Float(6,2))
	ml = db.Column(db.Float(6,2))
	hora = db.Column(db.DateTime)

class Lista_day(db.Model):
	__tablename__ ='Lista_day'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	dosis = db.Column(db.Float(6,2))
	ml = db.Column(db.Float(6,2))
	hora = db.Column(db.DateTime)

class Lista_str(db.Model):
	__tablename__ ='Lista_str'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	dosis = db.Column(db.String(11))
	ml = db.Column(db.String(11))
	hora = db.Column(db.String(11))