	
def whois(new):
	print new
	print self.inicio()

	for i in data: 
		comand = "whois " + i 
		process = os.popen(comand)
		result = str(process.read())