# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modify.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Modify(object):
    def setupUi(self, Modify):
        Modify.setObjectName("Modify")
        Modify.resize(526, 486)
        self.textBrowser = QtWidgets.QTextBrowser(Modify)
        self.textBrowser.setGeometry(QtCore.QRect(110, 30, 271, 401))
        self.textBrowser.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.textBrowser.setOverwriteMode(True)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextSelectableByMouse)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Modify)
        self.label.setGeometry(QtCore.QRect(110, 10, 271, 20))
        self.label.setObjectName("label")
        self.pushButton_save = QtWidgets.QPushButton(Modify)
        self.pushButton_save.setGeometry(QtCore.QRect(170, 440, 75, 23))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton = QtWidgets.QPushButton(Modify)
        self.pushButton.setGeometry(QtCore.QRect(410, 80, 75, 41))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Docs/1425186456_330401.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Modify)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 440, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(Modify)
        self.widget.setGeometry(QtCore.QRect(0, 0, 531, 491))
        self.widget.setStyleSheet("background-image: url(\"C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/background.jpg\");\n"
"")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.textBrowser.raise_()
        self.label.raise_()
        self.pushButton_save.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Modify)
        QtCore.QMetaObject.connectSlotsByName(Modify)

    def retranslateUi(self, Modify):
        _translate = QtCore.QCoreApplication.translate
        Modify.setWindowTitle(_translate("Modify", "Dialog"))
        self.label.setText(_translate("Modify", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">LIST OF CUSTOM COMMANDS</span></p></body></html>"))
        self.pushButton_save.setText(_translate("Modify", "MODIFY"))
        self.pushButton_2.setText(_translate("Modify", "DONE"))

