import os 
import math
import datetime as dt
from datetime import timedelta
import time
from flask import Flask
from flask import render_template
from flask import request

import forms
lista=[]
#-----Calculator-------#
Rf=float(109.771)
fac_cor_fluor= float(0.0063)

app = Flask(__name__)
#FUNCION ultima dosis de la lista

def dose_last(lista):
    lista=lista[-1]
    dose_last=lista[0]
    return dose_last

#FUNCION ultimo tiempo de la lista

def time_last(lista):
    lista=lista[-1]
    time_last=lista[1]
    return time_last

#FUNCION ultimo tiempo de la lista

def ml_last(lista):
    lista=lista[-1]
    ml_last=lista[2]
    return ml_last

def cal_decay(dose_act,minut_decay,Rf):
    dose_act=float(dose_act)
    minutos=float(minut_decay)
    act_fin=dose_act*(math.exp(-(0.693*minutos/Rf)))
    return act_fin


def dif_min_proy(time_last,time_proy):
    start_dt = time_proy
    end_dt = time_last
    diff = (start_dt - end_dt)
    minutos= int(diff.seconds/60)
    return minutos


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
		now= dt.datetime.now()
		hour=hour.replace(year=now.year, month=now.month, day=now.day)
		tupla=(dose,hour,ml)
		lista.append(tupla)
		print(tupla)
		min= dif_min(hour)
		print (min)


	title = "PET Manager"
	return render_template('dosis_ini.html', title=title, form = comment_form)

@app.route('/real_time')
def real_time():
	act_ini=dose_last(lista)
	time=time_last(lista)
	minutos=dif_min(time)
	dose_now=cal_decay(act_ini,minutos,Rf)
	dose_now= float(dose_now)-float((float(dose_now) * fac_cor_fluor))
	dose_now=format(dose_now, '.2f')
	print (dose_now)
	dose = dose_now

	return render_template('real_time.html',dose=dose)




if __name__ == '__main__':
	app.run(debug=True, port= 8000)