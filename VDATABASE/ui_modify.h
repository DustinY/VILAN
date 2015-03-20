/********************************************************************************
** Form generated from reading UI file 'modify.ui'
**
** Created by: Qt User Interface Compiler version 5.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MODIFY_H
#define UI_MODIFY_H

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

class Ui_Modify
{
public:
    QTextBrowser *textBrowser;
    QLabel *label;
    QPushButton *pushButton_save;
    QPushButton *pushButton;
    QPushButton *pushButton_2;
    QWidget *widget;

    void setupUi(QDialog *Modify)
    {
        if (Modify->objectName().isEmpty())
            Modify->setObjectName(QStringLiteral("Modify"));
        Modify->resize(526, 486);
        textBrowser = new QTextBrowser(Modify);
        textBrowser->setObjectName(QStringLiteral("textBrowser"));
        textBrowser->setGeometry(QRect(110, 40, 271, 391));
        textBrowser->setAutoFormatting(QTextEdit::AutoAll);
        textBrowser->setOverwriteMode(true);
        textBrowser->setTextInteractionFlags(Qt::LinksAccessibleByKeyboard|Qt::LinksAccessibleByMouse|Qt::TextBrowserInteraction|Qt::TextEditable|Qt::TextSelectableByMouse);
        label = new QLabel(Modify);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(110, 10, 281, 20));
        pushButton_save = new QPushButton(Modify);
        pushButton_save->setObjectName(QStringLiteral("pushButton_save"));
        pushButton_save->setGeometry(QRect(150, 440, 75, 23));
        pushButton = new QPushButton(Modify);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(410, 80, 75, 41));
        QIcon icon;
        icon.addFile(QStringLiteral("Docs/1425186456_330401.ico"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton->setIcon(icon);
        pushButton->setIconSize(QSize(40, 40));
        pushButton->setFlat(true);
        pushButton_2 = new QPushButton(Modify);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        pushButton_2->setGeometry(QRect(260, 440, 75, 23));
        widget = new QWidget(Modify);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setGeometry(QRect(0, 0, 531, 491));
        widget->setStyleSheet(QStringLiteral("background-image: url(\"C:/Users/Dustin/Documents/GitHub/VILAN/VDATABASE/Docs/background.jpg\");"));
        widget->raise();
        textBrowser->raise();
        label->raise();
        pushButton_save->raise();
        pushButton->raise();
        pushButton_2->raise();

        retranslateUi(Modify);

        QMetaObject::connectSlotsByName(Modify);
    } // setupUi

    void retranslateUi(QDialog *Modify)
    {
        Modify->setWindowTitle(QApplication::translate("Modify", "Dialog", 0));
        label->setText(QApplication::translate("Modify", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">LIST OF CUSTOM COMMANDS</span></p></body></html>", 0));
        pushButton_save->setText(QApplication::translate("Modify", "MODIFY", 0));
        pushButton->setText(QString());
        pushButton_2->setText(QApplication::translate("Modify", "DONE", 0));
    } // retranslateUi

};

namespace Ui {
    class Modify: public Ui_Modify {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MODIFY_H
