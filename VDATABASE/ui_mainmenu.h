/********************************************************************************
** Form generated from reading UI file 'mainmenu.ui'
**
** Created by: Qt User Interface Compiler version 5.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINMENU_H
#define UI_MAINMENU_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainMenu
{
public:
    QWidget *centralwidget;
    QPushButton *pushButton_add;
    QPushButton *pushButton_modify;
    QPushButton *pushButton_search;
    QPushButton *pushButton_display;
    QPushButton *pushButton_about;
    QPushButton *pushButton_6;
    QLabel *label_date;
    QPushButton *pushButton_commands;
    QPushButton *pushButton;
    QWidget *widget;

    void setupUi(QMainWindow *MainMenu)
    {
        if (MainMenu->objectName().isEmpty())
            MainMenu->setObjectName(QStringLiteral("MainMenu"));
        MainMenu->resize(679, 569);
        centralwidget = new QWidget(MainMenu);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        pushButton_add = new QPushButton(centralwidget);
        pushButton_add->setObjectName(QStringLiteral("pushButton_add"));
        pushButton_add->setGeometry(QRect(340, 10, 251, 69));
        QFont font;
        font.setPointSize(16);
        font.setBold(true);
        font.setWeight(75);
        pushButton_add->setFont(font);
        pushButton_add->setStyleSheet(QLatin1String("text-align: left;\n"
"color: rgb(33, 152, 175);\n"
""));
        QIcon icon;
        icon.addFile(QStringLiteral("Docs/ico.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_add->setIcon(icon);
        pushButton_add->setIconSize(QSize(70, 70));
        pushButton_add->setCheckable(false);
        pushButton_add->setFlat(true);
        pushButton_modify = new QPushButton(centralwidget);
        pushButton_modify->setObjectName(QStringLiteral("pushButton_modify"));
        pushButton_modify->setGeometry(QRect(340, 90, 251, 69));
        pushButton_modify->setFont(font);
        pushButton_modify->setStyleSheet(QLatin1String("text-align: left;\n"
"color: rgb(33, 152, 175);"));
        pushButton_modify->setIcon(icon);
        pushButton_modify->setIconSize(QSize(70, 70));
        pushButton_modify->setFlat(true);
        pushButton_search = new QPushButton(centralwidget);
        pushButton_search->setObjectName(QStringLiteral("pushButton_search"));
        pushButton_search->setGeometry(QRect(340, 170, 251, 69));
        pushButton_search->setFont(font);
        pushButton_search->setStyleSheet(QLatin1String("text-align: left;\n"
"color: rgb(33, 152, 175);"));
        pushButton_search->setIcon(icon);
        pushButton_search->setIconSize(QSize(70, 70));
        pushButton_search->setFlat(true);
        pushButton_display = new QPushButton(centralwidget);
        pushButton_display->setObjectName(QStringLiteral("pushButton_display"));
        pushButton_display->setGeometry(QRect(340, 330, 251, 69));
        pushButton_display->setFont(font);
        pushButton_display->setStyleSheet(QLatin1String("text-align: left;\n"
"color: rgb(33, 152, 175);"));
        pushButton_display->setIcon(icon);
        pushButton_display->setIconSize(QSize(70, 70));
        pushButton_display->setFlat(true);
        pushButton_about = new QPushButton(centralwidget);
        pushButton_about->setObjectName(QStringLiteral("pushButton_about"));
        pushButton_about->setGeometry(QRect(340, 400, 251, 69));
        pushButton_about->setFont(font);
        pushButton_about->setStyleSheet(QLatin1String("text-align: left;\n"
"color: rgb(33, 152, 175);"));
        pushButton_about->setIcon(icon);
        pushButton_about->setIconSize(QSize(70, 70));
        pushButton_about->setFlat(true);
        pushButton_6 = new QPushButton(centralwidget);
        pushButton_6->setObjectName(QStringLiteral("pushButton_6"));
        pushButton_6->setGeometry(QRect(340, 480, 251, 69));
        pushButton_6->setFont(font);
        pushButton_6->setStyleSheet(QLatin1String("text-align: left;\n"
"color: rgb(33, 152, 175);"));
        pushButton_6->setIcon(icon);
        pushButton_6->setIconSize(QSize(70, 70));
        pushButton_6->setFlat(true);
        label_date = new QLabel(centralwidget);
        label_date->setObjectName(QStringLiteral("label_date"));
        label_date->setGeometry(QRect(20, 20, 291, 41));
        QFont font1;
        font1.setPointSize(14);
        font1.setBold(true);
        font1.setWeight(75);
        label_date->setFont(font1);
        label_date->setStyleSheet(QStringLiteral("color: rgb(1, 170, 216);"));
        pushButton_commands = new QPushButton(centralwidget);
        pushButton_commands->setObjectName(QStringLiteral("pushButton_commands"));
        pushButton_commands->setGeometry(QRect(340, 250, 251, 69));
        pushButton_commands->setFont(font);
        pushButton_commands->setAutoFillBackground(false);
        pushButton_commands->setStyleSheet(QLatin1String("text-align: left;\n"
"color: rgb(33, 152, 175);"));
        pushButton_commands->setIcon(icon);
        pushButton_commands->setIconSize(QSize(70, 70));
        pushButton_commands->setFlat(true);
        pushButton = new QPushButton(centralwidget);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(20, 430, 131, 111));
        QIcon icon1;
        icon1.addFile(QStringLiteral("Docs/started.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton->setIcon(icon1);
        pushButton->setIconSize(QSize(80, 80));
        pushButton->setFlat(true);
        widget = new QWidget(centralwidget);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setGeometry(QRect(0, 0, 701, 591));
        widget->setAutoFillBackground(false);
        widget->setStyleSheet(QStringLiteral("background-image: url(\"C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/Docs/background.jpg\");"));
        pushButton_display->raise();
        MainMenu->setCentralWidget(centralwidget);
        widget->raise();
        pushButton_add->raise();
        pushButton_modify->raise();
        pushButton_search->raise();
        pushButton_display->raise();
        pushButton_about->raise();
        pushButton_6->raise();
        label_date->raise();
        pushButton_commands->raise();
        pushButton->raise();

        retranslateUi(MainMenu);

        QMetaObject::connectSlotsByName(MainMenu);
    } // setupUi

    void retranslateUi(QMainWindow *MainMenu)
    {
        MainMenu->setWindowTitle(QApplication::translate("MainMenu", "MainWindow", 0));
        pushButton_add->setText(QApplication::translate("MainMenu", "ADD", 0));
        pushButton_modify->setText(QApplication::translate("MainMenu", "MODIFY", 0));
        pushButton_search->setText(QApplication::translate("MainMenu", "SEARCH", 0));
        pushButton_display->setText(QApplication::translate("MainMenu", "DISPLAY", 0));
        pushButton_about->setText(QApplication::translate("MainMenu", "ABOUT", 0));
        pushButton_6->setText(QApplication::translate("MainMenu", "EXIT", 0));
        label_date->setText(QApplication::translate("MainMenu", "<html><head/><body><p>Date Label</p><p><br/></p></body></html>", 0));
        pushButton_commands->setText(QApplication::translate("MainMenu", "COMMANDS", 0));
        pushButton->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class MainMenu: public Ui_MainMenu {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINMENU_H
