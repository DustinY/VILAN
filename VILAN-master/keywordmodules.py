def create_dict_from_file(filename):
	dict = {}
	f = open(filename)

	for line in f:
		s = line.rstrip()
		if s and not s.startswith("#"):
			key, value = s.split(",")
			dict[key] = value
	
	return dict

programs = create_dict_from_file("programs.dat")
websites = create_dict_from_file("websites.dat")

# Open a program
# 'program' is the program name as said by the user
def open(program=None):
	recognized = False
	
	for p in programs.keys():
		if program == p:
			print "success -", programs[p]
			recognized = True
			break
	if not recognized:
		print "I didn't understand:", program

def go_to(website=None):
	recognized = False
	
	for w in websites.keys():
		if website == w:
			print "going to...", websites[w]
			recognized = True
			break
	if not recognized:
		print "I don't know how to go to", website