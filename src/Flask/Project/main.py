import os 
import os.path
import csv
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
from models import db
from models import User , Lista
from flask_mail import Mail
from flask_mail import Message


lista=[] #Dosis Global
lista2=[] #Dosis Pacientes
lista3=[]
listadosis = []
listafinal =[]
listahoraproystr=[]
var=0
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

#FUNCION INGRESO DE DATO ACTUALIZADO
def input_data(lista,new_dose,new_hour,new_ml):
    act_dose=dose_last(lista)
    act_ml=ml_last(lista)
    act_hour=time_last(lista) #Datos actuales
    new_dose=new_dose
    new_hour=new_hour
    new_ml=new_ml
    minutos=dif_min_proy(act_hour,new_hour)
    doserefresh=cal_decay(act_dose,minutos,Rf)
    doserefresh=format(float(doserefresh)-float(new_dose),'.3f')
    doserefresh=float(doserefresh)-float((float(doserefresh) *fac_cor_fluor))
    mlrefresh= format((float(ml_last(lista)) - float(new_ml)),'.2f')
    tupla=(new_dose,new_hour,new_ml)
    lista2.append(tupla)
    tupla_act=(str(doserefresh), new_hour, str(mlrefresh))
    lista.append(tupla_act)
    hour = new_hour.strftime("%H:%M")
    tupla1=(new_dose,hour,new_ml)
    lista3.append(tupla1)
    print ("Datos ingresados con exito")

def input_data_mod(dose,hour,ml):
    act_dose=dose_last(lista)
    act_ml=ml_last(lista)
    act_hour=time_last(lista)
    new_dose=dose
    new_hour=hour
    new_ml=ml
    minutos=dif_min_proy(act_hour,new_hour)
    doserefresh=cal_decay(act_dose,minutos)
    doserefresh=format(float(doserefresh)-float(new_dose),'.3f')
    mlrefresh= format((float(ml_last(lista)) - float(new_ml)),'.2f')
    tupla_act=(str(doserefresh), new_hour, str(mlrefresh))
    lista.append(tupla_act)
    print ("Datos ingresados con exito")

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf= CsrfProtect()
mail = Mail()


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


@app.route('/login' , methods = ['GET','POST'])
def login():
	global username1
	login_form = forms.LoginForm(request.form)
	if request.method == 'POST' and login_form.validate():
		username= login_form.username.data
		password= login_form.password.data

		user= User.query.filter_by(username = username).first()
		userid= user.id
		if user is not None and user.verify_password(password):
			if username == 'sinostroza':
				username1= 'TM Sebastian Inostroza'
			elif username == 'gvera':
				username1= 'TM Gonzalo Vera'
			elif username == 'ddaza':
				username1= 'TM Daniela Daza'
			elif username == 'jpereza':
				username1= 'TM Jose Perez'	

			success_message = 'Bienvenido {}'.format(username1)
			flash(success_message, 'success')
			session['username'] = username
			return redirect( url_for('index2'))

		else:
			error_message = 'Usuario o Contraseña no Validos.'
			flash(error_message, 'danger')

			return redirect( url_for('login'))


		session['username'] = login_form.username.data
		session['id'] = userid


	return render_template('login.html', form = login_form)

@app.route('/ajax_login',  methods = ['POST'])
def ajax_login():
	print (request.form)
	username= request.form['username']
	password = request.form['password']
	response= { 'username': username, 'password': password }
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
		success_message = 'Ya estas con una sesion activa'	
		flash(success_message, 'info')

		return render_template('index.html')
	else:

		return render_template('index.html')

@app.route('/index2', methods = ['GET','POST'])
def index2():
	if 'username' in session:
		username = session['username']

		return render_template('index2.html')
	else:
		
		return render_template('index.html')

@app.route('/reinicio')
def reinicio():
	global lista
	if lista == []:
		success_message= 'No se han ingresado Datos iniciales!.'
		flash(success_message, 'danger')
		return redirect( url_for('dosis_ini'))
		
	else:
		return render_template('reinicio.html')

@app.route('/reinicio2')
def reinicio2():
	global lista
	global lista2
	global lista3
	global listadosis
	global listafinal
	global listahoraproystr

	lista=[]
	lista2=[]
	lista3=[]
	listadosis = []
	listafinal =[]
	listahoraproystr=[]
	success_message= 'Valores reiniciados.'
	flash(success_message, 'success')

	return redirect( url_for('dosis_ini'))	
	

@app.route('/create', methods = ['GET','POST'])
def create():
	create_form = forms.CreateForm(request.form)
	if request.method == 'POST' and create_form.validate():
		user= User( create_form.username.data,
				    create_form.password.data )


		db.session.add(user)
		db.session.commit()

		success_message = 'Usuario Registrado correctamente en la Base de datos'	
		flash(success_message, 'success')

	return render_template('create.html', form = create_form)


@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username')
		success_message= 'Sesion cerrada con Exito!.'
		flash(success_message, 'success')
		return redirect (url_for('index'))
	else:
		success_message= 'Debes iniciar Sesion antes de cerrarla.'
		flash(success_message, 'warning')
		return redirect (url_for('index'))

@app.route('/dosis_ini' , methods = ['GET','POST'])
def dosis_ini():
	if 'username' in session:
		comment_form = forms.CommentForm(request.form)

		if lista == []:
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
				success_message= 'Datos Ingresados con Exito!'
				flash(success_message, 'success')
				return redirect (url_for('real_time'))


			title = "PET Manager"
			return render_template('dosis_ini.html', title=title, form = comment_form)
		else: 
			success_message= 'Ya existen datos Iniciales'
			flash(success_message, 'warning')
			return redirect (url_for('resumen'))

	else:
		success_message= 'Debes iniciar Sesion.'
		flash(success_message, 'warning')
		return redirect (url_for('login'))


@app.route('/dosis_new' , methods = ['GET','POST'])
def dosis_new():
	if 'username' in session:
		username = session['username']
		user= User.query.filter_by(username = username).first()
		userid= user.id
		if lista == []:
			success_message= 'No se han ingresado Datos iniciales!.'
			flash(success_message, 'danger')
			
			return redirect( url_for('dosis_ini'))
		else:
			comment_form = forms.CommentFormnew(request.form)

			if request.method == 'POST' and comment_form.validate():
				print (comment_form.dosis.data)
				print (comment_form.Hora.data)
				print (comment_form.ml.data)
				dose=comment_form.dosis.data
				hour=comment_form.Hora.data
				ml=comment_form.ml.data
				now= dt.datetime.now()
				hour=hour.replace(year=now.year, month=now.month, day=now.day)
				input_data(lista,dose,hour,ml)
				tupla=Lista(dosis=dose, ml=ml, hora=hour, user_id=userid)
				db.session.add(tupla)
				db.session.commit()

				success_message= 'Datos Ingresados con Exito!.'
				flash(success_message, 'success')
				return redirect( url_for('real_time'))


			title = "PET Manager"
			return render_template('dosis_new.html', title=title, form = comment_form)
	else:
		success_message= 'Debes iniciar Sesion.'
		flash(success_message, 'warning')
		return redirect (url_for('login'))		

@app.route('/real_time')
def real_time():
	if 'username' in session:
		comment_form = forms.CommentForm(request.form)
		if lista == []:
			success_message= 'No se han ingresado Datos iniciales!.'
			flash(success_message, 'danger')

			return redirect( url_for('dosis_ini'))
		else:
			act_ini=dose_last(lista)
			time=time_last(lista)
			minutos=dif_min(time)
			dose_now=cal_decay(act_ini,minutos,Rf)
			dose_now= float(dose_now)-float((float(dose_now) * fac_cor_fluor))
			dose_now=format(dose_now, '.2f')
			print (dose_now)
			dose = dose_now
			mlrest=ml_last(lista)
			pctes=len(lista2)



			return render_template('real_time.html',dose=dose, mlrest=mlrest,pctes=pctes)
	else:
		success_message= 'Debes iniciar Sesion.'
		flash(success_message, 'warning')
		return redirect (url_for('login'))



@app.route('/resumen')
def resumen():
	listafinal=[]
	d=1
	a=0
	for i in lista3:
		listadosis=[]
		listadosis.append(str(d))
		c=0
		while c < 3:
			listadosis.append(lista3[a][c])
			c = c+1

		listafinal.append(listadosis)
		a=a+1                      
		d=d+1

	print(listafinal)

	return render_template('resumen.html',listadosis=listafinal)

@app.route('/envio', methods = ['GET','POST'])
def envio():
	if 'username' in session:
		if lista == []:
			success_message= 'No se han ingresado Datos iniciales!.'
			flash(success_message, 'danger')
			
			return redirect( url_for('dosis_ini'))
		else:
			listafinal=[]
			d=1
			a=0
			for i in lista3:
				listadosis=[]
				listadosis.append(str(d))
				c=0
				while c < 3:
					listadosis.append(lista3[a][c])
					c = c+1
				listafinal.append(listadosis)
				a=a+1
				d=d+1

		
			now= dt.datetime.now()
			hour=now.replace(year=now.year, month=now.month, day=now.day)
			fecha= hour.strftime("%Y-%m-%d")
			archivo=os.path.abspath( os.path.join("data",fecha+'-DosisPET.csv'))
			csv=open(archivo,'w')
			titulo="Paciente,Dosis,Hora,mL\n"
			csv.write(titulo)
			print (listafinal)
			s=0
			for linea in listafinal:
				pcte,dosis,hora,ml=str(listafinal[s][0]),str(listafinal[s][1]),str(listafinal[s][2]),str(listafinal[s][3]),
				filas=pcte+","+dosis+","+hora+","+ml+"\n"
				csv.write(filas)
				s=s+1
			csv.close()

			comment_formmail = forms.CommentFormmail(request.form)
			if request.method == 'POST' and comment_formmail.validate():
				maildest=comment_formmail.mail.data
				msg= Message('Envio de Jornada PET', sender = app.config['MAIL_USERNAME'],
													recipients = [maildest] )
				msg.html = '<b> Se adjunta la lista de Jornada PET Clinica Reñaca</b><br></br>'
				with app.open_resource(os.path.join("data",fecha+'-DosisPET.csv')) as DosisPET:
					msg.attach(fecha+'-DosisPET.csv', fecha+'-DosisPET/csv', DosisPET.read())
				mail.send(msg)
				success_message= 'Mail enviado con exito.'
				flash(success_message, 'success')
				return redirect (url_for('resumen'))

			
		return render_template('envio.html', form= comment_formmail)

@app.route('/dose_proy' , methods = ['GET','POST'])
def dose_proy():
	if 'username' in session:
		if lista == []:
			success_message= 'No se han ingresado Datos iniciales!.'
			flash(success_message, 'danger')
			
			return redirect( url_for('dosis_ini'))
		else:
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
				hour = hour.strftime("%H:%M")

			return render_template('dose_proy.html', form= comment_form2, hour=hour, dose=dose)
	else:
		success_message= 'Debes iniciar Sesion.'
		flash(success_message, 'warning')
		return redirect (url_for('login'))

@app.route('/dose_ml' , methods = ['GET','POST'])
def dose_ml():
	if 'username' in session:
		if lista == []:
			success_message= 'No se han ingresado Datos iniciales!.'
			flash(success_message, 'danger')
			
			return redirect( url_for('dosis_ini'))
		else:
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
	else:
		success_message= 'Debes iniciar Sesion.'
		flash(success_message, 'warning')
		return redirect (url_for('login'))

@app.route('/dosis_mod' , methods = ['GET','POST'])
def dosis_mod():
	if 'username' in session:
		if lista2 == []:
			success_message= 'No se han ingresado Datos de Dosificacion!.'
			flash(success_message, 'danger')
			
			return redirect( url_for('dosis_new'))
		else:
			comment_form = forms.CommentFormod(request.form)

			if request.method == 'POST' and comment_form.validate():
				num=comment_form.num.data
				dose=comment_form.dosis.data
				hour=comment_form.Hora.data
				ml=comment_form.ml.data
				now= dt.datetime.now()
				hour=hour.replace(year=now.year, month=now.month, day=now.day)
				hour = hour.strftime("%H:%M")
				num= num-1
				if num > len(lista3):
					success_message= 'Dosificacion Paciente no valida.'
					flash(success_message, 'danger')
					return redirect( url_for('dosis_mod'))
				else:
					lista3[num]=(dose,hour,ml)


				success_message= 'Datos Modificados con Exito!.'
				flash(success_message, 'success')
				return redirect( url_for('resumen'))


			title = "PET Manager"
			return render_template('dosis_mod.html', title=title, form = comment_form)
	else:
		success_message= 'Debes iniciar Sesion.'
		flash(success_message, 'warning')
		return redirect (url_for('login'))	


@app.route('/ag_proy' , methods = ['GET','POST'])
def ag_proy():
	dosep=""
	hourp=""
	dosis=""
	tr=""
	hora=""
	inicio1 =""
	if 'username' in session:
		if lista == []:
			success_message= 'No se han ingresado Datos de Dosificacion!.'
			flash(success_message, 'danger')
			
			return redirect( url_for('dosis_ini'))
		else:
			listahoraproystr=[]
			listadosisproy=[]
			comment_form = forms.CommentForm_ag2(request.form)

			if request.method == 'POST' and comment_form.validate():
				r=2
				tr=comment_form.tr.data
				dosis=comment_form.dosis.data
				hora=comment_form.Hora.data
				now= dt.datetime.now()
				hour=hora.replace(year=now.year, month=now.month, day=now.day)
				act_ini=dose_last(lista)
				time=time_last(lista)
				minutos=dif_min_proy(time,hour)
				dosep=cal_decay(act_ini,minutos,Rf)
				dosep=format(dosep,'.3f')
				hourlista=hour.strftime("%H:%M")
				ho= hour + timedelta(minutes=tr)
				inicio1 = ho.strftime("%H:%M")
				listahoraproystr=[]
				listadosisproy=[]
				listadosisproy.append(dosep)
				grupo= (str(1),hourlista,inicio1)
				listahoraproystr.append(grupo)
				print(listahoraproystr)
				while float(dosep) > float(dosis):
					dosep= listadosisproy[-1]
					dosep = float(dosep)-float(dosis)
					dosep=format(dosep,'.3f')
					p1= hour + timedelta(minutes=tr)
					inicio = p1.strftime("%H:%M")
					p1= p1 + timedelta(minutes=40)
					p1 = p1 - timedelta(minutes=tr)
					hourlista = p1.strftime("%H:%M")
					tupla= (str(r),hourlista,inicio)
					listahoraproystr.append(tupla)
					dosep=cal_decay(dosep,40,Rf)
					dosep=format(dosep,'.3f')
					listadosisproy.append(dosep)
					print (listahoraproystr)
					r=r+1
					hour = p1
				dosep= str(dosep)
				print (dosep)
				return render_template('ag_proy_2.html', form= comment_form, listahoraproystr=listahoraproystr, dosisrestante=dosep, dosis=dosis)

			return render_template('ag_proy.html', form= comment_form, listahoraproystr=listahoraproystr, dosisrestante=dosep, dosis=dosis)

	else:
		success_message= 'Debes iniciar Sesion.'
		flash(success_message, 'warning')
		return redirect (url_for('login'))	

if __name__ == '__main__':
	csrf.init_app(app)
	db.init_app(app)
	mail.init_app(app)

	
	with app.app_context():
		db.create_all()

	app.run(port= 8000)