import math
#Se transforma a funcion , para recibir los parametros desde los modulos que realizan check de los datos.
def cal_decay(dose_act,minut_decay):
    dose_act=float(dose_act)
    des_fluor =float(109.771)
    minutos=float(minut_decay)
    act_fin=dose_act*(math.exp(-(0.693*minutos/des_fluor)))
   
    return act_fin
