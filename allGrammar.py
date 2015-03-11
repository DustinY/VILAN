from dragonfly import *
import pythoncom
import win32com.client
import time
from vilanGrammars import *

#used to end loop
loopCheck = True

class navigationalRule(MappingRule):
	mapping = {
		"down" : Key("down"),
		"up" : Key("up"),
		"left" : Key("left"),
		"right" : Key("right"),
		"enter" : Key("enter"),
		"tab" : Key("tab"),
	}
rule = navigationalRule()
class openRule(CompoundRule):
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

class turnOffRule(CompoundRule):
	spec = "turn off"
	extras = None
	def _process_recognition(self, node, extras):
		grammar.disable()
		gmailGrammar.disable()
		bookmarkGrammar.disable()
		allGrammar.disable()
		stopGrammar.enable()

class shutOffRule(compoundRule):
	spec = "shut off program"
	extras = None
	def _process_recognition(self, node, extras):
		loopCheck = False

rule = navigationalRule()
allGrammar.add_rule(rule)
rule = openRule()
allGrammar.add_rule(rule)
rule = shufOffRule()
allGrammar.add_rule(rule)
