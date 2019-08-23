import os 
import math
import datetime as dt
import time
from wtforms import Form
from wtforms import StringField, TextField, FloatField, DateTimeField, PasswordField, HiddenField, IntegerField
from wtforms.fields.html5 import EmailField
from models import User
from wtforms import validators
from flask_wtf import FlaskForm


def length_honeypot(form, field):
	if len(field.data) >0:
		raise validators.ValidationError('El campo debe estar vacio.')


def check_decimal(form, field):
	a=field.data
	a=str(a)
	b= a.split(".")
	if len(b[-1])> 2:
		raise validators.ValidationError('No debe ingresar mas de dos decimales.')

def num_positive(form, field):
	a=field.data
	if a <= 0:
		raise validators.ValidationError('No debe ingresar valores menores a Cero.')

def num_max(form, field):
	a=field.data
	if a > 1000000:
		raise validators.ValidationError('No debe ingresar valores mayores a 1000000.')

def ag_max(form, field):
	a=field.data
	if (a > 10) or (a < 2) :
		raise validators.ValidationError('Ingresar valor entre 2 y 10.')


class CommentForm(FlaskForm):
	dosis= FloatField('Dosis Inicial en mCi:',
		[ 
			validators.Required(message = 'Ingresar dosis Valida.'),
			check_decimal,
			num_positive,
			num_max

		]
		) 
	Hora= DateTimeField('Hora de medicion Inicial',format ="%H:%M", validators=[validators.Required(message='Ingresar Formato HH:MM')])


	ml= FloatField('Milimetros(mL) Totales',
		[ 
			validators.Required(message = 'Ingresar mL Valido.'),
			check_decimal,
			num_positive,
			num_max

		]
		) 
class CommentFormod(FlaskForm):
	num= IntegerField('Ingresar numero de dosificacion a modificar(Paciente)',
		[ 
			validators.Required(message = 'Ingresar numero valido.'),
			num_positive,

		])
	dosis= FloatField('Dosis a modificar en mCi:',
		[ 
			validators.Required(message = 'Ingresar dosis Valida.'),
			check_decimal,
			num_positive,
			num_max

		]
		) 
	Hora= DateTimeField('Hora a modificar',format ="%H:%M", validators=[validators.Required(message='Ingresar Formato HH:MM')])


	ml= FloatField('Milimetros(mL) Totales a modificar',
		[ 
			validators.Required(message = 'Ingresar mL Valido.'),
			check_decimal,
			num_positive,
			num_max

		]
		)

class CommentForm_ag2(FlaskForm):
	dosis= FloatField('Ingresar dosis utilizada para proyección',
		[ 
			validators.Required(message = 'Ingresar dosis Valida.'),
			check_decimal,
			num_positive,
			num_max

		]
		) 
	Hora= DateTimeField('Ingresar hora de primera administración de dosis',format ="%H:%M", validators=[validators.Required(message='Ingresar Formato HH:MM')])


	tr= IntegerField('Ingresar minutos de recirculación',
		[ 
			validators.Required(message = 'Ingresar numero valido.'),
			num_positive

		])

class CommentFormnew(FlaskForm):
	dosis= FloatField('Ingresar Dosis en mCi:',
		[ 
			validators.Required(message = 'Ingresar dosis Valida.'),
			check_decimal,
			num_positive,
			num_max

		]
		) 
	Hora= DateTimeField('Hora de medición',format ="%H:%M", validators=[validators.Required(message='Ingresar Formato HH:MM')])


	ml= FloatField('Milimetros(mL) Totales',
		[ 
			validators.Required(message = 'Ingresar mL Valido.'),
			check_decimal,
			num_positive,
			num_max

		]
		) 


class CommentForm2(FlaskForm):
	Hora= DateTimeField('Hora de Proyección',format ="%H:%M", validators=[validators.Required(message='Ingresar Formato HH:MM')])


class CommentFormmail(FlaskForm):
	mail= EmailField('Ingrese Mail de destino', validators=[validators.Required(message='Ingresar e-Mail Valido')])

class CommentForm3(FlaskForm):
	dosis= FloatField('Dosis Requerida en mCi:',
		[ 
			validators.Required(message = 'Ingresar dosis Valida.'),
			check_decimal,
			num_positive,
			num_max

		]
		) 

class LoginForm(FlaskForm):
	username= StringField('Username',
		[
			validators.Required(message= 'El Username es Requerido.'),
			validators.length(min=3, max =20, message='Ingrese un Username valido.'),

		])
	password = PasswordField('Password', [validators.Required(message='El password es Requerido'),
		])

class CreateForm(FlaskForm):
	username= StringField('Username',
		[
			validators.Required(message= 'El Username es Requerido.'),
			validators.length(min=3, max =20, message='Ingrese un Username valido.'),

		])
	password = PasswordField('Password', [validators.Required(message='El password es Requerido'),
		])

	def validate_username(form, field):
		username = field.data
		user = User.query.filter_by(username = username).first()
		if user is not None:
			raise validators.ValidationError('El nombre de Usuario ya se encuentra registrado!.')		





