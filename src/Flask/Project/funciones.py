import os 
import math
import datetime as dt
import time

#--Calculator time--#

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