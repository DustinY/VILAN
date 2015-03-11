from dragonfly import *
import pythoncom
import win32com.client
import time
from vilanGrammars import *

class browserNavigation(MappingRule):
	mapping = {
		"go forward" : Key("a-right"),
		"go front" : Key("a-right"),
		"go next page" : Key("a-right"),
		"go to next page": Key("a-right"),
		"go to the next page": Key("a-right"),
		"go forwards": Key("a-right"),
		"go backwards": Key("a-left"),
		"go backward": Key("a-left"),
		"go back": Key("a-left"),
		"go previous page": Key("a-left"),
		"go to previous page": Key("a-left"),
		"go to the previous page": Key("a-left"),
		"go home": Key("a-home"),
		"go to home page": Key("a-home"),
		"go to top": Key("home"),
		"go to bottom": Key("end"),
		"close tab" : Key("c-w"),
		"close chrome" : Key("a-f4"),
		"close browser": Key("a-f4"),

	}

rule = browserNavigation()
grammar.add_rule(rule)

class SearchNavigate(MappingRule):
	mapping = {
		"search [for] <option>": Key("c-l") + Text("%(option)s\n"),
	}
	extras = [
		Dictation("option")
		]

rule = SearchNavigate()
grammar.add_rule(rule)


class TabNavigate(CompoundRule):
	spec = "tab <option>"
	extras = [Choice("option", {
		"right":"c-tab",
		"left":"cs-tab",
		"one":"c-1",
		"two":"c-2",
		"three":"c-3",
		"four":"c-4",
		"five":"c-5",
		"six":"c-6",
		"seven":"c-7",
		"eight":"c-8"
		}
		)
		]
	def _process_recognition(self, node, extras):
		chosen = extras["option"]
		shell = Key(chosen)
		shell.execute()

rule = TabNavigate()
grammar.add_rule(rule)
