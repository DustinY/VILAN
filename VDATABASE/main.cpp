#include "vilan.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    VILAN w;
    w.show();

    return a.exec();
}
