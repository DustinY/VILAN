#ifndef COMMANDS_H
#define COMMANDS_H

#include <QDialog>

namespace Ui {
class commands;
}

class commands : public QDialog
{
    Q_OBJECT

public:
    void displayList();
    explicit commands(QWidget *parent = 0);
    ~commands();

private slots:
    void on_pushButton_display_clicked();

    void on_pushButton_clicked();

private:
    Ui::commands *ui;
};

#endif // COMMANDS_H
