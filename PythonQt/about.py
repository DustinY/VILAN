# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(567, 478)
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(160, 70, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(About)
        self.label_2.setGeometry(QtCore.QRect(320, 290, 161, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(About)
        self.label_3.setGeometry(QtCore.QRect(320, 320, 141, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(About)
        self.label_4.setGeometry(QtCore.QRect(320, 380, 121, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(About)
        self.label_5.setGeometry(QtCore.QRect(320, 350, 121, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(About)
        self.label_6.setGeometry(QtCore.QRect(190, 450, 251, 20))
        self.label_6.setObjectName("label_6")
        self.widget = QtWidgets.QWidget(About)
        self.widget.setGeometry(QtCore.QRect(0, 0, 571, 491))
        self.widget.setStyleSheet("background-image: url(\"C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/background.jpg\");")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Dialog"))
        self.label.setText(_translate("About", "<html><head/><body><p><span style=\" color:#ffffff;\">V.I.L.A.N</span></p></body></html>"))
        self.label_2.setText(_translate("About", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Marvin Itzep</span></p></body></html>"))
        self.label_3.setText(_translate("About", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Dustin York</span></p></body></html>"))
        self.label_4.setText(_translate("About", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Daanyaal Syed</span></p></body></html>"))
        self.label_5.setText(_translate("About", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Vicken Krikorian</span></p></body></html>"))
        self.label_6.setText(_translate("About", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">CSULA-Winter 20015-CS437</span></p></body></html>"))

