#!/usr/bin/python
# -*- coding: utf-8 -*-
import os 
import math
import time
import datetime as dt

#VARIABLES GLOBALES

lista= []

#-------CHECK INPUTS---------#

#FUNCION CHECK INPUT / SOLICITA EL DATO Permite filtrar str involuntario y el ingreso de mas de 2 decimales.

def check_input_dose():
    while True:
        dosis_u = input("Ingrese Dosis con punto y solo 2 decimales")
        try:
            dosis_u =float(dosis_u)
            dosis_u="%.*f" % (2, dosis_u)
            print (dosis_u)
            return dosis_u
            
        except ValueError:
            print ("Debe ingresar valores separador por PUNTO y solo dos decimales")

def check_input_ml():
    while True:
        ml_u = input("Ingrese cantidad de ml con punto y solo 2 decimales")
        try:
            ml_u =float(ml_u)
            ml_u="%.*f" % (2, ml_u)
            print (ml_u)
            return ml_u
            
        except ValueError:
            print ("Debe ingresar valores separador por PUNTO y solo dos decimales si tiene.")


def check_input_time():
    while True:
        time_u = input("Ingrese tiempo en minutos, ej 22 ")
        try:
            time_u =int(time_u)
            print (time_u)
            return time_u
            
        except ValueError:
            print ("Debe ingresar valores ENTEROS")

def check_input_hora():
    while True:
        data = input("Ingrese hora en formato HH:MM")
        try:
            time.strptime(data, "%H:%M")
            hour=time.strptime(data, "%H:%M")
            hour_min=time.strftime('%H:%M', hour)
            print (hour_min)
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



def menu():
	#MENU DE OPCIONES
	print("** ::::::::::::::::::::::::: **")
	print(":: Seleccione una Opcion ::")
	print("** ::::::::::::::::::::::::: **")
	print("-------------------------------")
	print("| Ingresar Dosis Inicial   :->  1     |")
	print("| Calcular Dosis Proyectada:->  2     |")
	print("| Calcular Dosis Real-Time: ->  3     |")
	print("| Calcular mL para X dosis: ->  4     |")
	print("| Ingreso dato actualizado: ->  5     |") 
	print("| Generar Reporte :         ->  6     |")
	print("| Salir:                    ->  s     |")
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
    menuPrincipal = menu()
    opc = opciones()
    #OPCIÓN DEL MENU

    #MODULO DE INGRESO DOSIS INICIAL
    if(opc == "1"):
        dose_inicio()
        print ("Regresando al Menu")
    
	
    #MODULO DE DOSIS PROYECTADA
    if(opc == "2"):
        print ("Regresando al Menu")


    #MODULO DE DOSIS REAL-TIME
    if(opc == "3"):
        dose=dose_now(lista)
        print ("la Dosis para este momento es;",dose," mCi")       
        print ("Regresando al Menu")

    #MODULO DE CALCULO ML
    if(opc == "4"):
        print ("Regresando al Menu")
       
	
    #MODULO DE INGRESO DATO ACTUALIZADO
    if(opc == "5"):
        print ("Regresando al Menu")
  

    #MODULO DE GENERACION DE REPORTE
    if(opc == "6"):
        print ("Regresando al Menu")
    

    
