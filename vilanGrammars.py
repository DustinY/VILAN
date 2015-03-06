from dragonfly import *

gmailContext = AppContext(executable="chrome", title="@gmail.com - Gmail")
bookmarkContext = AppContext(executable="chrome", title="Bookmark Manager")
mainContext = ~gmailContext

grammar = Grammar("Main Grammar", context=mainContext)
gmailGrammar = Grammar("Gmail Grammar", context=gmailContext)
