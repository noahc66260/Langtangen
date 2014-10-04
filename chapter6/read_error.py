filename = 'lnsum.txt'
infile = open(filename, 'r')

epsilon = []
exact_error = []
n = []
for line in infile:
	if 'epsilon:' not in line:
		continue
	words = line.split(',')
	eps = float(words[0].split(':')[-1])
	epsilon.append(eps)
	err = float(words[1].split(':')[-1])
	exact_error.append(err)
	i = int(words[2].split('=')[-1])
	n.append(i)

from scitools.std import *
plot(n,epsilon, log='y', 
	xlabel='n',
	ylabel='epsilon',
	title='epsilon v. n')
figure()
plot(n, exact_error, log='y',
	xlabel='n',
	ylabel='exact error',
	title='exact error v. n')
raw_input('Press Enter to quit: ')
	
