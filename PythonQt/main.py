import vilancpp
from vilancpp import *
import sys
from PyQt5 import *
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
vilanRun = VILAN()
vilanRun.show()
app.exec_()
