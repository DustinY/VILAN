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
#include<stdlib.h>

Modify::Modify(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Modify)
{
    ui->setupUi(this);
    displayList();
}

Modify::~Modify()
{
    delete ui;

}


void Modify::displayList()
{
    QFile file("C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/DOCS/customCommands.dat");
      if(!file.open(QIODevice::ReadOnly))
      QMessageBox::information(0, "info", file.errorString());
      QTextStream in(&file);
      ui->textBrowser->setText(in.readAll());
      file.close();
}

void Modify::on_pushButton_save_clicked()
{    
    //Get the text already in the textBrowser
    QTextDocument *doc = ui->textBrowser->document();
    QString html = doc->toPlainText();


    //Write the text again into the file.
    QFile file("C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/DOCS/customCommands.dat");
    if ( file.open(QFile::WriteOnly | QFile::Text ))
            {
        QTextStream stream( &file );
        stream<<html<<endl;
        file.flush();
        file.close();
    }
    system("taskkill /f /im pythonw.exe");
    system("C:/Python27/pythonw C:/Users/Dustin/Documents/GitHub/VILAN/VilanDragonfly.pyw");
}


void Modify::on_pushButton_2_clicked()
{
    hide();
}

void Modify::on_pushButton_clicked()
{
    QMessageBox::information(0, "Information", "You can only modified Custom Commands");
}
