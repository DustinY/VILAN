import modify
import sys
from modify import *
from PyQt5 import *
'''
#include "modify.h"
#include "ui_modify.h"
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

class Modify(QDialog, Ui_Modify):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        self.setupi(self)
        self.pushButton_save.clicked.connect(self.on_pushButton_save_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    def displayList() :
        file1 = open("C:/Users/Marvin/Desktop/CS437/Commander/Methods.txt", r);
        in1 = QTextStream(file1)
        self.textBrowser.setText(in1.readAll());
        file1.close();
#Start on_pushButton_save_clicked
    def on_pushButton_save_clicked() :
{
    #Get the text already in the textBrowser
        doc = QTextDocument(self.textBrowser.document())
        html = QString(doc.toPlainText())
    #Write the text again into the file.
        file2 = open("C:/Users/Marvin/Desktop/CS437/Commander/Methods.txt", w)
        stream = QTextStream(file2)
        stream << html << "\n"
        file2.flush()
        file2.close()

    def on_pushButton_2_clicked() :
        hide();

    def on_pushButton_clicked() :
        QMessageBox.information(0, "Information", "You can only modified Custom Commands");
