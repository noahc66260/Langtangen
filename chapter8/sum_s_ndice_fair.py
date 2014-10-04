import numpy as np
import sys

n = int(sys.argv[1]) 	# number of dice
s = int(sys.argv[2])	# sum we must equal or exceed to win
N = 10**5
successes = 0
total = 0
for i in range(N):
	rolls = np.random.randint(1,7,n)
	if np.sum(rolls) < s:
		successes += 1
	total += 1

print 'The probability of rolling %d dice and getting a sum of' % n
print 'less than %d is %f ' % (s, float(successes)/total) 

'''
python sum_s_ndice_fair.py 4 9
The probability of rolling 4 dice and getting a sum of
less than 9 is 0.054660 
'''
