from dragonfly import *
import pythoncom
import win32com.client
import time
from vilanGrammars import *

class mainRule(MappingRule):
	mapping = {
		"compose [new] [mail]" : Key("c"),
		"compose in new tab" : Key("d"),
		"email <recipient>" : Key("c") + Text("%(recipient)s\n"),
		"type <text>" : Text("%(text)s"),
		"CC" : Key("cs-c"),
		"BCC" : Key("cs-b"),
		"from <sender>" : Key("cs-f") + Text("%(sender)s\n"),
		"focus main window" : Key("c-escape"),
		"send [message]" : Key("c-enter"),
		"next [e-mail]" : Key("k"),
		"previous [e-mail]" : Key("j"),
		"search <option>" : Key("slash") + Text("%(option)s\n"),
		"next tab" : Key("backtick, down"),
		"previous tab" : Key("tilde, down"),
		"open" : Key("o"),
		"archive" : Key("e"),
		"return" : Key("u"),
		"select e-mail" : Key("x"),
		"select message" : Key("x"),
		"star [e-mail]" : Key("s"),
		"mark [as] important" : Key("plus"),
		"mark [as] unimportant" : Key("minus"),
		"[mark] [report] [as] spam" : Key("bang"),
		"reply" : Key("r"),
		"reply in new tab" : Key("s-r"),
		"replay [to] all" : Key("a"),
		"reply [to] all in new tab" : Key("s-a"),
		"forward [e-mail]" : Key("f"),
		"forward [e-mail] in new tab" : Key("s-f"),
		"escape" : Key("escape, escape"),
		"save [draft]" : Key("c-s"),
		"delete e-mail" : Key("hash"),
		"delete message" : Key("hash"),
		"label" : Key("l"),
		"label as <label>": Key("l") + Text("%(label)s\n") + Key("escape, escape"),
		"change label to <label>" : Key("v") + Text("%(label)s\n") + Key("escape, escape"),
		"mark [as] read" : Key("s-i"),
		"mark [as] unread" : Key("s-u"),
		"undo" : Key("z"),
		"archive current [e-mail]" : Key("rbracket"),
		"open chat" : Key("q"),
		"chat with <person>" : Key("q") + Text("%(person)s\n"),
		"update" : Key("s-n"),
		"remove" : Key("y"),
	}
	extras = [
			Dictation("recipient"),
			Dictation("text"),
			Dictation("option"),
			Dictation("sender"),
			Dictation("label"),
			Dictation("person"),
		]

rule = mainRule()
gmailGrammar.add_rule(rule)
