# ProyectoPET
Proyecto PETManager

## **Documentacion**
## **Archivo:**
mod_last_dat.py
## **Objetivo**: Modificar los datos de trabajo del ultimo paciente ingresado.
## **Datos de Entrada:**
*lista / valores que se encunetran en la lista (Datos de Radiofarmaco)

*lista2 / valores que se encunetran en la lista2 (Datos de dosis por paciente)

## **Datos de Salida:**
*Modificación de datos seleccionado - print que confirma operación.

## **Variables:**

*opc = guarda opción ingresada por usuario.

*menuPrincipal = llama al modulo menu_mod().

*dose= modificación de dosis/ ultima dosis ingresada.

*hour= modificación de hora/ ultima hora ingresada.

*ml= modificación de ml/ ultimo ml ingresado.

*lis= guarda ultima tupla de datos ingresada.

*lista2= se elimina ultima tupla ingresada y luego se agrega tupla nueva.

*lista= se elimina ultima tupla generada con los datos erroneos.

*input_data_mod = funcion donde se dan como parametros (dose,hour,ml).


## **Observaciones**
Este Modulo se conecta con otros modulos que permiten modificar el ultimo grupo de datos ingresado por el usuario (respecto al paciente). Posee 3 condiciones para modificar de manera separada: Dosis - Hora - mL . cuenta con el uso de una funcion de menu para seleccionar la opcion a modificar y un comando para salir del menu de modificacion y volver al menu principal.
Los datos modificados son actualizados con los datos del radiofarmaco gracias a la funcion input_data_mod(dose,hour,ml).
