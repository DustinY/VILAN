from dragonfly import *
import pythoncom
#import win32com.client
import time

#shell = win32com.client.Dispatch("WScript.Shell")
continueLoop = True
#Class for creating the open rules
grammar = Grammar("test grammar")
from dragonfly.engines.backend_sapi5.engine import Sapi5InProcEngine

engine = Sapi5InProcEngine()
engine.connect()

class TestRule(CompoundRule):
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
		time.sleep(.1)
		shell = Text(chosen)
		shell.execute()
		shell = Key("enter")
		shell.execute()

rule = TestRule()
grammar.add_rule(rule)


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
#grammar.load()
engine._load_grammar(grammar)
#engine.activate_grammar(grammar)

#def response(phrase, listenter):
#	print "You said %s" % phrase


while continueLoop:

	pythoncom.PumpWaitingMessages()
	print engine._recognizer_dispatch_name
	print "Waiting"
	time.sleep(.1)