from dragonfly import *
import pythoncom
import win32com.client
import time
from vilanGrammars import *

class browserNavigation(MappingRule):
	mapping = {
		"click <option>" : Key("c-f/25") + Text("%(option)s\n") + Key("escape/25,enter"),
		"close browser": Key("a-f4"),
		"close chrome" : Key("a-f4"),
		"close tab" : Key("c-w"),
		"go back": Key("a-left"),
		"go backward": Key("a-left"),
		"go backwards": Key("a-left"),
		"go forward" : Key("a-right"),
		"go forwards": Key("a-right"),
		"go front" : Key("a-right"),
		"go [to] home": Key("a-home"),
		"go [to] [the] bottom": Key("end"),
		"go [to] [the] next page" : Key("a-right"),
		"go [to] [the] previous page": Key("a-left"),
		"go [to] [the] top": Key("home"),
		"tab left": Key("cs-tab"),
		"tab right": Key("c-tab"),
		"tab one": Key("c-1"),
		"tab two": Key("c-2"),
		"tab three": Key("c-3"),
		"tab four": Key("c-4"),
		"tab five": Key("c-5"),
		"tab six": Key("c-6"),
		"tab seven": Key("c-7"),
		"tab eight": Key("c-8"),
	}
	extras = [
        Dictation("option"),
    ]

class SearchNavigation(MappingRule):
	mapping = {
		"find <option>" : Key("c-f/25") + Text("%(option)s\n"),
		"next" : Key("c-g"),
		"previous" : Key("cs-g"),
		"search [for] <option>": Key("c-l") + Text("%(option)s\n"),
		"select" : Key("escape/25, enter"),
	}
	extras = [
		Dictation("option")
		]

rule = browserNavigation()
grammar.add_rule(rule)
rule = SearchNavigation()
grammar.add_rule(rule)
