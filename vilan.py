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
from dragonfly.engines.backend_sapi5.engine import Sapi5InProcEngine

class Vilan():
		engine = Sapi5InProcEngine()
		engine.connect()
		#loading grammars and creating wrappers
		grammarWrapper = engine._load_grammar(grammar)
		gmailGrammarWrapper = engine._load_grammar(gmailGrammar)
		bookmarkGrammarWrapper = engine._load_grammar(bookmarkGrammar)
		allGrammarWrapper = engine._load_grammar(allGrammar)
		stopGrammarWrapper = engine._load_grammar(stopGrammar)
		#unloading grammars for initial state
		engine._unload_grammar(bookmarkGrammar, bookmarkGrammarWrapper)
		engine._unload_grammar(gmailGrammer, gmailGrammarWrapper)
		engine._unload_grammar(stopGrammar, stopGrammarWrapper)
		#variable to end program
		continueLoop = True
		#function to automatically change grammars
		def grammarActivation():
			window = Window.get_foreground()
			if window.executable == property(fget="chrome") and window.title == property(fget="@gmail.com - Gmail"):
				engine._load_grammar(gmailGrammar)
				engine._unload_grammar(bookmarkGrammar, bookmarkGrammarWrapper)
				engine._unload_grammar(grammar, grammarWrapper)
			elif window.executable == "chrome" and window.title == "Bookmark Manager":
				engine._load_grammar(bookmarkGrammar)
				engine._unload_grammar(gmailGrammar, gmailGrammarWrapper)
				engine._unload_grammar(grammar, grammarWrapper)
			else:
				engine._unload_grammar(bookmarkGrammar, bookmarkGrammarWrapper)
				engine._unload_grammar(gmailGrammar, gmailGrammarWrapper)
				engine._load_grammar(grammar)
				#self.grammar.process_begin(window.executable, window.title, window.handle)

		def run():
			while continueLoop:
				grammarActivation()
				pythoncom.PumpWaitingMessages()
				continueLoop = loopCheck

start = Vilan()
start.run()
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
