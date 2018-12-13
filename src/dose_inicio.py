#FUNCION INGRESO DE DOSIS INICIAL
def dose_inicio():
    dose=check_input_dose()
    hour=check_input_hora()
    ml=check_input_ml()
    tupla=(dose,hour,ml)
    lista.append(tupla)
    print ("Datos ingresados con exito")
