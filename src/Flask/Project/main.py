import os 
import math
import datetime as dt
from datetime import timedelta
import time
from flask import Flask
from flask import render_template
from flask import request
from flask import flash, make_response, session
from flask import redirect, url_for
from flask_wtf import CsrfProtect
import forms
import json
from config import DevelopmentConfig


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
app.config.from_object(DevelopmentConfig)
csrf= CsrfProtect()

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


@app.route('/login' , methods = ['GET','POST'])
def login():
	Login_Form = forms.LoginForm(request.form)
	if request.method == 'POST' and Login_Form.validate():
		username= Login_Form.username.data
		success_message = 'Bienvenido {}'.format(username)
		flash(success_message)

		session['username'] = Login_Form.username.data


	return render_template('login.html', form = Login_Form)

@app.route('/ajax_login',  methods = ['POST'])
def ajax_login():
	print (request.form)
	username= request.form['username']
	response= { 'status': 200, 'username': username, 'id': 1 }
	return json.dumps(response)

@app.route('/ajax_dose_ini',  methods = ['POST'])
def ajax_dose_ini():
	print (request.form)
	username= request.form['username']
	response= { 'status': 200, 'username': username, 'id': 1 }
	return json.dumps(response)
	

@app.route('/cookie')
def cookie():
	response= make_response(render_template('cookie.html'))
	response.set_cookie('custome_cookie', 'seba')
	return response

@app.route('/')
def index():
	if 'username' in session:
		username = session['username']
		print (username)

	title= 'Index'
	return render_template('index.html', title=title)


@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username')
	return redirect (url_for('login'))

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
		success_message= 'Datos Ingresados con Exito!.'
		flash(success_message)


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
	csrf.init_app(app)
	app.run(port= 8000)