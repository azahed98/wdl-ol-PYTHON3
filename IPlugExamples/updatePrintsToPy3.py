import sys, os.path

def addParen(args):
	"""
	The goal is to read each line and check if there is a print statement in it.
	If so, we wrap the contents of that print statement in quotes.
	For our basic purposes, we'll just add "(" write after the print and a ")" at the end of the line
	If I encounter anything more complicated, I will add it in the future.
	"""

	assert len(args) == 3, "Arguments: 1)py file to read 2)py file to create"
	assert os.path.isfile(args[1]), "File does not exist"

	new = open(args[2], "w")
	with open(args[1], "r") as old:
		for line in old:
			ind = line.find('print')
			nexind = line.find('\n') #always greater than -1 except for last line

			if ind >= 0: #meaning this line is a print statement
				line = line[0:ind+6]+'('+line[ind+6:]
				if(ind >=0):
					line = line[:len(line)-1]+')'+'\n'
				else:
					line = line + ')'

			new.write(line)
	new.close

addParen(sys.argv)



	
