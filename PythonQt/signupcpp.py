import signup
import sys
from signup import *
from PyQt5 import *
from PyQt5 import QtWidgets
'''
import "QMessageBox"
import "QFile"
import "QTextStream"
import "QDebug"
import "QStandardItem"
import "QListView"
import "QMimeData"
import "QClipboard"
import "QVector"
import "QString"
'''

#app = QtWidgets.QApplication(sys.argv)

class SignUp(QtWidgets.QDialog, Ui_SignUp) :
    def __init__(self, parent=None) :
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
    #start on_pushButton_clicked
    def on_pushButton_clicked(self) :
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        password2 = self.lineEdit_password2.text()
        if(password != password2) :
            QMessageBox.critical(this, "error", "Passwords don't Match")
        elif(password.isEmpty() or password2.isEmpty()) :
            QMessageBox.critical(this, "error", "Fields empty!")
        else :
            #Enter password and username in the list.
            file1 = open("C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/users.txt", a)
            file1.seek(file1.size())
            stream = QTextStream(file)
            stream << "," << username
            file1.flush()
            file1.close()
            file2 = open("C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/passwords.txt", w)
            file2.seek(file2.size())
            stream = QTextStream(file2)
            stream << "," << password
            file2.flush()
            file2.close()
            QMessageBox.information(0, "Complete", "Sign Up Completed!")
        self.hide()
    #start on_pushButton_2_clicked
    def on_pushButton_2_clicked(self) :
        self.hide()
        print ("hello")

#test = SignUp()
#test.show()
#app.exec_()
