from dragonfly import *
import pythoncom
import win32com.client
import time
from vilanGrammars import *

class mainRule(MappingRule):
	mapping = {
		"archive current [e-mail]" : Key("rbracket"),
		"archive" : Key("e"),
		"BCC" : Key("cs-b"),
		"CC" : Key("cs-c"),
		"change label to <label>" : Key("v") + Text("%(label)s\n") + Key("escape, escape"),
		"chat with <person>" : Key("q") + Text("%(person)s\n"),
		"compose [new] [mail]" : Key("c"),
		"compose in new tab" : Key("d"),
		"delete e-mail" : Key("hash"),
		"delete message" : Key("hash"),
		"email <recipient>" : Key("c") + Text("%(recipient)s\n"),
		"escape" : Key("escape, escape"),
		"focus main window" : Key("c-escape"),
		"forward [e-mail]" : Key("f"),
		"forward [e-mail] in new tab" : Key("s-f"),
		"from <sender>" : Key("cs-f") + Text("%(sender)s\n"),
		"label as <label>": Key("l") + Text("%(label)s\n") + Key("escape, escape"),
		"label" : Key("l"),
		"mark [as] important" : Key("plus"),
		"mark [as] read" : Key("s-i"),
		"mark [as] unimportant" : Key("minus"),
		"mark [as] unread" : Key("s-u"),
		"[mark] [report] [as] spam" : Key("bang"),
		"next e-mail" : Key("k"),
		"next message" : Key("k"),
		"next tab" : Key("backtick, down"),
		"open chat" : Key("q"),
		"open" : Key("o"),
		"previous e-mail" : Key("j"),
		"previous message" : Key("j"),
		"previous tab" : Key("tilde, down"),
		"remove" : Key("y"),
		"reply [to] all" : Key("a"),
		"reply [to] all in new tab" : Key("s-a"),
		"reply" : Key("r"),
		"reply in new tab" : Key("s-r"),
		"return" : Key("u"),
		"save [draft]" : Key("c-s"),
		"search email [for] <option>" : Key("slash") + Text("%(option)s\n"),
		"select e-mail" : Key("x"),
		"select message" : Key("x"),
		"send [message]" : Key("c-enter"),
		"star [e-mail]" : Key("s"),
		"type <text>" : Text("%(text)s"),
		"undo" : Key("z"),
		"update" : Key("s-n"),
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
