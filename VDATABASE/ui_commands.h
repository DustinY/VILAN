/********************************************************************************
** Form generated from reading UI file 'commands.ui'
**
** Created by: Qt User Interface Compiler version 5.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_COMMANDS_H
#define UI_COMMANDS_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_commands
{
public:
    QTextBrowser *textBrowser;
    QPushButton *pushButton;
    QPushButton *pushButton_display;
    QWidget *widget;

    void setupUi(QDialog *commands)
    {
        if (commands->objectName().isEmpty())
            commands->setObjectName(QStringLiteral("commands"));
        commands->resize(593, 566);
        textBrowser = new QTextBrowser(commands);
        textBrowser->setObjectName(QStringLiteral("textBrowser"));
        textBrowser->setGeometry(QRect(70, 20, 461, 481));
        pushButton = new QPushButton(commands);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(320, 520, 75, 23));
        pushButton_display = new QPushButton(commands);
        pushButton_display->setObjectName(QStringLiteral("pushButton_display"));
        pushButton_display->setGeometry(QRect(210, 520, 75, 23));
        widget = new QWidget(commands);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setGeometry(QRect(0, 0, 601, 581));
        widget->setStyleSheet(QStringLiteral("background-image: url(\"C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/Docs/background.jpg\");"));
        widget->raise();
        textBrowser->raise();
        pushButton->raise();
        pushButton_display->raise();

        retranslateUi(commands);

        QMetaObject::connectSlotsByName(commands);
    } // setupUi

    void retranslateUi(QDialog *commands)
    {
        commands->setWindowTitle(QApplication::translate("commands", "Dialog", 0));
        pushButton->setText(QApplication::translate("commands", "OK", 0));
        pushButton_display->setText(QApplication::translate("commands", "Display", 0));
    } // retranslateUi

};

namespace Ui {
    class commands: public Ui_commands {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_COMMANDS_H
