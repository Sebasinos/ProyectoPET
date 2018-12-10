import os 
import math
import time
import datetime as dt

def dose_proy(lista):
    hour_x=check_input_hora()
    act_ini=dose_last(lista)
    time=time_last(lista)
    minutos=dif_min_proy(time,hour_x)
    dose=cal_decay(act_ini,minutos)
    dose=round(dose,3)
    print ("la dosis proyectada para las",hour_x," es", dose, "mCi")
    return dose
