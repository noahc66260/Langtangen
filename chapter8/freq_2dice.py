import random
import numpy as np

sums = {}
for i in range(2,13):
	sums[i] = 0

N = 10**4
for i in range(N):
	s = np.sum(np.random.randint(1,7,2))
	sums[s] += 1

print '%10s %20s' % ('sum', 'probability')
prob_sum = 0
for s in sums:
	prob = float(sums[s])/N
	prob_sum += prob
	print '%10i %20f' %  (s, float(sums[s])/N)

print 'sum of probabilities =  %f' % prob_sum

'''
python freq_2dice.py
       sum          probability
         2             0.024400
         3             0.057700
         4             0.078600
         5             0.111000
         6             0.139200
         7             0.166500
         8             0.141400
         9             0.109600
        10             0.082500
        11             0.061000
        12             0.028100
sum of probabilities =  1.000000
'''
