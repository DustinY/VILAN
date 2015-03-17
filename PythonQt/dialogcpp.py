import dialog
import sys
from dialog import *
from PyQt5 import *
from PyQt5 import QtWidgets
'''
#include "ui_dialog.h"
#include "vilan.h"
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

class Dialog(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton_5.clicked.connect(self.on_pushButton_5_clicked)
    def display(self):
        file1 = open("C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/Methods.txt", r)
        in1 = QTextStream(file1)
        self.textBrowser.setText(in1.readAll())
        file1.close()
    def on_pushButton_clicked(self):
        voice = QString(self.lineEdit_voice.text())
        command = QString(self.lineEdit_command.text())
        if(voice.isEmpty() and command.isEmpty()):
            QMessageBox.critical(self, "error", "Fields Empty!!")
        elif(voice.isEmpty()):
            QMessageBox.critical(self, "error", "Voice Field Empty!")
        elif(command.isEmpty()):
            QMessageBox.critical(self, "error", "Command Field Empty!")
        else:
            reply = QMessageBox.


void Dialog::on_pushButton_clicked()
{
    QString voice = ui->lineEdit_voice->text();
    QString command = ui->lineEdit_command->text();

    if(voice.isEmpty() && command.isEmpty())
        {
            QMessageBox::critical(this, "error", "Fields Empty!!");
        } else if(voice.isEmpty())
        {
              QMessageBox::critical(this, "error", "Voice Field Empty");
        } else if (command.isEmpty())
        {
              QMessageBox::critical(this, "error", "Command Name empty");
        }
        else {
            QMessageBox::StandardButton reply;
             reply = QMessageBox::question(this, "Test", "Would you like this new Command?", QMessageBox::Yes|QMessageBox::No);

             if (reply == QMessageBox::Yes) {
               qDebug() << "Command Added";
               QFile file("C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/users.txt");
               if ( file.open(QFile::WriteOnly | QFile::Append ))
                       {
                           file.seek(file.size());
                           QTextStream stream( &file );
                           stream<<"\n"<<voice<<","<<command<<"\r"<<endl;
                           file.flush();
                           file.close();
                       }
               //If a new command was addded, reload list.
                display();
             } else {
               qDebug() << "Comment Canceled!";
             }
    }


}

void Dialog::on_pushButton_5_clicked()
{
    //Exit the program.
 hide();

}

void Dialog::on_pushButton_2_clicked()
{
    display();
}
