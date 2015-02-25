from dragonfly import *
import pythoncom
import win32com.client
import time
from vilanGrammars import *

class mainRule(MappingRule):
	mapping = {
		"compose [new] [mail]" : Key("c"),
		"email <recipient>" : Key("c") + Text("%(recipient)s\n"),
		"type <text>" : Text("%(text)s"),
	}
	extras = [
			Dictation("recipient"),
			Dictation("text"),
		]
		
class grammarRule(CompoundRule):
	spec = "disable <option>"
	extras = [Choice("option",{
		"grammar": "gmail"
		}
		)
		]
	def _proccess_recogntion(self, noe, extras):
		chosen = extras["option"]
		if(chosen == "gmail"):
			gmailGrammar.disable()
			grammar.enable()

rule = mainRule()
gmailGrammar.add_rule(rule)
rule = grammarRule()
gmailGrammar.add_rule(rule)