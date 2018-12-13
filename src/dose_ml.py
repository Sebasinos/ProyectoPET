#FUNCION CANTIDAD ML-DOSIS
def dose_ml(lista):
    dose_req=float(check_input_dose())
    dose_act=float(dose_last(lista))
    ml_act=float(ml_last(lista))
    ml= (dose_req*ml_act)/dose_act
    ml= round(ml,1)
    print ("Los ml necesarios para tener", dose_req, "mCi, son: ", ml, "ml")
