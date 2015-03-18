# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Search(object):
    def setupUi(self, Search):
        Search.setObjectName("Search")
        Search.resize(611, 477)
        self.lineEdit = QtWidgets.QLineEdit(Search)
        self.lineEdit.setGeometry(QtCore.QRect(170, 59, 261, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_search = QtWidgets.QPushButton(Search)
        self.pushButton_search.setGeometry(QtCore.QRect(454, 62, 81, 31))
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_2 = QtWidgets.QPushButton(Search)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 440, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(Search)
        self.textBrowser.setGeometry(QtCore.QRect(25, 130, 221, 301))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Search)
        self.textBrowser_2.setGeometry(QtCore.QRect(360, 130, 231, 301))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.widget = QtWidgets.QWidget(Search)
        self.widget.setGeometry(QtCore.QRect(-20, -10, 641, 501))
        self.widget.setStyleSheet("background-image: url(\"C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/background.jpg\");")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(Search)
        self.label.setGeometry(QtCore.QRect(30, 60, 121, 31))
        self.label.setObjectName("label")
        self.widget.raise_()
        self.lineEdit.raise_()
        self.pushButton_search.raise_()
        self.pushButton_2.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        self.label.raise_()

        self.retranslateUi(Search)
        QtCore.QMetaObject.connectSlotsByName(Search)

    def retranslateUi(self, Search):
        _translate = QtCore.QCoreApplication.translate
        Search.setWindowTitle(_translate("Search", "Dialog"))
        self.pushButton_search.setText(_translate("Search", "SEARCH"))
        self.pushButton_2.setText(_translate("Search", "DONE"))
        self.label.setText(_translate("Search", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">COMMAND NAME:</span></p></body></html>"))

