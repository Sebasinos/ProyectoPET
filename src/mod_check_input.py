#-------CHECK INPUTS---------#

#FUNCION CHECK INPUT / SOLICITA EL DATO Permite filtrar str involuntario y el ingreso de mas de 2 decimales.

def check_input_dose():
    while True:
        dosis_u = input("Ingrese Dosis con punto y solo 2 decimales\n")
        try:
            dosis_u =float(dosis_u)
            dosis_u="%.*f" % (2, dosis_u)
            return dosis_u
            
        except ValueError:
            print ("Debe ingresar valores separador por PUNTO y solo dos decimales")

def check_input_ml():
    while True:
        ml_u = input("Ingrese cantidad de ml con punto y solo 2 decimales\n")
        try:
            ml_u =float(ml_u)
            ml_u="%.*f" % (2, ml_u)
            return ml_u
            
        except ValueError:
            print ("Debe ingresar valores separador por PUNTO y solo dos decimales si tiene.")


def check_input_time():
    while True:
        time_u = input("Ingrese tiempo en minutos, ej 22 \n")
        try:
            time_u =int(time_u)
            return time_u
            
        except ValueError:
            print ("Debe ingresar valores ENTEROS")

def check_input_hora():
    while True:
        data = input("Ingrese hora en formato HH:MM \n")
        try:
            time.strptime(data, "%H:%M")
            hour=time.strptime(data, "%H:%M")
            hour_min=time.strftime('%H:%M', hour)
            return hour_min
        except ValueError:
            print ("Debe ingresar formato valido HH:MM ")


