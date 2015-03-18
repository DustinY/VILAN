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


Dialog::Dialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Dialog)
{
    ui->setupUi(this);
    connect(ui->pushButton_5, SIGNAL(click()), this, SLOT(on_pushButton_5_clicked()));
}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::display()
{
    QFile file("C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/DOCS/customCommands.txt");
    if(!file.open(QIODevice::ReadOnly))
    QMessageBox::information(0, "info", file.errorString());
    QTextStream in(&file);
    ui->textBrowser->setText(in.readAll());
    file.close();
}

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
               QFile file("C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/DOCS/Methods.txt");
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
