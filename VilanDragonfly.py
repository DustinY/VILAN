from dragonfly import *
import pythoncom
import win32com.client
import time

from vilanGrammars import *
from mainGrammar import *
from gmailGrammar import *
from bookmarkGrammar import *

newshell = win32com.client.Dispatch("WScript.Shell")
#newshell.Run("http://chrome://bookmarks")


continueLoop = True
#Class for creating the open rules
#grammar = Grammar("test grammar")
from dragonfly.engines.backend_sapi5.engine import Sapi5InProcEngine

engine = Sapi5InProcEngine()
engine.connect()
#newshell.Run("endSpeechThing.bat")


engine._load_grammar(grammar)
engine._load_grammar(gmailGrammar)
engine._load_grammar(bookmarkGrammar)
gmailGrammar.disable()
bookmarkGrammar.disable()
#grammar.enable()

while continueLoop:
	pythoncom.PumpWaitingMessages()
	#print "Waiting"
	time.sleep(.1)
