#include "vilan.h"
#include "ui_vilan.h"
#include <QString>
#include <QDebug>
#include <QMessageBox>
#include "dialog.h"
#include<QFile>
#include<QTextStream>
#include<QDebug>
#include<QStandardItem>
#include<QListView>
#include<QVector>

VILAN::VILAN(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::VILAN)
{
    ui->setupUi(this);
    connect(ui->pushButton, SIGNAL(click()), this, SLOT(on_pushButton_clicked()));
    connect(ui->pushButton_2, SIGNAL(click()), this, SLOT(on_pushButton_2_clicked()));
}

VILAN::~VILAN()
{
    delete ui;
}

void VILAN::on_pushButton_clicked()
{
    QString username, password;
    username = ui->lineEdit_username->text();
    password = ui->lineEdit_password->text();

    QString user, pass;

    //READ USERNAMES
    QFile file("C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/DOCS/users.txt");
     if(!file.open(QIODevice::ReadOnly))
     QMessageBox::information(0, "info", file.errorString());
     QTextStream in(&file);
     user = in.readAll();
     file.close();

     QFile file2("C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/DOCS/passwords.txt");
      if(!file2.open(QIODevice::ReadOnly))
      QMessageBox::information(0, "info", file2.errorString());
      QTextStream in2(&file2);
      pass = in2.readAll();
      file2.close();

      //Testing
    QString fakeUser, fakePassword;

    QStringList userBreak = user.split(",");
    QStringList passBreak = pass.split(",");


    for(int x=0; x<userBreak.size(); x++)
    {
        if(userBreak.at(x)==username)
        {
            fakeUser=userBreak.at(x);
        }
    }

    for(int x=0; x<passBreak.size(); x++)
    {
        if(passBreak.at(x)==password)
        {
            fakePassword=passBreak.at(x);
        }
    }


    if(username.isEmpty() && password.isEmpty())
    {
        QMessageBox::critical(this, "error", "No Username or Password Submitted");

     } else if (username!=fakeUser && password!=fakePassword) {
        //Display an Error
        QMessageBox::critical(this, "error", "Login Unsuccessful ");
    }
    else if(username==fakeUser && password==fakePassword)
    {
        //Open Dialog window
        mainMenu = new MainMenu();
        mainMenu->show();
        hide();
    } else
    {
        qDebug() <<"";
    }
}

void VILAN::on_pushButton_2_clicked()
{
    mySignUp = new SignUp();
    mySignUp->show();
}
