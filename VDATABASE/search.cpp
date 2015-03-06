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

Search::Search(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Search)
{
    ui->setupUi(this);
}

Search::~Search()
{
    delete ui;
}



void Search::on_pushButton_search_clicked()
{
    //Load the file
    QFile file("C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/Methods.txt");
       if(!file.open(QIODevice::ReadOnly))
       QMessageBox::information(0, "info", file.errorString());
       QTextStream in(&file);
       ui->textBrowser->setText(in.readAll());
       file.close();

       //Load list to a vector
       QVector<QString> table;

       QTextDocument *doc = ui->textBrowser->document();
       QString com = doc->toPlainText();
       QStringList breakCom = com.split("\n");


       //Get command to search for
       QString match;
       match = ui->lineEdit->text();

     for(int i=0; i<breakCom.size(); i++)
     {
         if(breakCom.at(i).contains(match) || breakCom.at(i).endsWith(match)){

             table.push_front(breakCom.at(i));
         }
     }
    //Check the Vector
    for(int i=0; i<table.size(); i++)
    {
            ui->textBrowser_2->setText(table.at(i));
    }

}

void Search::on_pushButton_2_clicked()
{
    hide();
}
