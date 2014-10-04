from scitools.std import *
filename = 'pendulum.dat'
infile = open(filename, 'r')
infile.readline() # discard first line

L = []
T = []
for line in infile: 
	words = line.split()
	L.append(float(words[0]))
	T.append(float(words[1]))
infile.close()

figure()
poly1 = polyfit(L,T,1)
poly2 = polyfit(L,T,2)
poly3 = polyfit(L,T,3)
x = linspace((min(L)), (max(L)), 500)
p = poly1d(poly1)
T_fit1 = p(x)
p = poly1d(poly2)
T_fit2 = p(x)
p = poly1d(poly3)
T_fit3 = p(x)
plot(L,T,'o',
	x,T_fit1,
	x,T_fit2,
	x,T_fit3,
	xlabel='Length of Pendulum',
	ylabel='Period',
	legend=['data points', 'degree-1 polynomial', 'degree-2 polynomial',
		'degree-3 polynomial'])
raw_input('Press Enter to quit: ')

