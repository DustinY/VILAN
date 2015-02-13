import keywordmodules as km

def read_keywords(filename):
	keywords = []
	f = open(filename)

	for line in f:
		s = line.rstrip()
		if s and not s.startswith("#"):
			keywords.append(s)

	return keywords

def exec_input(input):
	input = input.lower()
	recognized = False
	
	for k in keywords:
		if input.startswith(k):
			arg = input.replace(k,"").lstrip()
			k = k.replace(" ","_")
			eval("km." + k + "(\"" + arg + "\")")
			recognized = True
			break
	
	if not recognized:
		print "I don't understand:", input

keywords = read_keywords('keywords.dat')


# Tests
inputs = []
inputs.append("open chrome")
inputs.append("open notchrome")
inputs.append("go to google")
inputs.append("go to notgoogle")
inputs.append("fakecommand test")

for input in inputs:
	exec_input(input)