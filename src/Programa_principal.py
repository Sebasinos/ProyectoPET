#!/usr/bin/python
# -*- coding: utf-8 -*-
import os 
import math
import time
import datetime as dt

#VARIABLES GLOBALES

lista= []
lista2=[]
listadosis = []
listafinal =[]
var=0

#-------CHECK INPUTS---------#

#FUNCION CHECK INPUT / SOLICITA EL DATO Permite filtrar str involuntario y el ingreso de mas de 2 decimales.

def check_input_dose():
    while True:
        dosis_u = input("Ingrese Dosis con PUNTO(.) y solo 2 decimales\n")
        try:
            dosis_u =float(dosis_u)
            dosis_u="%.*f" % (2, dosis_u)
            return dosis_u
            
        except ValueError:
            print ("Debe ingresar valores separador por PUNTO(.) y solo 2 decimales")

def check_input_ml():
    while True:
        ml_u = input("Ingrese cantidad de ml con PUNTO(.) y solo 2 decimales\n")
        try:
            ml_u =float(ml_u)
            ml_u="%.*f" % (2, ml_u)
            return ml_u
            
        except ValueError:
            print ("Debe ingresar valores separador por PUNTO(.) y solo 2 decimales.")


def check_input_time():
    while True:
        time_u = input("Ingrese tiempo en minutos, ej 22 \n")
        try:
            time_u =int(time_u)
            return time_u
            
        except ValueError:
            print ("Debe ingresar valores ENTEROS")

def check_input_hora():
    while True:
        data = input("Ingrese hora en formato HH:MM \n")
        try:
            time.strptime(data, "%H:%M")
            hour=time.strptime(data, "%H:%M")
            hour_min=time.strftime('%H:%M', hour)
            return hour_min
        except ValueError:
            print ("Debe ingresar formato valido HH:MM ")


#-----CALCULATOR-------#
            
def dif_min(time_x):
    now= time.strftime('%H:%M')
    start_dt = dt.datetime.strptime(now, '%H:%M')
    end_dt = dt.datetime.strptime(time_x, '%H:%M')
    diff = (start_dt - end_dt)
    minutos= int(diff.seconds/60)
    return minutos

def cal_decay(dose_act,minut_decay):
    dose_act=float(dose_act)
    des_fluor =float(109.771)
    minutos=float(minut_decay)
    act_fin=dose_act*(math.exp(-(0.693*minutos/des_fluor)))
    return act_fin

def dif_min_proy(time_1,time_2):
    start_dt = dt.datetime.strptime(time_2, '%H:%M')
    end_dt = dt.datetime.strptime(time_1, '%H:%M')
    diff = (start_dt - end_dt)
    minutos= int(diff.seconds/60)
    return minutos
    
    
#------CONTROLLERS------#

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

#FUNCION DOSIS REAL-TIME
def dose_now(lista):
    act_ini=dose_last(lista)
    time=time_last(lista)
    minutos=dif_min(time)
    dose_now=cal_decay(act_ini,minutos)
    dose_now=round(dose_now,3)
    return dose_now
            
#FUNCION INGRESO DE DOSIS INICIAL
def dose_inicio():
    dose=check_input_dose()
    hour=check_input_hora()
    ml=check_input_ml()
    tupla=(dose,hour,ml)
    lista.append(tupla)
    print ("Datos ingresados con exito")


#FUNCION DE DOSIS PROYECTADA
def dose_proy(lista):
    hour_x=check_input_hora()
    act_ini=dose_last(lista)
    time=time_last(lista)
    minutos=dif_min_proy(time,hour_x)
    dose=cal_decay(act_ini,minutos)
    dose=round(dose,3)
    print ("la dosis proyectada para las",hour_x," es", dose, "mCi")
    return dose
    
#FUNCION CANTIDAD ML-DOSIS
def dose_ml(lista):
    dose_req=float(check_input_dose())
    dose_act=float(dose_now(lista))
    ml_act=float(ml_last(lista))
    ml= (dose_req*ml_act)/dose_act
    ml= round(ml,1)
    print ("Los ml necesarios para tener", dose_req, "mCi, son: ", ml, "ml")

#FUNCION INGRESO DE DATO ACTUALIZADO
def input_data(lista):
    act_dose=dose_last(lista)
    act_ml=ml_last(lista)
    act_hour=time_last(lista)
    new_dose=check_input_dose()
    new_hour=check_input_hora()
    new_ml=check_input_ml()
    minutos=dif_min_proy(act_hour,new_hour)
    doserefresh=cal_decay(act_dose,minutos)
    doserefresh=round(float(doserefresh)-float(new_dose),2)
    mlrefresh= float(ml_last(lista)) - float(new_ml)
    tupla=(new_dose,new_hour,new_ml)
    lista2.append(tupla)
    tupla_act=(str(doserefresh), new_hour, str(mlrefresh))
    lista.append(tupla_act)
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
    doserefresh=round(float(doserefresh)-float(new_dose),2)
    mlrefresh= float(ml_last(lista)) - float(new_ml)
    tupla_act=(str(doserefresh), new_hour, str(mlrefresh))
    lista.append(tupla_act)
    print ("Datos ingresados con exito")
    
    


#FUNCION GENERAR INFORME

def gen_info(lista2):
    d=1
    a=0
    for i in lista2:
        listadosis=[]
        listadosis.append(str(d))
        c=0
        while c < 3:
            listadosis.append(lista2[a][c])
            c = c+1
    
        listafinal.append(listadosis)
        a=a+1                      
        d=d+1


def crate_file(listafinal):
    archivo="lista Pacientes Diario.csv"
    csv=open(archivo,"w")
    titulo= "Paciente,Dosis,Hora,mL\n"
    csv.write(titulo)

    s=0
    for linea in listafinal:
        pcte,dosis,hora,ml=listafinal[s][0],listafinal[s][1],listafinal[s][2],listafinal[s][3],
        filas=pcte+","+dosis+","+hora+","+ml+"\n"
        csv.write(filas)
        s=s+1
    csv.close()
    print ("Reporte generado con Exito")

def mod_last_dat(lista2,lista):
    if (lista2 == []):
        print("No hay pacientes para modificar")

    else:
        opc=0
        while opc != "s":
            print("Ingese una opción valida")
            menuPrincipal = menu_mod()
            opc = opciones() 
            if(opc == "1"):
                dose=check_input_dose()
                lis=list(lista2[-1])
                lis[0]=dose
                hour=lis[1]
                ml=lis[2]
                listanew=tuple(lis)
                lista2.pop(-1)
                lista2.append(listanew)
                lista.pop(-1)
                input_data_mod(dose,hour,ml)
                print ("Regresando al Menú")
            if(opc == "2"):
                hour=check_input_hora()
                lis=list(lista2[-1])
                lis[1]=hour
                dose=lis[0]
                ml=lis[2]
                listanew=tuple(lis)
                lista2.pop(-1)
                lista2.append(listanew)
                lista.pop(-1)
                input_data_mod(dose,hour,ml)
                print ("Regresando al Menú")
            if(opc == "3"):
                ml=check_input_ml()
                lis=list(lista2[-1])
                lis[2]=ml
                dose=lis[0]
                hour=lis[1]
                listanew=tuple(lis)
                lista2.pop(-1)
                lista2.append(listanew)
                lista.pop(-1)
                input_data_mod(dose,hour,ml)
                print ("Regresando al Menú")
        


def menu_mod():
    clean(var)
    print("** Importante **")
    print("Los datos modificados solo son aplicables al ULTIMO paciente ingresado")
    print("Selecciona Opción:")
    print("** ::::::::::::::::::::::::: **")
    print("Modificar Dosis  :-> 1")
    print("Modificar Hora   :-> 2")
    print("Modificar mL     :-> 3")
    print("Volver al menú   :-> s")
    print("** ::::::::::::::::::::::::: **")

    
    


def clean(var):
    if os.name == "posix":
        var = "clear"

    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"

    os.system(var)
    
    

    


def menu():
    
	#MENU DE OPCIONES
	print("** ::::::::::::::::::::::::: **")
	print(":: Seleccione una Opción ::")
	print("** ::::::::::::::::::::::::: **")
	print("-------------------------------")
	print("| Ingresar Dosis Inicial   : ->  1     |")
	print("| Calcular Dosis Proyectada: ->  2     |")
	print("| Calcular Dosis Real-Time : ->  3     |")
	print("| Calcular mL para X dosis : ->  4     |")
	print("| Ingreso dato nuevo Pcte  : ->  5     |") 
	print("| Generar Reporte          : ->  6     |")
	print("| Modificar ultimo Pcte    : ->  7     |")
	print("| Salir                    : ->  s     |")
	print("-------------------------------")
	print("** ::::::::::::::::::::::::: **") 
	print("\n")
	#MENU DE OPCIONES
#OPCIÓN DEL MENU

def opciones(opc=0):
	opcion =input("Selecione una Opción... ")
	return opcion

opc=0
while opc != "s":
    print("Ingrese una opción valida")
    menuPrincipal = menu()
    opc = opciones()
    #OPCIÓN DEL MENU

    #MODULO DE INGRESO DOSIS INICIAL
    if(opc == "1"):
        dose_inicio()
        print ("Regresando al Menu")
        time.sleep(2)
        clean(var)
    
	
    #MODULO DE DOSIS PROYECTADA
    if(opc == "2"):
        dose_proy(lista) 
        print ("Regresando al Menu")
        time.sleep(2)
        clean(var)


    #MODULO DE DOSIS REAL-TIME
    if(opc == "3"):
        dose=dose_now(lista)
        ml=ml_last(lista)
        pctes=len(lista2)
        print ("la Dosis actual es:",dose," mCi, en:",ml,"mL\nActualmente se han realizado",pctes,"pacientes")
        
        print ("Regresando al Menu")
        time.sleep(5)
        clean(var)
        
        

    #MODULO DE CALCULO ML
    if(opc == "4"):
        ml=dose_ml(lista)
        print ("Regresando al Menu")
        time.sleep(2)
        clean(var)
       
	
    #MODULO DE INGRESO DATO ACTUALIZADO
    if(opc == "5"):
        input_data(lista) 
        print ("Regresando al Menu")
        time.sleep(2)
        clean(var)
  

    #MODULO DE GENERACION DE REPORTE
    if(opc == "6"):
        gen_info(lista2)
        crate_file(listafinal)
        print ("Regresando al Menu")
        time.sleep(2)
        clean(var)

    #MODULO DE MODIFICACION
    if(opc == "7"):
        mod_last_dat(lista2,lista)
        print ("Regresando al Menu")
        time.sleep(2)
        clean(var)
