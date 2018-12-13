#FUNCION DOSIS REAL-TIME
def dose_now(lista):
    act_ini=dose_last(lista)
    time=time_last(lista)
    minutos=dif_min(time)
    dose_now=cal_decay(act_ini,minutos)
    dose_now=round(dose_now,3)
    return dose_now
            
