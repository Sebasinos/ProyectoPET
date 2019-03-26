#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:50:31 2019

@author: Sebas
"""

import sys
from PyQt5 import uic, QtWidgets
from ventana2 import Ui_ventana2

qtCreatorFile = "ventana1.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.botondi.clicked.connect(self.abrirIDat)

        
    def abrirIDat (self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_ventana2()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        self.BtnIngresar_do.clicked.connect(self.check_input_dose)
        
    def check_input_dose(self):
        dosis_u=(self.capdosis.toPlainText())
        errordos= str("Debe ingresar valores separador por PUNTO(.) y solo 2 decimales")
        self.errordosis.setText(errordos)

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_()) 