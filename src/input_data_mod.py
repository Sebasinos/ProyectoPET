#FUNCION ACTUALIZACION VALORES DE RADIOFARMACO TRAS MODIFICACION
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
