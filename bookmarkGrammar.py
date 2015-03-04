from dragonfly import *
import pythoncom
import win32com.client
import time
from vilanGrammars import *

class grammarRule(CompoundRule):
	spec = "disable <option>"
	extras = [Choice("option",{
		"grammar": "bookmark",
		}
		)
		]
	def _proccess_recognition(self, noe, extras):
		chosen = extras["option"]
		if(chosen == "bookmark"):
			bookmarkGrammar.disable()
			grammar.enable()

rule = grammarRule()
bookmarkGrammar.add_rule(rule)