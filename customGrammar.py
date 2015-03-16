from dragonfly import *
import pythoncom
import win32com.client
import time
from vilanGrammars import *

def create_dict_from_file(filename):
	dict = {}
	f = open(filename)

	for line in f:
		s = line.rstrip()
		if s and not s.startswith("#"):
			key, value = s.split(",")
			dict[key] = value

	return dict

customCommands = create_dict_from_file("customCommands.dat")

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

rule = mainRule()
customGrammar.add_rule(rule)