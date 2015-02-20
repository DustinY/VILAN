from dragonfly import *
import pythoncom
#import win32com.client
import time

#newshell = win32com.client.Dispatch("WScript.Shell")

continueLoop = True
#Class for creating the open rules
grammar = Grammar("test grammar")
from dragonfly.engines.backend_sapi5.engine import Sapi5InProcEngine

engine = Sapi5InProcEngine()
engine.connect()

class OpenRule(CompoundRule):
    spec = "open <option>"
    extras = [Choice("option", {
        "chrome":"chrome",
        "browser":"chrome",
        "email":"www.gmail.com",
        "the mail":"www.gmail.com",
        "gmail":"www.gmail.com"
        }
        )
        ]
    def _process_recognition(self, node, extras):
        chosen = extras["option"]
        shell = Key("w-r")
        shell.execute()
        shell = Text(chosen)
        shell.execute()
        shell = Key("enter")
        shell.execute()

rule = OpenRule()
grammar.add_rule(rule)

class BrowserNavigate(CompoundRule):
	spec = "go <option>"
	extras = [Choice("option", {
        "forward":"f",
        "front":"f",
        "next page":"f",
		"to next page":"f",
		"to the next page":"f",
        "forwards":"f",
        "backwards":"b",
		"backward":"b",
		"back":"b",
		"previous page":"b",
        "to previous page":"b",
		"to the previous page":"b"
		}
        )
        ]
    def _process_recognition(self, node, extras):
        chosen = extras["option"]
		if(chosen == "f")
			shell = Key("a-right")
			shell.execute()
		elif(chosen == "b")
			shell = Key("a-left")
			shell.execute()

rule = BrowserNavigate()
grammer.add_rule(rule)

class TurnoffRule(CompoundRule):
    spec = "turn <option>"
    extras = [Choice("option", {
        "off":"off",
        "on":"on"}
        )
        ]
    def _process_recognition(self, node, extras):
        chosen = extras["option"]
        if chosen == "off":
            self.loopStatus = "off"


rule = TurnoffRule()
grammar.add_rule(rule)
engine._load_grammar(self, grammar)


#def response(phrase, listenter):
#    print "You said %s" % phrase


while continueLoop:
    pythoncom.PumpWaitingMessages()
    #print "Waiting"
    time.sleep(.1)