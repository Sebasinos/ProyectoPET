# ProyectoPET
Proyecto PETManager

## **Documentacion**
## **Archivo:**
input_data.py
## **Objetivo**: Ingresar valores actualizados de dosis , hora y ml. Estos son los datos que corresponde a la dosificacion que se realiza a cada paciente cada vez que se manipula el farmaco.
## **Datos de Entrada:**
*lista / Valores guardados en la lista

*dosis / Valores ingresados por el Usuario 

*tiempo / Valores ingresados por el Usuario

*ml / Valores ingresados por el Usuario

## **Datos de Salida:**
*print con msg: Datos Ingresados con Exito

## **Variables:**

*act_dose = llama al modulo dose_last() con parametro lista.

*act_ml = llama al modulo ml_last() con parametro lista.

*act_hour = llama al modulo time_last() con parametro lista.

*new_dose = llama al modulo Check_input_dose.

*new_hour = llama al modulo Check_input_hora.

*new_ml= llama al modulo Check_input_ml.

*minutos= llama al modulo dif_min_proy() con parametros act_hour , new_hour

*doserefresh= llama al modulo cal_decay() con parametros act_dose , minutos)

*mlrefresh= resta entre ml_last (ultimo valor ml de lista) y new_ml (ml ingresado por el usuario) en formato float.

*tupla= tupla con los datos nuevos ingresado por el usuario (new_dose, new_hour,new_ml).

*lista2= lista que almacena los valores ingresador por el usuario por cada manipulacion.

*tupla_act= crea tupla con datos calculados y actualizados (doserefresh, new_hour, mlrefresh) foramto str. esta se almacena en lista

## **Observaciones**
Este Modulo se conecta con varios modulos y requiere de datos almacendaos en la lista e ingresados por el usuario. La tupla es almacenada en la lista2 y la tupla_act es almacenada en la lista. finalmente  retorna un msg de verificacion de ingreso.
