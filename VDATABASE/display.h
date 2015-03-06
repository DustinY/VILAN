#ifndef DISPLAY_H
#define DISPLAY_H

#include <QDialog>

namespace Ui {
class Display;
}

class Display : public QDialog
{
    Q_OBJECT

public:
    void displayList();
    void displayList2();
    explicit Display(QWidget *parent = 0);
    ~Display();

private slots:
    void on_pushButton_clicked();

private:
    Ui::Display *ui;
};

#endif // DISPLAY_H
