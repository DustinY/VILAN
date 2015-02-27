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
		"down" : Key("down"),
		"up" : Key("up"),
		"left" : Key("left"),
		"right" : Key("right"),
		"send [message]" : Key("c-enter"),
		"next [e-mail]" : Key("k"),
		"previous [e-mail]" : Key("j"),
		"search <option>" : Key("slash") + Text("%(option)s\n"),
		"tab [right]" : Key("backtick, down"),
		"tab left" : Key("tilde, down"),
		"enter" : Key("enter"),
		"open" : Key("o"),
		"archive" : Key("e"),
		"return" : Key("u"),
		"select [e-mail]" : Key("x"),
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
		"delete [e-mail]" : Key("hash"),
		"label" : Key("l"),
		"label as <label>": Key("l") + Text("%(label)s\n") + Key("escape, escape"),
		"change label to <label>" : Key("v") + Text("%(label)s\n") + Key("escape, escape"),
		"mark [as] read" : Key("s-i"),
		"mark [as] unread" : Key("s-u"),
		"undo" : Key("z"),
		"archive current [e-mail]" : Key("rbracket"),
		
		
		
	}
	extras = [
			Dictation("recipient"),
			Dictation("text"),
			Dictation("option"),
			Dictation("sender"),
			Dictation("label"),
		]
		
class grammarRule(CompoundRule):
	spec = "disable <option>"
	extras = [Choice("option",{
		"gmail grammar": "gmail"
		}
		)
		]
	def _proccess_recogntion(self, noe, extras):
		chosen = extras["option"]
		if(chosen == "gmail"):
			gmailGrammar.disable()
			grammar.enable()

rule = mainRule()
gmailGrammar.add_rule(rule)
rule = grammarRule()
gmailGrammar.add_rule(rule)