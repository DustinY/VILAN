from dragonfly import *
import pythoncom
import win32com.client
import time
from vilanGrammars import *


class mainRule(MappingRule):
    mapping = {
        "Bookmarks" : Mouse("(1.0,0.0)") + Mouse("<-95,97>, left") + Key("tab:4, down"),
        "Folder options" : Mouse("(1.0,0.0)") + Mouse("<-95,97>, left") + Key("tab, down"),
        "Folders" : Mouse("(1.0,0.0)") + Mouse("<-95,97>, left") + Key("tab:2, down"),
        "Organize" : Mouse("(1.0,0.0)") + Mouse("<-95,97>, left") + Key("tab:3, down"),
        "Search" : Mouse("(1.0,0.0)") + Mouse("<-95,97>, left"),
        "Select bookmark" : Key("enter:2"),
        "type <text>" : Text("%(text)s"),
    }
    extras = [
        Dictation("text"),
    ]

rule = mainRule()
bookmarkGrammar.add_rule(rule)
