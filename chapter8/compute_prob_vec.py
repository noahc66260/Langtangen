from numpy import *

N = 10**5
r = random.uniform(0,1,N)
r1 = r[r <= 0.6]
num = r1[r1 >= 0.5].size
print 'The number of elements between 0.5 and 0.6 out of %g points from the uniform distribution on [0,1) is %d' % (N, num)

'''
python compute_prob_vec.py
The number of elements between 0.5 and 0.6 out of 100000 points from the uniform distribution on [0,1) is 10109
'''
