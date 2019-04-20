import os 
import math
import datetime as dt
from datetime import timedelta
import time
from flask import Flask
from flask import render_template
from flask import request
from flask import flash

import forms

lista=[]
#-----Calculator-------#
Rf=float(109.771)
fac_cor_fluor= float(0.0063)

def dose_now(lista):
    act_ini=dose_last(lista)
    time=time_last(lista)
    minutos=dif_min(time)
    dose_now=cal_decay(act_ini,minutos,Rf)
    dose_now= float(dose_now)-float((float(dose_now) * float(0.0063)))
    dose_now=format(dose_now, '.2f')
    print (dose_now)
    return dose_now


def dif_min(time_x):
    now= dt.datetime.now()
    diff = (now - time_x)
    minutos= int(diff.seconds/60)
    return minutos

def dif_min_proy(time_last,time_proy):
    start_dt = time_proy
    end_dt = time_last
    diff = (start_dt - end_dt)
    minutos= int(diff.seconds/60)
    return minutos

#--Calculator Dose--#

def cal_decay(dose_act,minut_decay,Rf):
    dose_act=float(dose_act)
    minutos=float(minut_decay)
    act_fin=dose_act*(math.exp(-(0.693*minutos/Rf)))
    return act_fin

def real_time(lista, Rf):
	act_ini=dose_last(lista)
	time=time_last(lista)
	minutos=dif_min(time)
	dose_now=cal_decay(act_ini,minutos,Rf)
	dose_now= float(dose_now)-float((float(dose_now) * fac_cor_fluor))
	dose_now=format(dose_now, '.2f')
	dose = dose_now


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

app = Flask(__name__)
app.config['SECRET_KEY']= 'PETMANUNAB'


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

@app.route('/dose_proy' , methods = ['GET','POST'])
def dose_proy():
	hour=""
	dose=""
	comment_form2 = forms.CommentForm2(request.form)
	if request.method == 'POST' and comment_form2.validate():
		hour=comment_form2.Hora.data
		now= dt.datetime.now()
		hour=hour.replace(year=now.year, month=now.month, day=now.day)
		print(hour)
		act_ini=dose_last(lista)
		time=time_last(lista)
		minutos=dif_min_proy(time,hour)
		dose=cal_decay(act_ini,minutos,Rf)
		dose=format(dose,'.3f')
		hour = hour.strftime("%H:%M:")

	return render_template('dose_proy.html', form= comment_form2, hour=hour, dose=dose)

@app.route('/dose_ml' , methods = ['GET','POST'])
def dose_ml():
	dose_req=""
	ml=""
	comment_form3 = forms.CommentForm3(request.form)
	if request.method == 'POST' and comment_form3.validate():
		dose_req=comment_form3.dosis.data
		dose_act=float(dose_now(lista))
		ml_act=float(ml_last(lista))
		ml= (dose_req*ml_act)/dose_act
		ml= format(ml,'.2f')

	return render_template('dose_ml.html', form= comment_form3, ml=ml, dose=dose_req)


if __name__ == '__main__':
	app.run(debug=True, port= 8000)