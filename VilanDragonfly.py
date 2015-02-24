from dragonfly import *
import pythoncom
import win32com.client
import time

newshell = win32com.client.Dispatch("WScript.Shell")
#newshell.Run("http://chrome://bookmarks")


continueLoop = True
#Class for creating the open rules
grammar = Grammar("test grammar")
from dragonfly.engines.backend_sapi5.engine import Sapi5InProcEngine

engine = Sapi5InProcEngine()
engine.connect()

#newshell.Run("endSpeechThing.bat")


class OpenRule(CompoundRule):
	spec = "open <option>"
	extras = [Choice("option", {
		"chrome":"chrome",
		"browser":"chrome",
		"email":"www.gmail.com",
		"the mail":"www.gmail.com",
		"gmail":"www.gmail.com",
		"bookmarks":"bookmarks",
		"last tab":"last",
		"history":"history",
		"downloads":"downloads"
		}
		)
		]
	def _process_recognition(self, node, extras):
		chosen = extras["option"]
		if (chosen == "bookmarks"):
			BringApp("chrome").execute()
			time.sleep(.1)
			shell = Key("cs-o")
			shell.execute()
		elif (chosen == "last"):
			BringApp("chrome").execute()
			time.sleep(.1)
			shell = Key("cs-t")
			shell.execute()
		elif (chosen == "history"):
			BringApp("chrome").execute()
			time.sleep(.1)
			shell = Key("c-h")
			shell.execute()
		elif (chosen == "downloads"):
			BringApp("chrome").execute()
			time.sleep(.1)
			shell = Key("c-j")
			shell.execute()
		else:
			shell = Key("w-r")
			shell.execute()
			time.sleep(.1)
			shell = Text(chosen)
			shell.execute()
			time.sleep(.1)
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
		"to the previous page":"b",
		"home":"a-home",
		"to home page":"a-home",
		"to top":"home",
		"to bottom":"end"
		}
		)
		]
	def _process_recognition(self, node, extras):
		chosen = extras["option"]
		if(chosen == "f"):
			shell = Key("a-right")
			shell.execute()
		elif(chosen == "b"):
			shell = Key("a-left")
			shell.execute()
		else:
			shell = Key(chosen)
			shell.execute()

rule = BrowserNavigate()
grammar.add_rule(rule)

class CloseNavigate(CompoundRule):
	spec = "close <option>"
	extras = [Choice("option", {
		"tab":"c-w",
		"chrome":"a-f4",
		"browser":"a-f4"
		}
		)
		]
	def _process_recognition(self, node, extras):
		chosen = extras["option"]
		shell = Key(chosen)
		shell.execute()

rule = CloseNavigate()
grammar.add_rule(rule)

'''
class SearchNavigate(CompoundRule):
	spec = "search <option>"
	extras = [Choice("option", {
		"copied text":"c-v"
		}
		)
		]
	def _process_recognition(self, node, extras):
		chosen = extras["option"]
		shell = Key("c-l")
		shell.execute()
		time.sleep(.1)
		shell = Key(chosen) + Key("enter")
		shell.execute()

rule = SearchNavigate()
grammar.add_rule(rule)
'''

class TabNavigate(CompoundRule):
	spec = "tab <option>"
	extras = [Choice("option", {
		"right":"c-tab",
		"left":"cs-tab",
		"one":"c-1",
		"two":"c-2",
		"three":"c-3",
		"four":"c-4",
		"five":"c-5",
		"six":"c-6",
		"seven":"c-7",
		"eight":"c-8"
		}
		)
		]
	def _process_recognition(self, node, extras):
		chosen = extras["option"]
		shell = Key(chosen)
		shell.execute()

rule = TabNavigate()
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
engine._load_grammar(grammar)
#newshell.Run("speechexit")


#def response(phrase, listenter):
#	print "You said %s" % phrase


while continueLoop:
	pythoncom.PumpWaitingMessages()
	#print "Waiting"
	time.sleep(.1)
