def substance1(filename):
	'''
	Parses a data file to create a dictionary
	of the names of substances and their densities
	'''
	density = {}
	infile = open(filename, 'r')
	for line in infile:
		words = line.split()
		key = ' '.join(words[:-1])
		density[key] = float(words[-1])
	infile.close()
	return density

def substance2(filename):
	'''
	Parses a data file to create a dictionary
	of the names of substances and their densities
	This is a less efficient version, in my opinion
	'''
	density = {}
	infile = open(filename, 'r')
	k = 13 # position that the density starts at
	for line in infile:
		element = line[:k-1].strip()
		density[element] = float(line[k-1:])
	infile.close()
	return density

filename = 'densities.dat'
density1 = substance1(filename)
density2 = substance2(filename)

print 'Our dictionary using substance1()'
for key in sorted(density1):
	print '%-12s %g' % (key, density1[key])

print
print 'Our dictionary using substance2()'
for key in sorted(density2):
	print '%-12s %g' % (key, density2[key])

'''
python density_improved.py
Our dictionary using substance1()
Earth core   13
Earth mean   5.52
Moon         3.3
Sun core     160
Sun mean     1.4
air          0.0012
gasoline     0.67
gold         18.9
granite      2.7
human body   1.03
ice          0.9
iron         7.8
limestone    2.6
mercury      13.6
platinium    21.4
proton       2.8e+14
pure water   1
seawater     1.025
silver       10.5

Our dictionary using substance2()
Earth core   13
Earth mean   5.52
Moon         3.3
Sun core     160
Sun mean     1.4
air          0.0012
gasoline     0.67
gold         18.9
granite      2.7
human body   1.03
ice          0.9
iron         7.8
limestone    2.6
mercury      13.6
platinium    21.4
proton       2.8e+14
pure water   1
seawater     1.025
silver       10.5
'''
