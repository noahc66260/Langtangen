filename = 'xy.dat'
infile = open(filename, 'r')
x = []
y = []
for line in infile:
	words = line.split()
	x.append(float(words[0]))
	y.append(float(words[1]))
infile.close()
from scitools.std import *
x = array(x)
y = array(y)
print 'The maximum y coordinate is %6.4f' % max(y)
print 'The minimum y coordinate is %6.4f' % min(y)
plot(x,y, xlabel='x', ylabel='y')
raw_input('Press Enter to quit: ')

'''
python read_2columns.py
The maximum y coordinate is 0.9482
The minimum y coordinate is -0.9482
Press Enter to quit: 
'''
