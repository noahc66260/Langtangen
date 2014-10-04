import random
lower = 0.5
upper = 0.6

i = [1,2,3,6]
for j in i:
	hits = 0
	total = 0
	for k in range(10**j):
		x = random.uniform(0,1)
		if lower <= x <= upper:
			hits += 1
		total += 1
	print 'After 10**%d trials, the probability is %f' \
		% (j, float(hits)/total)

'''
python compute_prob.py
After 10**1 trials, the probability is 0.300000
After 10**2 trials, the probability is 0.160000
After 10**3 trials, the probability is 0.115000
After 10**6 trials, the probability is 0.100275
'''
