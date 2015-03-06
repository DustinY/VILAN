/********************************************************************************
** Form generated from reading UI file 'search.ui'
**
** Created by: Qt User Interface Compiler version 5.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SEARCH_H
#define UI_SEARCH_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Search
{
public:
    QLineEdit *lineEdit;
    QPushButton *pushButton_search;
    QPushButton *pushButton_2;
    QTextBrowser *textBrowser;
    QTextBrowser *textBrowser_2;
    QWidget *widget;
    QLabel *label;

    void setupUi(QDialog *Search)
    {
        if (Search->objectName().isEmpty())
            Search->setObjectName(QStringLiteral("Search"));
        Search->resize(611, 477);
        lineEdit = new QLineEdit(Search);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));
        lineEdit->setGeometry(QRect(170, 59, 261, 31));
        pushButton_search = new QPushButton(Search);
        pushButton_search->setObjectName(QStringLiteral("pushButton_search"));
        pushButton_search->setGeometry(QRect(454, 62, 81, 31));
        pushButton_2 = new QPushButton(Search);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        pushButton_2->setGeometry(QRect(260, 440, 75, 23));
        textBrowser = new QTextBrowser(Search);
        textBrowser->setObjectName(QStringLiteral("textBrowser"));
        textBrowser->setGeometry(QRect(25, 130, 221, 301));
        textBrowser_2 = new QTextBrowser(Search);
        textBrowser_2->setObjectName(QStringLiteral("textBrowser_2"));
        textBrowser_2->setGeometry(QRect(360, 130, 231, 301));
        widget = new QWidget(Search);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setGeometry(QRect(-20, -10, 641, 501));
        widget->setStyleSheet(QStringLiteral("background-image: url(\"C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/background.jpg\");"));
        label = new QLabel(Search);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(30, 60, 121, 31));
        widget->raise();
        lineEdit->raise();
        pushButton_search->raise();
        pushButton_2->raise();
        textBrowser->raise();
        textBrowser_2->raise();
        label->raise();

        retranslateUi(Search);

        QMetaObject::connectSlotsByName(Search);
    } // setupUi

    void retranslateUi(QDialog *Search)
    {
        Search->setWindowTitle(QApplication::translate("Search", "Dialog", 0));
        pushButton_search->setText(QApplication::translate("Search", "SEARCH", 0));
        pushButton_2->setText(QApplication::translate("Search", "DONE", 0));
        label->setText(QApplication::translate("Search", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">COMMAND NAME:</span></p></body></html>", 0));
    } // retranslateUi

};

namespace Ui {
    class Search: public Ui_Search {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SEARCH_H
