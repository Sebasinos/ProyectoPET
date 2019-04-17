import os 
import math
import datetime as dt
import time
from wtforms import Form
from wtforms import StringField, TextField, FloatField, DateTimeField
from wtforms.fields.html5 import EmailField

from wtforms import validators


def check_decimal(form, field):
	a=field.data
	a=str(a)
	b= a.split(".")
	if len(b[-1])> 2:
		raise validators.ValidationError('No debe ingresar mas de dos decimales.')


class CommentForm(Form):
	dosis= FloatField('Dosis en mCi:',
		[ 
			validators.Required(message = 'Ingresar dosis Valida.'),
			check_decimal

		]
		) 
	Hora= DateTimeField('Hora de medicion',format ="%H:%M", validators=[validators.Required(message='Ingresar Formato HH:MM')])


	ml= FloatField('Milimetros(mL)',
		[ 
			validators.Required(message = 'Ingresar mL Valido.'),
			check_decimal

		]
		) 

