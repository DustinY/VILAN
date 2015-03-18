import search
import sys
from search import *
from PyQt5 import *
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

class Search(QDialog, Ui_Search) :

    def __init__(self, parent=None) :
        QDialog.__init__(self, parent)
        self.setupUi(self);
        self.pushButton_search.clicked.connect(self.on_pushButton_search_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)

#start on_pushButton_search_clicked()
    def on_pushButton_search_clicked() :
{
    #Load the file
        file1 = open("C:/Users/Marvin/Desktop/CS437/Commander/Methods.txt", r)
        in1 = QTextStream(file)
        self.textBrowser.setText(in1.readAll())
        file.close();
    #Load list to a vector
        table = QVector<QString>()
        doc = QTextDocument (self.textBrowser.document())
        com = QString(doc.toPlainText())
        breakCom = QStringList(com.split("\n"))
    #Get command to search for
        match = QString(self.lineEdit.text())
        for i in xrange(0, breakCom.size()) :
           if(breakCom.at(i).contains(match) || breakCom.at(i).endsWith(match)):
               table.push_front(breakCom.at(i));
        for x in xrange (0, table.size()) :
            self.textBrowser_2.setText(table.at(x));

    def on_pushButton_2_clicked() :
        hide()
