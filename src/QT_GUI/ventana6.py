# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana6.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 637)
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
        self.Ltit2 = QtWidgets.QLabel(self.centralwidget)
        self.Ltit2.setGeometry(QtCore.QRect(90, 250, 301, 61))
        self.Ltit2.setObjectName("Ltit2")
        self.btncalcula = QtWidgets.QPushButton(self.centralwidget)
        self.btncalcula.setGeometry(QtCore.QRect(110, 540, 113, 32))
        self.btncalcula.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.btncalcula.setObjectName("btncalcula")
        self.btnvolver = QtWidgets.QPushButton(self.centralwidget)
        self.btnvolver.setGeometry(QtCore.QRect(260, 540, 113, 32))
        self.btnvolver.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.btnvolver.setObjectName("btnvolver")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(190, 300, 101, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.textBrowser.setObjectName("textBrowser")
        self.Lmsg = QtWidgets.QLabel(self.centralwidget)
        self.Lmsg.setGeometry(QtCore.QRect(90, 360, 301, 41))
        self.Lmsg.setObjectName("Lmsg")
        self.lResultado = QtWidgets.QLabel(self.centralwidget)
        self.lResultado.setGeometry(QtCore.QRect(90, 440, 301, 81))
        self.lResultado.setObjectName("lResultado")
        self.ltit3 = QtWidgets.QLabel(self.centralwidget)
        self.ltit3.setGeometry(QtCore.QRect(80, 410, 321, 31))
        self.ltit3.setObjectName("ltit3")
        self.logo.raise_()
        self.borde1.raise_()
        self.borde2.raise_()
        self.titulo2.raise_()
        self.Ltit2.raise_()
        self.btncalcula.raise_()
        self.btnvolver.raise_()
        self.textBrowser.raise_()
        self.Lmsg.raise_()
        self.lResultado.raise_()
        self.ltit3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; color:#fa9a0a;\">PET Manager</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; color:#fa9a0a;\">Calculo mL</span></p></body></html>"))
        self.Ltit2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#f98900;\">Ingresar Hora a Proyectar</span></p></body></html>"))
        self.btncalcula.setText(_translate("MainWindow", "Calcular"))
        self.btnvolver.setText(_translate("MainWindow", "Volver"))
        self.Lmsg.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ff0000;\">Msg</span></p></body></html>"))
        self.lResultado.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:64pt; font-weight:600; color:#ff8000;\">Resultado</span></p></body></html>"))
        self.ltit3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#f98900;\">Para la hora ingresada la dosis sera:</span></p></body></html>"))

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

