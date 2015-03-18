#ifndef MAINMENU_H
#define MAINMENU_H

#include <QMainWindow>
#include "dialog.h"
#include "modify.h"
#include "search.h"
#include "display.h"
#include "about.h"
#include "commands.h"

namespace Ui {
class MainMenu;
}

class MainMenu : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainMenu(QWidget *parent = 0);
    ~MainMenu();

private slots:
    //Add function
    void on_pushButton_add_clicked();
    //Exit function
    void on_pushButton_6_clicked();
    //Modify function
    void on_pushButton_modify_clicked();

    void on_pushButton_search_clicked();

    void on_pushButton_display_clicked();

    void on_pushButton_about_clicked();

    void on_pushButton_commands_clicked();

private:
    Ui::MainMenu *ui;
    Modify *myModify;
    Dialog *myDialog;
    Search *mySearch;
    Display *myDisplay;
    About *myAbout;
    commands *myCommands;
};

#endif // MAINMENU_H
