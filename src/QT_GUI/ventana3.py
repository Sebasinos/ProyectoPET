# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        MainWindow.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo2 = QtWidgets.QLabel(self.centralwidget)
        self.titulo2.setGeometry(QtCore.QRect(90, 30, 291, 141))
        self.titulo2.setObjectName("titulo2")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(200, 170, 91, 81))
        self.logo.setStyleSheet("border-image: url(:/logo/radiacion.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.borde1 = QtWidgets.QLabel(self.centralwidget)
        self.borde1.setGeometry(QtCore.QRect(0, 0, 481, 20))
        self.borde1.setStyleSheet("border-image: url(:/borde/borde.png);")
        self.borde1.setText("")
        self.borde1.setObjectName("borde1")
        self.borde2 = QtWidgets.QLabel(self.centralwidget)
        self.borde2.setGeometry(QtCore.QRect(0, 600, 481, 20))
        self.borde2.setStyleSheet("border-image: url(:/borde/borde.png);")
        self.borde2.setText("")
        self.borde2.setObjectName("borde2")
        self.btnvolver = QtWidgets.QPushButton(self.centralwidget)
        self.btnvolver.setGeometry(QtCore.QRect(250, 490, 221, 32))
        self.btnvolver.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.btnvolver.setObjectName("btnvolver")
        self.btn1realtime = QtWidgets.QPushButton(self.centralwidget)
        self.btn1realtime.setGeometry(QtCore.QRect(20, 310, 221, 32))
        self.btn1realtime.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.btn1realtime.setObjectName("btn1realtime")
        self.btn2proyect = QtWidgets.QPushButton(self.centralwidget)
        self.btn2proyect.setGeometry(QtCore.QRect(20, 370, 221, 32))
        self.btn2proyect.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.btn2proyect.setObjectName("btn2proyect")
        self.btn3ml = QtWidgets.QPushButton(self.centralwidget)
        self.btn3ml.setGeometry(QtCore.QRect(20, 430, 221, 32))
        self.btn3ml.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.btn3ml.setObjectName("btn3ml")
        self.btn4newdat = QtWidgets.QPushButton(self.centralwidget)
        self.btn4newdat.setGeometry(QtCore.QRect(250, 310, 221, 32))
        self.btn4newdat.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.btn4newdat.setObjectName("btn4newdat")
        self.btn5mod = QtWidgets.QPushButton(self.centralwidget)
        self.btn5mod.setGeometry(QtCore.QRect(250, 370, 221, 32))
        self.btn5mod.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.btn5mod.setObjectName("btn5mod")
        self.btn6report = QtWidgets.QPushButton(self.centralwidget)
        self.btn6report.setGeometry(QtCore.QRect(250, 430, 221, 32))
        self.btn6report.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.btn6report.setObjectName("btn6report")
        self.btn7reinicio = QtWidgets.QPushButton(self.centralwidget)
        self.btn7reinicio.setGeometry(QtCore.QRect(20, 490, 221, 32))
        self.btn7reinicio.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.btn7reinicio.setObjectName("btn7reinicio")
        self.logo.raise_()
        self.borde1.raise_()
        self.borde2.raise_()
        self.btnvolver.raise_()
        self.btn1realtime.raise_()
        self.btn2proyect.raise_()
        self.btn3ml.raise_()
        self.btn4newdat.raise_()
        self.btn5mod.raise_()
        self.btn6report.raise_()
        self.titulo2.raise_()
        self.btn7reinicio.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; color:#fa9a0a;\">PET Manager</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; color:#fa9a0a;\">Opciones</span></p></body></html>"))
        self.btnvolver.setText(_translate("MainWindow", "Salir"))
        self.btn1realtime.setText(_translate("MainWindow", "Calcular Dosis en Tiempo Real"))
        self.btn2proyect.setText(_translate("MainWindow", "Calcular Dosis Proyectada"))
        self.btn3ml.setText(_translate("MainWindow", "Calcular mL para Dosificación"))
        self.btn4newdat.setText(_translate("MainWindow", "Ingreso de nuevo Datos paciente"))
        self.btn5mod.setText(_translate("MainWindow", "Modificar Ultimo Dato de Paciente"))
        self.btn6report.setText(_translate("MainWindow", "Generar Reporte"))
        self.btn7reinicio.setText(_translate("MainWindow", "Reiniciar Programa"))

import borde
import logo

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

