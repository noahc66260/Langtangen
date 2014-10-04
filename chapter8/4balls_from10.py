# I am going to treat the question as if there were no replacement

import random
hat = [0]*40
for i in range(len(hat)):
	if 0<= i <= 9:
		hat[i] = 'red'
	elif 10 <= i <= 19:
		hat[i] = 'blue'
	elif 20 <= i <= 29:
		hat[i] = 'yellow'
	elif 30 <= i <= 39:
		hat[i] = 'purple'

from scitools.std import array, append
import copy
N = 10**4
successes = 0
total = 0
for i in range(N):
	temp = copy.deepcopy(hat)
	selection = []
	for j in range(10):
		pick = random.choice(temp)
		temp.remove(pick)
		selection = append(selection, pick)
	n_blue = sum(array(selection) == 'blue')
	n_purple = sum(array(selection) == 'purple')
	if n_blue == 2 and n_purple == 2:
		successes += 1
	total += 1

print 'Our probability of picking two blue balls and two'
print 'purple balls from ten picks without repalcement is'
print '%.6f' % (float(successes) / total)

'''
python 4balls_from10.py
Our probability of picking two blue balls and two
purple balls from ten picks without repalcement is
0.090600
'''
