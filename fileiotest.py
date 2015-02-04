# if input starts with some p from phrases, 
# (input - p) is passed as arg to p's function

import keywordmodules as km

def read_keywords(filename):
	keywords = []
	f = open(filename)

	for line in f:
		s = line.rstrip()
		if s and not s.startswith("#"):
			keywords.append(s)

	return keywords

keywords = read_keywords('keywords.dat')
	
input = "open chrome"
for k in keywords:
	if input.startswith(k):
		arg = input.replace(k,"").lstrip()
		eval("km." + k + "(\"" + arg + "\")")