#include "display.h"
#include "ui_display.h"
#include<QDebug>
#include<QStandardItem>
#include<QListView>
#include<QMimeData>
#include<QClipboard>
#include<QVector>
#include<QMessageBox>
#include<QFile>


Display::Display(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Display)
{
    ui->setupUi(this);
    displayList();
    displayList2();
}

Display::~Display()
{
    delete ui;
}
//Display the default list of commands
void Display::displayList()
{
    QFile file("C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/DOCS/commandList.txt");
    if(!file.open(QIODevice::ReadOnly))
    QMessageBox::information(0, "info", file.errorString());
    QTextStream in(&file);
    ui->textBrowser->setText(in.readAll());
    file.close();
}

//Display the custom list of commands
void Display::displayList2()
{
    QFile file("C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/DOCS/customCommands.dat");
    if(!file.open(QIODevice::ReadOnly))
    QMessageBox::information(0, "info", file.errorString());
    QTextStream in(&file);
    ui->textBrowser_2->setText(in.readAll());
    file.close();
}

void Display::on_pushButton_clicked()
{
  displayList();
  displayList2();
}
