# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana9.ui'
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
        self.titulo2.setGeometry(QtCore.QRect(40, 30, 401, 141))
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
        self.Ldosis = QtWidgets.QLabel(self.centralwidget)
        self.Ldosis.setGeometry(QtCore.QRect(100, 290, 291, 21))
        self.Ldosis.setObjectName("Ldosis")
        self.capdosis = QtWidgets.QTextEdit(self.centralwidget)
        self.capdosis.setGeometry(QtCore.QRect(110, 330, 281, 41))
        self.capdosis.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.capdosis.setObjectName("capdosis")
        self.BtnIngresar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnIngresar.setGeometry(QtCore.QRect(120, 540, 113, 32))
        self.BtnIngresar.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.BtnIngresar.setObjectName("BtnIngresar")
        self.btnvolver = QtWidgets.QPushButton(self.centralwidget)
        self.btnvolver.setGeometry(QtCore.QRect(270, 540, 113, 32))
        self.btnvolver.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.btnvolver.setObjectName("btnvolver")
        self.logo.raise_()
        self.borde1.raise_()
        self.borde2.raise_()
        self.titulo2.raise_()
        self.Ldosis.raise_()
        self.capdosis.raise_()
        self.BtnIngresar.raise_()
        self.btnvolver.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; color:#fa9a0a;\">PET Manager</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; color:#fa9a0a;\">Generar Reporte</span></p></body></html>"))
        self.Ldosis.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ea9700;\">Ingresar Correo electronico a enviar</span></p></body></html>"))
        self.BtnIngresar.setText(_translate("MainWindow", "Enviar"))
        self.btnvolver.setText(_translate("MainWindow", "Volver"))

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

