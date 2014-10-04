import sys
from scitools.std import *
usage = '%s *.dat' % sys.argv[0]

try: 
	filename = sys.argv[1]
except:
	print usage
	sys.exit(1)

infile = open(filename, 'r')
temp = [] # in C
density = [] # in kg/m**3
for line in infile:
	if line[0] == '#' or line.strip() == '':
		continue
	else:
		words = line.split()
		temp.append(float(words[0]))
		density.append(float(words[1]))
infile.close()
plot(temp, density, xlabel='Temperature (C)', ylabel='Density (kg/m**3)')
raw_input('Press Enter to quit: ')

