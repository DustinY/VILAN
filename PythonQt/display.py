# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Display(object):
    def setupUi(self, Display):
        Display.setObjectName("Display")
        Display.resize(592, 481)
        self.pushButton = QtWidgets.QPushButton(Display)
        self.pushButton.setGeometry(QtCore.QRect(230, 420, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Display)
        self.textBrowser.setGeometry(QtCore.QRect(30, 50, 241, 351))
        self.textBrowser.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Display)
        self.textBrowser_2.setGeometry(QtCore.QRect(320, 50, 241, 351))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label = QtWidgets.QLabel(Display)
        self.label.setGeometry(QtCore.QRect(90, 20, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Display)
        self.label_2.setGeometry(QtCore.QRect(390, 20, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(Display)
        self.widget.setGeometry(QtCore.QRect(0, 0, 591, 481))
        self.widget.setStyleSheet("background-image: url(\"C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/background.jpg\");")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.pushButton.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        self.label.raise_()
        self.label_2.raise_()

        self.retranslateUi(Display)
        QtCore.QMetaObject.connectSlotsByName(Display)

    def retranslateUi(self, Display):
        _translate = QtCore.QCoreApplication.translate
        Display.setWindowTitle(_translate("Display", "Dialog"))
        self.pushButton.setText(_translate("Display", "LOAD COMMANDS"))
        self.label.setText(_translate("Display", "<html><head/><body><p><span style=\" color:#9e9e9e;\">Default List</span></p></body></html>"))
        self.label_2.setText(_translate("Display", "<html><head/><body><p><span style=\" color:#ababab;\">Custom List</span></p></body></html>"))

