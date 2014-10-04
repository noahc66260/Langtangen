import sys
from scitools.std import * 

usage = '%s \"f(x)\" xmin xmax' % sys.argv[0]
try:
	f = vectorize(StringFunction(sys.argv[1]))
	xmin = float(eval(sys.argv[2]))
	xmax = float(eval(sys.argv[3]))
except:
	print usage
	sys.exit(1)

x = linspace(xmin, xmax, 500)
plot(x,f(x), xlabel='x', ylabel='y', savefig='tmp.eps')
raw_input('Press Enter to quit: ')

