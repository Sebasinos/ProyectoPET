
def crate_file(listafinal):
    archivo="lista Pacientes Diario.csv"
    csv=open(archivo,"w")
    titulo= "Paciente,Dosis,Hora,mL\n"
    csv.write(titulo)

    s=0
    for linea in listafinal:
        pcte,dosis,hora,ml=listafinal[s][0],listafinal[s][1],listafinal[s][2],listafinal[s][3],
        filas=pcte+","+dosis+","+hora+","+ml+"\n"
        csv.write(filas)
        s=s+1
    csv.close()
    print ("Reporte generado con Exito")
