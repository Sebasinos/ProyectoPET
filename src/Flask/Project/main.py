import os 
import math
import datetime as dt
import time
from flask import Flask
from flask import render_template
from flask import request

import forms
lista=[]
#-----Calculator-------#

app = Flask(__name__)

def dif_min(time_x):
    now= dt.datetime.now()
    diff = (now - time_x)
    minutos= int(diff.seconds/60)
    print (now)
    print (time_x)
    return minutos

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/dosis_ini' , methods = ['GET','POST'])
def dosis_ini():
	comment_form = forms.CommentForm(request.form)

	if request.method == 'POST' and comment_form.validate():
		print (comment_form.dosis.data)
		print (comment_form.Hora.data)
		print (comment_form.ml.data)
		dose=comment_form.dosis.data
		hour=comment_form.Hora.data
		ml=comment_form.ml.data
		tupla=(dose,hour,ml)
		lista.append(tupla)
		print(tupla)
		min= dif_min(hour)
		print (min)
		

	title = "PET Manager"
	return render_template('dosis_ini.html', title=title, form = comment_form)

if __name__ == '__main__':
	app.run(debug=True, port= 8000)