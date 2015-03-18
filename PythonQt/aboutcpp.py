import about
import sys
from about import *
from PyQt5 import *
from PyQt5 import QtWidgets
'''
#include "about.h"
#include "ui_about.h"
'''

class About(QtWidgets.QMainWindow, Ui_About):
    def __init__(self, parent=None):
        self.setupUi(self)
