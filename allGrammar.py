import os
from dragonfly import *
import pythoncom
import win32com.client
import time
from vilanGrammars import *

#used to end loop
loopCheck = True

class navigationalRule(MappingRule):
	mapping = {
		"delete" : Key("delete"),
		"down" : Key("down"),
		"enter" : Key("enter"),
		"left" : Key("left"),
		"right" : Key("right"),
		"tab" : Key("tab"),
		"tab back" : Key("s-tab"),
		"up" : Key("up"),
		"type <text>" : Text("%(text)s"),
		"backspace": Key("backspace"),
		"back space" : Key("backspace"),
		"select all" : Key("cs-a"),
		"select previous" : Key("cs-left"),
		"delete previous" : Key("cs-left, delete"),
		"select next" : Key("cs-right"),
		"edit commands" : Key("w-r/25") + Text("C:/Users/Dustin/Desktop/Demo/VDATABASE.exe") + Key("enter"),
	}
	extras=[
		Dictation("text"),
	]

class openRule(MappingRule):
	mapping = {
		"open bookmarks": BringApp("chrome") + Key("cs-o"),
		"open browser": Key("w-r/25") + Text("chrome") + Key("enter"),
		"open chrome": Key("w-r/25") + Text("chrome") + Key("enter"),
		"open downloads": BringApp("chrome") + Key("c-j"),
		"open email": Key("w-r/25") + Text("www.gmail.com") + Key("enter"),
		"open gmail": Key("w-r/25") + Text("www.gmail.com") + Key("enter"),
		"open last tab": BringApp("chrome") + Key("cs-t"),
		"open [new] tab": BringApp("chrome") + Key("c-t"),
		"open history": BringApp("chrome") + Key("c-h"),
		"open the mail": Key("w-r/25") + Text("www.gmail.com") + Key("enter"),
	}

class turnOffRule(CompoundRule):
	spec = "turn off"
	extras = []
	def _process_recognition(self, node, extras):
		grammar.disable()
		gmailGrammar.disable()
		bookmarkGrammar.disable()
		allGrammar.disable()
		stopGrammar.enable()


class shutOffRule(CompoundRule):
	spec = "end program"
	extras = []
	def _process_recognition(self, node, extras):
		os.system("taskkill /f /im pythonw.exe")

rule = navigationalRule()
allGrammar.add_rule(rule)
rule = openRule()
allGrammar.add_rule(rule)
rule = turnOffRule()
allGrammar.add_rule(rule)
rule = shutOffRule()
allGrammar.add_rule(rule)
