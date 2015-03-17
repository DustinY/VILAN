import display
import sys
from display import *
from PyQt5 import *
from PyQt5 import QtWidgets
'''
#include "display.h"
#include "ui_display.h"
#include<QDebug>
#include<QStandardItem>
#include<QListView>
#include<QMimeData>
#include<QClipboard>
#include<QVector>
#include<QMessageBox>
#include<QFile>
'''

class Display(QtWidgets.QMainWindow, Ui_Display):
    def __init__(self, parent=None):
        self.setupUi(self)
    #Display the list of commands
    def displayList(self):
        file1 = open("C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/Methods.txt", r)
        in1 = QTextStream(file1)
        self.textBrowser.setText(in1.readAll())
        file1.close()
    #Display the custom list of commands
    def displayList2(self):
        file2 = open("C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/Methods.txt", r)
        in2 = QTextStream(file2)
        self.textBrowser_2.setText(in2.readAll())
        file2.close()
    def on_pushButton_clicked(self):
        displayList()
        displayList2()
