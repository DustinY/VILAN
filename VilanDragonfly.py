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
from customGrammar import *

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
gmailGrammarWrapper = engine._load_grammar(gmailGrammar)
bookmarkGrammarWrapper = engine._load_grammar(bookmarkGrammar)
allGrammarWrapper = engine._load_grammar(allGrammar)
customGrammarWrapper = engine._load_grammar(customGrammar)
#stopGrammarWrapper = engine._load_grammar(stopGrammar)
#self.grammar.process_begin(window.executable, window.title, window.handle

while continueLoop:
	pythoncom.PumpWaitingMessages()
	global loopCheck
	continueLoop = loopCheck
	time.sleep(.1)
