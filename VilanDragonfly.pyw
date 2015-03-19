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

from dragonfly.engines.backend_sapi5.engine import Sapi5InProcEngine

engine = Sapi5InProcEngine()
engine.connect()

grammarWrapper = engine._load_grammar(grammar)
gmailGrammarWrapper = engine._load_grammar(gmailGrammar)
bookmarkGrammarWrapper = engine._load_grammar(bookmarkGrammar)
allGrammarWrapper = engine._load_grammar(allGrammar)
customGrammarWrapper = engine._load_grammar(customGrammar)
#stopGrammarWrapper = engine._load_grammar(stopGrammar)

while True:
	pythoncom.PumpWaitingMessages()
	global loopCheck
	continueLoop = loopCheck
	time.sleep(.1)
