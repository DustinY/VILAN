#ifndef MODIFY_H
#define MODIFY_H

#include <QDialog>

namespace Ui {
class Modify;
}

class Modify : public QDialog
{
    Q_OBJECT

public:
    void displayList();
    explicit Modify(QWidget *parent = 0);
    ~Modify();

private slots:
    void on_pushButton_save_clicked();

    void on_pushButton_2_clicked();

    void on_pushButton_clicked();

private:
    Ui::Modify *ui;
};

#endif // MODIFY_H
