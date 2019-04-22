import os 
import math
import datetime as dt
import time
from wtforms import Form
from wtforms import StringField, TextField, FloatField, DateTimeField, PasswordField, HiddenField
from wtforms.fields.html5 import EmailField

from wtforms import validators

def length_honeypot(form, field):
	if len(field.data) >0:
		raise validators.ValidationError('El campo debe estar vacio.')


def check_decimal(form, field):
	a=field.data
	a=str(a)
	b= a.split(".")
	if len(b[-1])> 2:
		raise validators.ValidationError('No debe ingresar mas de dos decimales.')


class CommentForm(Form):
	dosis= FloatField('Dosis Inicial en mCi:',
		[ 
			validators.Required(message = 'Ingresar dosis Valida.'),
			check_decimal

		]
		) 
	Hora= DateTimeField('Hora de medicion Inicial',format ="%H:%M", validators=[validators.Required(message='Ingresar Formato HH:MM')])


	ml= FloatField('Milimetros(mL) Totales',
		[ 
			validators.Required(message = 'Ingresar mL Valido.'),
			check_decimal

		]
		) 

class CommentForm2(Form):
	Hora= DateTimeField('Hora de Proyección',format ="%H:%M", validators=[validators.Required(message='Ingresar Formato HH:MM')])


class CommentForm3(Form):
	dosis= FloatField('Dosis Requerida en mCi:',
		[ 
			validators.Required(message = 'Ingresar dosis Valida.'),
			check_decimal

		]
		) 

class LoginForm(Form):
	username= StringField('Username',
		[
			validators.Required(message= 'El Username es Requerido.'),
			validators.length(min=3, max =20, message='Ingrese un Username valido.'),

		])
	password = PasswordField('Password', [validators.Required(message='El password es Requerido'),
		])


