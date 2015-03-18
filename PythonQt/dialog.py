# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(609, 499)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(140, 130, 301, 361))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit_voice = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_voice.setGeometry(QtCore.QRect(130, 40, 271, 20))
        self.lineEdit_voice.setObjectName("lineEdit_voice")
        self.lineEdit_command = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_command.setGeometry(QtCore.QRect(130, 70, 271, 20))
        self.lineEdit_command.setObjectName("lineEdit_command")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 91, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 61, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(410, 40, 71, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 150, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(500, 460, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 621, 501))
        self.widget.setStyleSheet("background-image: url(\"C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/background.jpg\");")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.textBrowser.raise_()
        self.lineEdit_voice.raise_()
        self.lineEdit_command.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_5.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#afafaf;\">Voice Command</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#b4b4b4;\">Command</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "ADD"))
        self.pushButton_2.setText(_translate("Dialog", "RELOAD"))
        self.pushButton_5.setText(_translate("Dialog", "DONE"))

