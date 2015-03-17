import search
import sys
from search import *
from PyQt5 import *
from PyQt5 import QtWidgets

'''
#include "search.h"
#include "ui_search.h"
#include "mainmenu.h"
#include<QMessageBox>
#include<QFile>
#include<QTextStream>
#include<QDebug>
#include<QStandardItem>
#include<QListView>
#include<QMimeData>
#include<QClipboard>
#include<QVector>
'''


class Search(QtWidgets.QDialog, Ui_Search):
    def __init__(self, parent=None) :
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.pushButton_search_clicked.clicked.connect(self.on_pushButton_search_clicked)
        self.pushButton_2_clicked.clicked.connect(self.on_pushButton_2_clicked)
    #Start on_pushButton_search_clicked
    def on_pushButton_search_clicked(self):
        file1 = open("C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/Methods.txt", r)
        in1 = QTextStream(file1)
        self.textBrowser.setText(in1.readAll())
        file1.close()

        #Load List to a vector
        table = QVector<QString>()
        doc = QTextDocument(self.textBrowser.document())
        com = QStrick(doc.toPlainText())
        breakCom = QStringList(com.split("\n"))

        #Get Command to search for
        match = QString(self.lineEdit.text())

        for i in xrange(0, breakCom.size()):
            if(breakCom.at(i).contains(match) or breakCom.at(i).endsWith(match)):
                table.push_front(breakCom.at(i))
        for i in xrange(0, table.size()):
            self.textBrowser_2.setText(table.at(i))
    def on_pushButton_2_clicked(self):
        self.hide()
