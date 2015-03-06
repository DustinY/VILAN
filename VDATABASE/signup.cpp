#include "signup.h"
#include "ui_signup.h"
#include<QMessageBox>
#include<QFile>
#include<QTextStream>
#include<QDebug>
#include<QStandardItem>
#include<QListView>
#include<QMimeData>
#include<QClipboard>
#include<QVector>
#include<QString>

SignUp::SignUp(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::SignUp)
{
    ui->setupUi(this);
}

SignUp::~SignUp()
{
    delete ui;
}

void SignUp::on_pushButton_clicked()
{
    QString username, password, password2;
    username = ui->lineEdit_username->text();
    password = ui->lineEdit_password->text();
    password2 = ui->lineEdit_password2->text();

    if(password!=password2){
        QMessageBox::critical(this, "error", "Passwords don't Match");
    } else if(password.isEmpty() || password2.isEmpty()) {
        QMessageBox::critical(this, "error", "Fields empty!");
    } else
    {
        //Enter password and username in the list.
        QFile file("C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/users.txt");
        if ( file.open(QFile::WriteOnly | QFile::Append ))
                {
                    file.seek(file.size());
                    QTextStream stream( &file );
                    stream<<","<<username;
                    file.flush();
                    file.close();
                }

        QFile file2("C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/passwords.txt");
        if ( file2.open(QFile::WriteOnly | QFile::Append ))
                {
                    file2.seek(file2.size());
                    QTextStream stream( &file2 );
                    stream<<","<<password;
                    file2.flush();
                    file2.close();
                }

        QMessageBox::information(0, "Complete", "Sign Up Completed!");

    }
    hide();
}

void SignUp::on_pushButton_2_clicked()
{
    hide();
}
