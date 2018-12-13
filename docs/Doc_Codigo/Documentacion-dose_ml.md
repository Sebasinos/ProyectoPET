# ProyectoPET
Proyecto PETManager

## **Documentacion**
## **Archivo:**
dose_ml.py
## **Objetivo**: Calcular los ml necesarios para obtener cierta cantidad de Dosis (mCi) en tiempo real.
## **Datos de Entrada:**
*Lista / Valores guardados en la lista

*dosis / Valores ingresados por el Usuario 

## **Datos de Salida:**
*print con msg: Los ml necesarios para tener "Dosis requerida" , son "Resultado" ml.

## **Variables:**

*dose_req = llama al modulo Check_input_dose. Dosis requerida 

*dose_act = llama al modulo dose_last() con parametro lista y lo transforma a formato float . ultima dosis ingresada al sistema

*ml_act = llama al modulo ml_last() con parametro lista y lo transforma a formato float . ultimo ml ingresado al sistema

*ml= regla de 3 simples con los datos - dose_req , ml_act y dose_act

*ml = reodnde el resultado a 1 decimal



## **Observaciones**
Este Modulo se conecta con varios modulos y recoge datos almacendaos en la lista y datos suministrados por el usuario en ese momento .Da como resultado el msg con la cantidad de ml que se requieren para cierta actividad en el momento que se realiza la consulta.
