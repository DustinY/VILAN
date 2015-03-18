import vilan
from signupcpp import *
import sys
from vilan import *
from PyQt5 import *
from PyQt5 import QtWidgets
'''
from QString import *
from QDebug import *
from QMessageBox import *
from dialog.h import *
from QFile import *
from QTextStream import *
from QDebug import *
from QStandardItem import *
from QListView import *
from QVector import *
from QMainWindow import *
'''
'''from "mainmenu.h" import *
from "signup.h" import *
'''

#form_class = uic.loadUiType("vilan.ui")[0]
#class VILAN(QMainWindow, form_class):
#app = QtWidgets.QApplication(sys.argv)

class VILAN(QtWidgets.QMainWindow, Ui_VILAN):
    def __init__(self, parent=None) :
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
    #start on_pushButton_clicked
    def on_pushButton_clicked(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        #READ USERNAMES
        file1 = open("C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/users.txt",r)
        #QTextStream in(file1)
        in1 = QTextStream(file1)
        user = in2.readAll()
        file1.close()
        file2("C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/passwords.txt",r)
        in2 = QTextStream(file2)
        passwrd = in2.readAll()
        file2.close()
        #Testing
        fakeUser
        fakePassword
        userBreak = user.split(",")
        passBreak = passwrd.split(",")
        for x in xrange(0, userBreak.size()):
            if(userBreak.at(x)==username):
                fakeUser=userBreak.at(x)
        for x in xrange(0, passBreak.size()):
            if(passBreak.at(x)==password):
                fakePassword=passBreak.at(x)
        if(username.isEmpty() and password.isEmpty()):
            critical(self, "error", "No Username or Password Submitted")
        elif (username!=fakeUser and password!=fakePassword):
            #Display an Error
            critical(self, "error", "Login Unsuccessful ")
        elif(username==fakeUser and password==fakePassword):
            #Open Dialog window
            #mainMenu = new MainMenu()
            #mainMenu.show()
            self.hide()
        else:
            qDebug() << ""
    #end on_pushButton_clicked
    #start on_pushButton_2_clicked
    def on_pushButton_2_clicked(self) :
        #self.hide()
        signupRun = SignUp()
        signupRun.show()

    #end on_pushButton_2_clicked
'''run = VILAN()
run.show()
app.exec_()
'''
