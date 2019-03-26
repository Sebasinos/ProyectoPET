# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ventana2(object):
    def setupUi(self, ventana2):
        ventana2.setObjectName("ventana2")
        ventana2.resize(480, 640)
        ventana2.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.centralwidget = QtWidgets.QWidget(ventana2)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo2 = QtWidgets.QLabel(self.centralwidget)
        self.titulo2.setGeometry(QtCore.QRect(90, 30, 291, 141))
        self.titulo2.setObjectName("titulo2")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(180, 160, 111, 101))
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
        self.Ldosis.setGeometry(QtCore.QRect(110, 290, 59, 21))
        self.Ldosis.setObjectName("Ldosis")
        self.Lhora = QtWidgets.QLabel(self.centralwidget)
        self.Lhora.setGeometry(QtCore.QRect(100, 370, 81, 21))
        self.Lhora.setObjectName("Lhora")
        self.Lml = QtWidgets.QLabel(self.centralwidget)
        self.Lml.setGeometry(QtCore.QRect(110, 450, 59, 21))
        self.Lml.setObjectName("Lml")
        self.capdosis = QtWidgets.QTextEdit(self.centralwidget)
        self.capdosis.setGeometry(QtCore.QRect(190, 290, 121, 31))
        self.capdosis.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.capdosis.setObjectName("capdosis")
        self.caphora = QtWidgets.QTextEdit(self.centralwidget)
        self.caphora.setGeometry(QtCore.QRect(190, 370, 121, 31))
        self.caphora.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.caphora.setObjectName("caphora")
        self.capml = QtWidgets.QTextEdit(self.centralwidget)
        self.capml.setGeometry(QtCore.QRect(190, 450, 121, 31))
        self.capml.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.capml.setObjectName("capml")
        self.btnvolver_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnvolver_2.setGeometry(QtCore.QRect(120, 540, 113, 32))
        self.btnvolver_2.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.btnvolver_2.setObjectName("btnvolver_2")
        self.btnvolver = QtWidgets.QPushButton(self.centralwidget)
        self.btnvolver.setGeometry(QtCore.QRect(270, 540, 113, 32))
        self.btnvolver.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.btnvolver.setObjectName("btnvolver")
        self.BtnIngresar_do = QtWidgets.QPushButton(self.centralwidget)
        self.BtnIngresar_do.setGeometry(QtCore.QRect(330, 290, 71, 32))
        self.BtnIngresar_do.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.BtnIngresar_do.setObjectName("BtnIngresar_do")
        self.BtnIngresar_ho = QtWidgets.QPushButton(self.centralwidget)
        self.BtnIngresar_ho.setGeometry(QtCore.QRect(330, 370, 71, 32))
        self.BtnIngresar_ho.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.BtnIngresar_ho.setObjectName("BtnIngresar_ho")
        self.BtnIngresar_ml = QtWidgets.QPushButton(self.centralwidget)
        self.BtnIngresar_ml.setGeometry(QtCore.QRect(330, 450, 71, 32))
        self.BtnIngresar_ml.setStyleSheet("background-color: rgb(252, 176, 0);")
        self.BtnIngresar_ml.setObjectName("BtnIngresar_ml")
        self.errordosis = QtWidgets.QTextEdit(self.centralwidget)
        self.errordosis.setGeometry(QtCore.QRect(100, 330, 331, 31))
        self.errordosis.setObjectName("errordosis")
        self.errorhora = QtWidgets.QTextEdit(self.centralwidget)
        self.errorhora.setGeometry(QtCore.QRect(100, 410, 331, 31))
        self.errorhora.setObjectName("errorhora")
        self.errorml = QtWidgets.QTextEdit(self.centralwidget)
        self.errorml.setGeometry(QtCore.QRect(100, 490, 331, 31))
        self.errorml.setObjectName("errorml")
        ventana2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ventana2)
        self.statusbar.setObjectName("statusbar")
        ventana2.setStatusBar(self.statusbar)

        self.retranslateUi(ventana2)
        QtCore.QMetaObject.connectSlotsByName(ventana2)

    def retranslateUi(self, ventana2):
        _translate = QtCore.QCoreApplication.translate
        ventana2.setWindowTitle(_translate("ventana2", "MainWindow"))
        self.titulo2.setText(_translate("ventana2", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; color:#fa9a0a;\">PET Manager</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; color:#fa9a0a;\">Datos Iniciales</span></p></body></html>"))
        self.Ldosis.setText(_translate("ventana2", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ea9700;\">Dosis</span></p></body></html>"))
        self.Lhora.setText(_translate("ventana2", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#e89600;\">Hora:min</span></p></body></html>"))
        self.Lml.setText(_translate("ventana2", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#e89600;\">mL</span></p></body></html>"))
        self.btnvolver_2.setText(_translate("ventana2", "Volver"))
        self.btnvolver.setText(_translate("ventana2", "Menu Principal"))
        self.BtnIngresar_do.setText(_translate("ventana2", "Ingresar"))
        self.BtnIngresar_ho.setText(_translate("ventana2", "Ingresar"))
        self.BtnIngresar_ml.setText(_translate("ventana2", "Ingresar"))
        self.errordosis.setHtml(_translate("ventana2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.errorhora.setHtml(_translate("ventana2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.errorml.setHtml(_translate("ventana2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

import borde_rc
import logo_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana2 = QtWidgets.QMainWindow()
    ui = Ui_ventana2()
    ui.setupUi(ventana2)
    ventana2.show()
    sys.exit(app.exec_())

