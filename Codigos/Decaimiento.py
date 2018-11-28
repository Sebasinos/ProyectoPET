import math

Act_ini = float(raw_input("Ingrese Actividad Inicial: "))
tiempo = float(raw_input("Ingrese tiempo: "))
des_fluor =float(109.771)
Act_fin =Act_ini*(math.exp(-(0.693*float(tiempo)/des_fluor)))

print "El decaimiento es", Act_fin
