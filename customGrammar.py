from dragonfly import *
import pythoncom
import win32com.client
import time
from vilanGrammars import *

import os.path, time
import threading

def create_dict_from_file(filename):
    dict = {}
    f = open(filename)

    for line in f:
        s = line.rstrip()
        if s and not s.startswith("#"):
            key, value = s.split(",")
            dict[key] = value

    return dict

#datelastMod = time.ctime(os.path.getmtime("C:\Users\Dustin\Documents\GitHub\VILAN\customCommands.dat"))
#customCommands = create_dict_from_file("C:\Users\Dustin\Documents\GitHub\VILAN\customCommands.dat")

'''class mainRule(CompoundRule):
    spec = "open <option>"
    extras = [Choice("option", customCommands)]

    def _process_recognition(self, node, extras):
        chosen = extras["option"]

        shell = Key("w-r")
        shell.execute()
        time.sleep(.1)
        shell = Text(chosen)
        shell.execute()
        time.sleep(.1)
        shell = Key("enter")
        shell.execute()
'''
#customRule
#customGrammar.add_rule(customRule)

def lastMod():
    customCommands = create_dict_from_file("C:\Users\Dustin\Documents\GitHub\VILAN\VDATABASE\DOCS\customCommands.dat")
    print customCommands
    class mainRule(CompoundRule):
        spec = "open <option>"
        extras = [Choice("option", customCommands)]

        def _process_recognition(self, node, extras):
            chosen = extras["option"]

            shell = Key("w-r")
            shell.execute()
            time.sleep(.1)
            shell = Text(chosen)
            shell.execute()
            time.sleep(.1)
            shell = Key("enter")
            shell.execute()
    customRule = mainRule()
    if (customGrammar.rules):
        customGrammar.remove_rule(customGrammar.rules[0])
    #global datelastMod
    #newDateLastMod = time.ctime(os.path.getmtime("C:\Users\Dustin\Documents\GitHub\VILAN\customCommands.dat"))
    #if newDateLastMod is not datelastMod:
    customGrammar.add_rule(customRule)
    #datelastMod = newDateLastMod
    threading.Timer(1, lastMod).start()

lastMod()
