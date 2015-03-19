#include "commands.h"
#include "ui_commands.h"
#include<QDebug>
#include<QStandardItem>
#include<QListView>
#include<QMimeData>
#include<QClipboard>
#include<QVector>
#include<QMessageBox>
#include<QFile>

commands::commands(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::commands)
{
    ui->setupUi(this);
}

commands::~commands()
{
    delete ui;
}

void commands::displayList()
{
    QFile file("C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/Docs/commandList.txt");
    if(!file.open(QIODevice::ReadOnly))
        QMessageBox::information(0, "info", file.errorString());
    QFile file2("c:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/Docs/customCommands.dat");
    if(!file2.open(QIODevice::ReadOnly))
        QMessageBox::information(0, "info", file2.errorString());
    QTextStream in(&file);
    QTextStream in2(&file2);
    QString allIn = in.readAll() + in2.readAll();
    //ui->textBrowser->setText(in.readAll());
    ui->textBrowser->setText(allIn);
    file.close();
    file2.close();
}
void commands::on_pushButton_display_clicked()
{
    displayList();
}

void commands::on_pushButton_clicked()
{
    hide();
}
