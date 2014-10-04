from scitools.std import * # do I need this?
import sys
from scitools.StringFunction import StringFunction

usage = '%s function a b n filename\n(n equally spaced values on interval [a,b])' \
	% sys.argv[0]

try:
	f = StringFunction(sys.argv[1])
	a = float(sys.argv[2])
	b = float(sys.argv[3])
	n = int (sys.argv[4])
	filename = sys.argv[5]
except:
	print usage
	sys.exit(1)

x = linspace(a,b,n)
y = f(x)

outfile = open(filename, 'a') # I don't want to clobber the file
for i in range(len(x)): #x and y are the same length
	outfile.write('%f\t%f\n' % (x[i], y[i]))

'''
I tried the following
python write_cml_function.py 'x**2' 1 10 50 exercise_6.19.dat
See exercise_6.19.dat for output
'''
