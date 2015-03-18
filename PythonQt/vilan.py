# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vilan.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VILAN(object):
    def setupUi(self, VILAN):
        VILAN.setObjectName("VILAN")
        VILAN.resize(708, 469)
        self.centralWidget = QtWidgets.QWidget(VILAN)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(160, 110, 371, 191))
        font = QtGui.QFont()
        font.setFamily("Raavi")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(161, 161, 161);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Raavi\";\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.label.setStyleSheet("color: rgb(165, 165, 165);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 81, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_username = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_username.setGeometry(QtCore.QRect(100, 60, 251, 20))
        self.lineEdit_username.setStyleSheet("font: 75 11pt \"Myriad Web Pro Condensed\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_username.setText("")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_password.setGeometry(QtCore.QRect(100, 110, 251, 20))
        self.lineEdit_password.setStyleSheet("font: 75 11pt \"Myriad Web Pro Condensed\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(190, 150, 75, 23))
        self.pushButton.setStyleSheet("color: rgb(152, 152, 152);\n"
"color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 150, 75, 23))
        self.pushButton_2.setStyleSheet("color: rgb(152, 152, 152);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 791, 561))
        self.widget.setStyleSheet("background-image: url(\"C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/pic.jpg\");")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.groupBox.raise_()
        VILAN.setCentralWidget(self.centralWidget)

        self.retranslateUi(VILAN)
        QtCore.QMetaObject.connectSlotsByName(VILAN)

    def retranslateUi(self, VILAN):
        _translate = QtCore.QCoreApplication.translate
        VILAN.setWindowTitle(_translate("VILAN", "VILAN"))
        self.groupBox.setTitle(_translate("VILAN", "Welcome"))
        self.label.setText(_translate("VILAN", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">USERNAME</span></p></body></html>"))
        self.label_2.setText(_translate("VILAN", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">PASSWORD</span></p></body></html>"))
        self.pushButton.setText(_translate("VILAN", "Login"))
        self.pushButton_2.setText(_translate("VILAN", "Sign Up"))

