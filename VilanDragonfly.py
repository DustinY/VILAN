from dragonfly import *
import pythoncom
import win32com.client
import time

from vilanGrammars import *
from mainGrammar import *
from gmailGrammar import *

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


grammar.enable()
gmailGrammar.disable()
bookmarkGrammar.disable()
def grammarActivation():
	window = Window.get_foreground()
    if window.executable == "chrome" & window.title == "@gmail.com - Gmail":
		gmailGrammar.enable()
		bookmarkGrammar.disable()
		grammar.disable()
	elif window.executable == "chrome" & window.title == "Bookmark Manager":
		bookmarkGrammar.enable()
		gmailGrammar.disable()
		grammar.disable()
	else:
		bookmarkGrammar.disable()
		gmailGrammar.disable()
		grammar.enable()
	#self.grammar.process_begin(window.executable, window.title, window.handle)


while continueLoop:
	pythoncom.PumpWaitingMessages()
	time.sleep(.1)
	grammarActivation()
