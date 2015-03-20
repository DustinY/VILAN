/********************************************************************************
** Form generated from reading UI file 'display.ui'
**
** Created by: Qt User Interface Compiler version 5.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DISPLAY_H
#define UI_DISPLAY_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Display
{
public:
    QPushButton *pushButton;
    QTextBrowser *textBrowser;
    QTextBrowser *textBrowser_2;
    QLabel *label;
    QLabel *label_2;
    QWidget *widget;

    void setupUi(QDialog *Display)
    {
        if (Display->objectName().isEmpty())
            Display->setObjectName(QStringLiteral("Display"));
        Display->resize(592, 481);
        pushButton = new QPushButton(Display);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(230, 420, 111, 31));
        textBrowser = new QTextBrowser(Display);
        textBrowser->setObjectName(QStringLiteral("textBrowser"));
        textBrowser->setGeometry(QRect(30, 50, 241, 351));
        textBrowser->setAutoFormatting(QTextEdit::AutoBulletList);
        textBrowser_2 = new QTextBrowser(Display);
        textBrowser_2->setObjectName(QStringLiteral("textBrowser_2"));
        textBrowser_2->setGeometry(QRect(320, 50, 241, 351));
        label = new QLabel(Display);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(90, 15, 121, 21));
        QFont font;
        font.setPointSize(12);
        font.setBold(true);
        font.setWeight(75);
        label->setFont(font);
        label_2 = new QLabel(Display);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(390, 15, 121, 21));
        label_2->setFont(font);
        widget = new QWidget(Display);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setGeometry(QRect(0, 0, 591, 481));
        widget->setStyleSheet(QStringLiteral("background-image: url(\"C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/Docs/background.jpg\");"));
        widget->raise();
        pushButton->raise();
        textBrowser->raise();
        textBrowser_2->raise();
        label->raise();
        label_2->raise();

        retranslateUi(Display);

        QMetaObject::connectSlotsByName(Display);
    } // setupUi

    void retranslateUi(QDialog *Display)
    {
        Display->setWindowTitle(QApplication::translate("Display", "Dialog", 0));
        pushButton->setText(QApplication::translate("Display", "LOAD COMMANDS", 0));
        label->setText(QApplication::translate("Display", "<html><head/><body><p><span style=\" color:#9e9e9e;\">Default List</span></p></body></html>", 0));
        label_2->setText(QApplication::translate("Display", "<html><head/><body><p><span style=\" color:#ababab;\">Custom List</span></p></body></html>", 0));
    } // retranslateUi

};

namespace Ui {
    class Display: public Ui_Display {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DISPLAY_H
