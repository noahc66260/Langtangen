from scitools.std import *

filename = 'constants.txt'
infile = open(filename, 'r')
infile.readline()
infile.readline() # discard first two lines

constants = {}
for line in infile:
	words = line.split()
	key = ' '.join(words[0:-2])
	constants[key] = float(words[-2])

for key in constants:
	print 'constants["%s"] = %g' % (key,constants[key])
