/********************************************************************************
** Form generated from reading UI file 'about.ui'
**
** Created by: Qt User Interface Compiler version 5.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ABOUT_H
#define UI_ABOUT_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_About
{
public:
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QLabel *label_4;
    QLabel *label_5;
    QLabel *label_6;
    QWidget *widget;

    void setupUi(QDialog *About)
    {
        if (About->objectName().isEmpty())
            About->setObjectName(QStringLiteral("About"));
        About->resize(567, 478);
        label = new QLabel(About);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(160, 70, 261, 51));
        QFont font;
        font.setPointSize(36);
        font.setBold(true);
        font.setWeight(75);
        label->setFont(font);
        label_2 = new QLabel(About);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(320, 290, 161, 31));
        label_3 = new QLabel(About);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(320, 320, 141, 31));
        label_4 = new QLabel(About);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(320, 380, 121, 31));
        label_5 = new QLabel(About);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setGeometry(QRect(320, 350, 121, 31));
        label_6 = new QLabel(About);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setGeometry(QRect(190, 450, 251, 20));
        widget = new QWidget(About);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setGeometry(QRect(0, 0, 571, 491));
        widget->setStyleSheet(QStringLiteral("background-image: url(\"C:/Users/Dustin/Documents/School/CSULA/CS 437/VDATABASE/Docs/background.jpg\");"));
        widget->raise();
        label->raise();
        label_2->raise();
        label_3->raise();
        label_4->raise();
        label_5->raise();
        label_6->raise();

        retranslateUi(About);

        QMetaObject::connectSlotsByName(About);
    } // setupUi

    void retranslateUi(QDialog *About)
    {
        About->setWindowTitle(QApplication::translate("About", "Dialog", 0));
        label->setText(QApplication::translate("About", "<html><head/><body><p><span style=\" color:#ffffff;\">V.I.L.A.N</span></p></body></html>", 0));
        label_2->setText(QApplication::translate("About", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Marvin Itzep</span></p></body></html>", 0));
        label_3->setText(QApplication::translate("About", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Dustin York</span></p></body></html>", 0));
        label_4->setText(QApplication::translate("About", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Daanyaal Syed</span></p></body></html>", 0));
        label_5->setText(QApplication::translate("About", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Vicken Krikorian</span></p></body></html>", 0));
        label_6->setText(QApplication::translate("About", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">CSULA-Winter 20015-CS437</span></p></body></html>", 0));
    } // retranslateUi

};

namespace Ui {
    class About: public Ui_About {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ABOUT_H
