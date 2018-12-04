# ProyectoPET
Proyecto PETManager

## **Documentacion**
## **Archivo:**
Programa_principal.py
## **Objetivo**: Base de la aplicacion para realizar test de los modulos y funcionalidades.

## **Funcionalidad Dose_now:**
Funcion de dosis en tiempo real. 

## **Datos de Entrada:**
*lista = Datos consistentes en tuplas que almacenan informacion de dosis, hora y ml)

## **Datos de Salida:**
*Activdad en tiempo real como valor float 

## **Variables:**
*act_ini= ultima dosis registrada en la lista de datos local (llama al metodo - dose_last(lista) dando como parametro la lista).

*time = ultimo tiempo registrado de medicion de dosis (llama a metodo - time_last(lista) dando como parametro la lista).

*minutos= cantidad de minutos transcurridos entre la ultima dosis medida y el tiempo actual (llama al metodo dif_min(time) dando como parametro la variable time).

*dose_now= dosis en tiempo real (llama al metodo cal_decay(act_ini,minutos) dando como parametro las variables act_ini y minutos), luego el resultado es un float que se redondea con 3 decimales.


## **Observaciones**
Este Modulo a traves de la funcion menu() entrega en pantalla la cantidad de actividad en tiempo real.
