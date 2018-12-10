import time
import datetime as dt

#-----CALCULATOR-------#
#Calculo de minutos entre dos horas formato HH:MM.

def dif_min_proy(time_1,time_2):
    start_dt = dt.datetime.strptime(time_2, '%H:%M')
    end_dt = dt.datetime.strptime(time_1, '%H:%M')
    diff = (start_dt - end_dt)
    minutos= int(diff.seconds/60)
    print (minutos)
    return minutos
