from dragonfly import *
import pythoncom
import win32com.client
import time
from vilanGrammars import *

class grammarRule(CompoundRule):
	spec = "start <option>"
	extras = [Choice("option",{
		"listening": "start"
		}
		)
		]
	def _proccess_recognition(self, noe, extras):
		chosen = extras["option"]
		if(chosen == "start"):
			pauseGrammar.disable()
			grammar.enable()
			
rule = grammarRule()
pauseGrammar.add_rule(rule)