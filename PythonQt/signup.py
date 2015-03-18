# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_SignUp(object):
    def setupUi(self, SignUp):
        SignUp.setObjectName("SignUp")
        SignUp.resize(389, 406)
        self.label = QtWidgets.QLabel(SignUp)
        self.label.setGeometry(QtCore.QRect(60, 100, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(SignUp)
        self.label_2.setGeometry(QtCore.QRect(60, 150, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(SignUp)
        self.label_3.setGeometry(QtCore.QRect(60, 190, 71, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_username = QtWidgets.QLineEdit(SignUp)
        self.lineEdit_username.setGeometry(QtCore.QRect(140, 100, 181, 20))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(SignUp)
        self.lineEdit_password.setGeometry(QtCore.QRect(140, 150, 181, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password2 = QtWidgets.QLineEdit(SignUp)
        self.lineEdit_password2.setGeometry(QtCore.QRect(140, 190, 181, 20))
        self.lineEdit_password2.setObjectName("lineEdit_password2")
        self.pushButton = QtWidgets.QPushButton(SignUp)
        self.pushButton.setGeometry(QtCore.QRect(110, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(SignUp)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 250, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(SignUp)
        self.widget.setGeometry(QtCore.QRect(0, 0, 391, 411))
        self.widget.setStyleSheet("background-image: url(\"C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/background.jpg\");")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEdit_username.raise_()
        self.lineEdit_password.raise_()
        self.lineEdit_password2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)

    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "Dialog"))
        self.label.setText(_translate("SignUp", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Username:</span></p></body></html>"))
        self.label_2.setText(_translate("SignUp", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Password:</span></p></body></html>"))
        self.label_3.setText(_translate("SignUp", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Re-Enter:</span></p></body></html>"))
        self.pushButton.setText(_translate("SignUp", "OK"))
        self.pushButton_2.setText(_translate("SignUp", "CANCEL"))
