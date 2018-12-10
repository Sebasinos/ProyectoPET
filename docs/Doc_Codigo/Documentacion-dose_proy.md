# ProyectoPET
Proyecto PETManager

## **Documentacion**
## **Archivo:**
dose_proy.py
## **Objetivo**: Calcular el valor de dosis proyectada basada en una hora futura.
## **Datos de Entrada:**
*Hora determinada en formato HH:MM

## **Datos de Salida:**
*dosis en formato float, con 3 decimales.

## **Variables:**
*hour_x = llama a modulo chec_input_hora.

*act_ini = llama al modulo dose_last(dando como parametro la lista).

*time = llama al modulo time_last(dando como parametro la lista).

*minutos= llama al modulo dif_min_proy(parametros time y hour_x)

*dose= llama al modulo cal_decay(parametros act_ini y minutos).

*dose= redondea el valor dose a 3 decimales.


## **Observaciones**
Este Modulo se conecta con varios modulos que permiten calcular una proyeccion de dosis en tiempo. basada en el ultimo registro de dosis realizada y el tiempo ingresado por el usuario.
