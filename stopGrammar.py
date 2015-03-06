from dragonfly import *
import pythoncom
import win32com.client
import time
from vilanGrammars import *

class turnOnRule(CompoundRule):
	spec = "turn on"
	extras = None
	def _process_recognition(self, node, extras):
		grammar.enable()
		stopGrammar.disable()