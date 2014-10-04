import sys
import numpy as np

n_dice = int(sys.argv[1])
n_experiments = int(sys.argv[2])

throws = np.random.randint(1,7, size=n_dice*n_experiments)
throws.resize(n_experiments, n_dice)
successes = 0
for i in range(n_experiments):
	if sum(throws[i] == 6) > 0:
		successes += 1

print 'The probability of getting at least one six after'
print '%d throws is %f' % (n_dice, float(successes)/n_experiments)

'''
python one6_ndice.py 2 1000000
The probability of getting at least one six after
2 throws is 0.305734
'''
