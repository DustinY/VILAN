from dragonfly import *
import pythoncom
import win32com.client
import time
from vilanGrammars import *
from mainGrammar import *
from gmailGrammar import *
from bookmarkGrammar import *
from stopGrammar import *
from allGrammar import *

newshell = win32com.client.Dispatch("WScript.Shell")
#newshell.Run("http://chrome://bookmarks")


continueLoop = True
#Class for creating the open rules
#grammar = Grammar("test grammar")
from dragonfly.engines.backend_sapi5.engine import Sapi5InProcEngine

engine = Sapi5InProcEngine()
engine.connect()
#newshell.Run("endSpeechThing.bat")


grammarWrapper = engine._load_grammar(grammar)
#engine._load_grammar(gmailGrammar)
#engine._load_grammar(bookmarkGrammar)
allGrammarWrapper = engine._load_grammar(allGrammar)
#engine._load_grammar(stopGrammar)

'''grammar.enable()
gmailGrammar.disable()
bookmarkGrammar.disable()
allGrammar.enable()
stopGrammar.disable()
'''
'''engine.activate_grammar(grammar)
engine.deactivate_grammar(gmailGrammar)
engine.deactivate_grammar(bookmarkGrammar)
engine.activate_grammar(allGrammar)
engine.deactivate_grammar(stopGrammar)
'''
def grammarActivation():
	window = Window.get_foreground()
	if window.executable == property(fget="chrome") and window.title == property(fget="@gmail.com - Gmail"):
		engine._load_grammar(gmailGrammar)
		engine._unload_grammar(bookmarkGrammar, grammarWrapper)
		engine._unload_grammar(grammar, grammarWrapper)
	elif window.executable == "chrome" and window.title == "Bookmark Manager":
		engine._load_grammar(bookmarkGrammar)
		engine._unload_grammar(gmailGrammar, grammarWrapper)
		engine._unload_grammar(grammar, grammarWrapper)
	else:
		engine._unload_grammar(bookmarkGrammar, grammarWrapper)
		engine._unload_grammar(gmailGrammar, grammarWrapper)
		engine._load_grammar(grammar)
		#self.grammar.process_begin(window.executable, window.title, window.handle)


while continueLoop:
	grammarActivation()
	pythoncom.PumpWaitingMessages()
	time.sleep(.1)
