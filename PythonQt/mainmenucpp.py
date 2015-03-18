import mainmenu
import signupcpp
from signupcpp import *
import about
from about import *
import dialog
from dialog import *
import modify
from modify import *
import search
from search import *
import vilan
from vilan import *
import sys
from mainmenu import *
from PyQt5 import *
from PyQt5 import QtWidgets
'''
#include "mainmenu.h"
#include "ui_mainmenu.h"
#include "dialog.h"
#include "vilan.h"
#include "modify.h"
#include "search.h"
#include "display.h"
#include "about.h"
#include <QTime>
#include <QDate>
'''

class MainMenu(QtWidgets.QMainWindow, Ui_MainMenu):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton_add.clicked.connect(self.on_pushButton_add_clicked)
        self.pushButton_modify.clicked.connect(self.on_pushButton_modify_clicked)
        self.pushButton_search.clicked.connect(self.on_pushButton_search_clicked)
        self.pushButton_display.clicked.connect(self.on_pushButton_display_clicked)
        self.pushButton_about.clicked.connect(self.on_pushButton_about.clicked)
        self.label_date.setText(QDate.currentDate().toString("ddd MMMM d yyyy"))
    def on_pushButton_add_clicked(self):
        myDialog = Dialog()
        myDialog.show()
    def on_pushButton_Mmodify_clicked(self):
        myModify = Modify()
        myModify.show()
    def on_pushButton_6_clicked(self):
        QApplication.quit()
    def on_pushButton_search_clicked(self):
        mySearch = Search()
        mySearch.show()
    def on_pushButton_display_clicked(self):
        myDisplay = Display()
        myDisplay.show()
    def on_pushButton_about_clicked(self):
        myAbout = About()
        myAbout.show()
