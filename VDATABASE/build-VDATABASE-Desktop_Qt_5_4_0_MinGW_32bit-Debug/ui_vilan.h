/********************************************************************************
** Form generated from reading UI file 'vilan.ui'
**
** Created by: Qt User Interface Compiler version 5.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_VILAN_H
#define UI_VILAN_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_VILAN
{
public:
    QWidget *centralWidget;
    QGroupBox *groupBox;
    QLabel *label;
    QLabel *label_2;
    QLineEdit *lineEdit_username;
    QLineEdit *lineEdit_password;
    QPushButton *pushButton;
    QPushButton *pushButton_2;
    QWidget *widget;

    void setupUi(QMainWindow *VILAN)
    {
        if (VILAN->objectName().isEmpty())
            VILAN->setObjectName(QStringLiteral("VILAN"));
        VILAN->resize(708, 469);
        centralWidget = new QWidget(VILAN);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        groupBox = new QGroupBox(centralWidget);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setGeometry(QRect(160, 110, 371, 191));
        QFont font;
        font.setFamily(QStringLiteral("Raavi"));
        font.setPointSize(12);
        font.setBold(false);
        font.setItalic(false);
        font.setWeight(9);
        groupBox->setFont(font);
        groupBox->setStyleSheet(QLatin1String("color: rgb(161, 161, 161);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Raavi\";\n"
""));
        label = new QLabel(groupBox);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(20, 60, 71, 16));
        label->setStyleSheet(QStringLiteral("color: rgb(165, 165, 165);"));
        label_2 = new QLabel(groupBox);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(20, 110, 81, 16));
        lineEdit_username = new QLineEdit(groupBox);
        lineEdit_username->setObjectName(QStringLiteral("lineEdit_username"));
        lineEdit_username->setGeometry(QRect(100, 60, 251, 20));
        lineEdit_username->setStyleSheet(QLatin1String("font: 75 11pt \"Myriad Web Pro Condensed\";\n"
"color: rgb(0, 0, 0);"));
        lineEdit_password = new QLineEdit(groupBox);
        lineEdit_password->setObjectName(QStringLiteral("lineEdit_password"));
        lineEdit_password->setGeometry(QRect(100, 110, 251, 20));
        lineEdit_password->setStyleSheet(QLatin1String("font: 75 11pt \"Myriad Web Pro Condensed\";\n"
"color: rgb(0, 0, 0);"));
        lineEdit_password->setInputMask(QStringLiteral(""));
        lineEdit_password->setEchoMode(QLineEdit::Password);
        pushButton = new QPushButton(groupBox);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(190, 150, 75, 23));
        pushButton->setStyleSheet(QLatin1String("color: rgb(152, 152, 152);\n"
"color: rgb(0, 0, 0);"));
        pushButton_2 = new QPushButton(groupBox);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        pushButton_2->setGeometry(QRect(270, 150, 75, 23));
        pushButton_2->setStyleSheet(QLatin1String("color: rgb(152, 152, 152);\n"
"color: rgb(0, 0, 0);"));
        widget = new QWidget(centralWidget);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setGeometry(QRect(0, 0, 791, 561));
        widget->setStyleSheet(QStringLiteral("background-image: url(\"C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/pic.jpg\");"));
        VILAN->setCentralWidget(centralWidget);
        widget->raise();
        groupBox->raise();

        retranslateUi(VILAN);

        QMetaObject::connectSlotsByName(VILAN);
    } // setupUi

    void retranslateUi(QMainWindow *VILAN)
    {
        VILAN->setWindowTitle(QApplication::translate("VILAN", "VILAN", 0));
        groupBox->setTitle(QApplication::translate("VILAN", "Welcome", 0));
        label->setText(QApplication::translate("VILAN", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">USERNAME</span></p></body></html>", 0));
        label_2->setText(QApplication::translate("VILAN", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">PASSWORD</span></p></body></html>", 0));
        lineEdit_username->setText(QString());
        lineEdit_password->setText(QString());
        pushButton->setText(QApplication::translate("VILAN", "Login", 0));
        pushButton_2->setText(QApplication::translate("VILAN", "Sign Up", 0));
    } // retranslateUi

};

namespace Ui {
    class VILAN: public Ui_VILAN {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_VILAN_H
