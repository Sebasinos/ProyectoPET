import time
import datetime as dt

#-----CALCULATOR-------#
#Calculo de minutos entre una hora formato HH:MM y el tiempo Actual del computador            
def dif_min(time_x):
    now= time.strftime('%H:%M')
    start_dt = dt.datetime.strptime(now, '%H:%M')
    end_dt = dt.datetime.strptime(time_x, '%H:%M')
    diff = (start_dt - end_dt)
    minutos= int(diff.seconds/60)
    return minutos
