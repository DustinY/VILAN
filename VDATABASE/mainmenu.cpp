#include "mainmenu.h"
#include "ui_mainmenu.h"
#include "dialog.h"
#include "vilan.h"
#include "modify.h"
#include "search.h"
#include "display.h"
#include "about.h"
#include <QTime>
#include <QDate>
MainMenu::MainMenu(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainMenu)
{
    ui->setupUi(this);
     connect(ui->pushButton_add, SIGNAL(click()), this, SLOT(on_pushButton_add_clicked()));
     connect(ui->pushButton_modify, SIGNAL(click()), this, SLOT(on_pushButton_modify_clicked()));
     connect(ui->pushButton_search, SIGNAL(click()), this, SLOT(on_pushButton_search_clicked()));
     connect(ui->pushButton_display, SIGNAL(click()), this, SLOT(on_pushButton_display_clicked()));
     connect(ui->pushButton_about, SIGNAL(click()), this, SLOT(on_pushButton_about_clicked()));
     connect(ui->pushButton_commands, SIGNAL(click()), this, SLOT(on_pushButton_commands_clicked()));
     ui->label_date->setText(QDate::currentDate().toString("ddd MMMM d yyyy"));
}

MainMenu::~MainMenu()
{
    delete ui;
}


void MainMenu::on_pushButton_add_clicked()
{
    myDialog = new Dialog();
    myDialog->show();
}


void MainMenu::on_pushButton_modify_clicked()
{
    myModify = new Modify();
    myModify->show();
}

void MainMenu::on_pushButton_6_clicked()
{
    QApplication::quit();
}

void MainMenu::on_pushButton_search_clicked()
{
    mySearch = new Search();
    mySearch->show();
}

void MainMenu::on_pushButton_display_clicked()
{
    myDisplay = new Display();
    myDisplay->show();
}
void MainMenu::on_pushButton_about_clicked()
{
   myAbout = new About();
   myAbout->show();
}


void MainMenu::on_pushButton_commands_clicked()
{
    myCommands = new commands();
    myCommands->show();
}
