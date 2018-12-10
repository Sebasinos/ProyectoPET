# ProyectoPET
Proyecto PETManager

## **Documentacion**
## **Archivo:**
cal_decay.py
## **Objetivo**: Realizar el calculo del decaimiento radiactivo de un radiofarmaco
## **Datos de Entrada:**
*Requiere el valor numerico de Dosis inicial medida en milicuries (mCi) con dos decimales Ej 180.39
*Requiere el valor entero de tiempo en Minutos (min) que transcurre desde la actividad inicial a la hora de medida requerida Ej 55

## **Datos de Salida:**
*Valor de Decaimiento radiactivo de fluor en milicuries (mCi) de FDG en el periodo de tiempo establecido - tipo float.

## **Variables:**
*dose_act = float / Actividad Inicial del Radiofarmaco. transforma a float valor ingresado

*minutos = float / Tiempo de decaimiento del Radiofarmaco.

*des_fluor =float(109.771) / Valor fijo para Radifarmaco FLuor18- Constante de decaimiento propia del elemento.

*act_fin = float / Resultado - Actividad Final calculada.


## **Formula**
La formula se basa en la ley de Decaimiento radiactivo
![fomula decaimiento radiactivo](http://2.bp.blogspot.com/-5Frs2P2kPg0/U1O5U789ycI/AAAAAAAAAZw/j1ruPf8Imsw/s1600/F%C3%B3rmula+de+la+desintegraci%C3%B3n.jpg)

## **Observaciones**
Este Modulo de calculo de decaimiento debara comunicarse con el Modulo de check_inputs, modulos que impliquen calculo de decaimiento radiactivo - Dose_now , Dose_proy y el colector de datos.
