#ifndef VILAN_H
#define VILAN_H

#include <QMainWindow>
#include "mainmenu.h"
#include "signup.h"

namespace Ui {
class VILAN;
}

class VILAN : public QMainWindow
{
    Q_OBJECT

public:
    explicit VILAN(QWidget *parent = 0);
    ~VILAN();

private slots:
    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

private:
    Ui::VILAN *ui;
    MainMenu *mainMenu;
    SignUp *mySignUp;

};

#endif // VILAN_H
