#FUNCION MODIFICACION ULTIMO PACIENTE INGRESADO
def mod_last_dat(lista2,lista):
    if (lista2 == []):
        print("No hay pacientes para modificar")

    else:
        opc=0
        while opc != "s":
            print("Ingrese una opcion valida")
            menuPrincipal = menu_mod()
            opc = opciones()
            
            if(opc == "1"):
                dose=check_input_dose()
                lis=list(lista2[-1])
                lis[0]=dose
                hour=lis[1]
                ml=lis[2]
                listanew=tuple(lis)
                lista2.pop(-1)
                lista2.append(listanew)
                lista.pop(-1)
                input_data_mod(dose,hour,ml)
                print ("Regresando al Menu")

            if(opc == "2"):
                hour=check_input_hora()
                lis=list(lista2[-1])
                lis[1]=hour
                dose=lis[0]
                ml=lis[2]
                listanew=tuple(lis)
                lista2.pop(-1)
                lista2.append(listanew)
                lista.pop(-1)
                input_data_mod(dose,hour,ml)
                print ("Regresando al Menu")


            if(opc == "3"):
                ml=check_input_ml()
                lis=list(lista2[-1])
                lis[2]=ml
                dose=lis[0]
                hour=lis[1]
                listanew=tuple(lis)
                lista2.pop(-1)
                lista2.append(listanew)
                lista.pop(-1)
                input_data_mod(dose,hour,ml)
                print ("Regresando al Menu")
        


