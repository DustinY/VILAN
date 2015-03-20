/********************************************************************************
** Form generated from reading UI file 'signup.ui'
**
** Created by: Qt User Interface Compiler version 5.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SIGNUP_H
#define UI_SIGNUP_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_SignUp
{
public:
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QLineEdit *lineEdit_username;
    QLineEdit *lineEdit_password;
    QLineEdit *lineEdit_password2;
    QPushButton *pushButton;
    QPushButton *pushButton_2;
    QWidget *widget;

    void setupUi(QDialog *SignUp)
    {
        if (SignUp->objectName().isEmpty())
            SignUp->setObjectName(QStringLiteral("SignUp"));
        SignUp->resize(389, 406);
        label = new QLabel(SignUp);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(40, 100, 91, 21));
        label_2 = new QLabel(SignUp);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(40, 150, 91, 21));
        label_3 = new QLabel(SignUp);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(50, 190, 81, 21));
        lineEdit_username = new QLineEdit(SignUp);
        lineEdit_username->setObjectName(QStringLiteral("lineEdit_username"));
        lineEdit_username->setGeometry(QRect(140, 100, 181, 20));
        lineEdit_password = new QLineEdit(SignUp);
        lineEdit_password->setObjectName(QStringLiteral("lineEdit_password"));
        lineEdit_password->setGeometry(QRect(140, 150, 181, 20));
        lineEdit_password->setEchoMode(QLineEdit::Password);
        lineEdit_password2 = new QLineEdit(SignUp);
        lineEdit_password2->setObjectName(QStringLiteral("lineEdit_password2"));
        lineEdit_password2->setGeometry(QRect(140, 190, 181, 20));
        lineEdit_password2->setEchoMode(QLineEdit::NoEcho);
        pushButton = new QPushButton(SignUp);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(110, 250, 75, 23));
        pushButton_2 = new QPushButton(SignUp);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        pushButton_2->setGeometry(QRect(210, 250, 75, 23));
        widget = new QWidget(SignUp);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setGeometry(QRect(0, 0, 391, 411));
        widget->setStyleSheet(QStringLiteral("background-image: url(\"C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/Docs/background.jpg\");"));
        widget->raise();
        label->raise();
        label_2->raise();
        label_3->raise();
        lineEdit_username->raise();
        lineEdit_password->raise();
        lineEdit_password2->raise();
        pushButton->raise();
        pushButton_2->raise();

        retranslateUi(SignUp);

        QMetaObject::connectSlotsByName(SignUp);
    } // setupUi

    void retranslateUi(QDialog *SignUp)
    {
        SignUp->setWindowTitle(QApplication::translate("SignUp", "Dialog", 0));
        label->setText(QApplication::translate("SignUp", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Username:</span></p></body></html>", 0));
        label_2->setText(QApplication::translate("SignUp", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Password:</span></p></body></html>", 0));
        label_3->setText(QApplication::translate("SignUp", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Re-Enter:</span></p></body></html>", 0));
        pushButton->setText(QApplication::translate("SignUp", "OK", 0));
        pushButton_2->setText(QApplication::translate("SignUp", "CANCEL", 0));
    } // retranslateUi

};

namespace Ui {
    class SignUp: public Ui_SignUp {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SIGNUP_H
