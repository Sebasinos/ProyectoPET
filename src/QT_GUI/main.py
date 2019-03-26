#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 21:46:46 2019

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
        self.botondi.clicked.connect(self.abrirIngresoDosis)

        
    def abrirIngresoDosis (self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_ventana2()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())