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
    QFile file("C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/DOCS/commandList.txt");
    if(!file.open(QIODevice::ReadOnly))
        QMessageBox::information(0, "info", file.errorString());
    QFile file2("C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/DOCS/customCommands.dat");
    if(!file2.open(QIODevice::ReadOnly))
        QMessageBox::information(0, "info", file2.errorString());
    QTextStream in(&file);
    QTextStream in2(&file2);
    QString allText = in.readAll() + in2.readAll();
    ui->textBrowser->setText(allText);
    file.close();
    file2.close();

       //Load list to a vector
       QVector<QString> table;
       QStringList breakCom = allText.split("\n");
       //Get command to search for
       QString match;
       match = ui->lineEdit->text();

     for(int i=0; i<breakCom.size(); i++)
     {
         if(breakCom.at(i).contains(match) || breakCom.at(i).endsWith(match)){

             table.push_front(breakCom.at(i));
         }
     }
    QString foundCommands = "";
    for(int x=0; x<table.size(); x++){
        foundCommands += table.at(x) + "\n";
     }

    ui->textBrowser_2->setText(foundCommands);
}

void Search::on_pushButton_2_clicked()
{
    hide();
}
