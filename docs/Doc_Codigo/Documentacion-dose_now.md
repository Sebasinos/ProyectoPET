# ProyectoPET
Proyecto PETManager

## **Documentacion**
## **Archivo:**
dose_now.py
## **Objetivo**: Calcular el valor de dosis en el momento actual (Tiempo real).
## **Datos de Entrada:**
*lista / valores que se encunetran en la lista 

## **Datos de Salida:**
*dosis en formato float, con 3 decimales.

## **Variables:**

*act_ini = llama al modulo dose_last(dando como parametro la lista).

*time = llama al modulo time_last(dando como parametro la lista).

*minutos= llama al modulo dif_min(parametros time)

*dose_now= llama al modulo cal_decay(parametros act_ini y minutos).

*dose_now= redondea el valor dose a 3 decimales.


## **Observaciones**
Este Modulo se conecta con varios modulos que permiten calcular una proyeccion de dosis en tiempo real. basada en el ultimo registro de dosis realizada y el tiempo de pc en el momento actual.
