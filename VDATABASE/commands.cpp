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
    QFile file("C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/Docs/commands.txt");
    if(!file.open(QIODevice::ReadOnly))
    QMessageBox::information(0, "info", file.errorString());
    QTextStream in(&file);
    ui->textBrowser->setText(in.readAll());
            file.close();
}
void commands::on_pushButton_display_clicked()
{
    displayList();
}

void commands::on_pushButton_clicked()
{
    hide();
}
