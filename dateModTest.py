import os.path
import time
import threading


def lastMod():
    print "last modified: %s" %
    time.ctime(os.path.getmtime("dateModTestFile.txt"))

    threading.Timer(5, lastMod).start()

lastMod()
