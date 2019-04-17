import os 
import math
import datetime as dt
import time

#--Calculator time--#

def dif_min_now(time_x):
    now= dt.datetime.now()
    time_x=time_x.replace(year=now.year, month=now.month, day=now.day)
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
    des_fluor =float(109.771)
    minutos=float(minut_decay)
    act_fin=dose_act*(math.exp(-(0.693*minutos/des_fluor)))
    return act_fin