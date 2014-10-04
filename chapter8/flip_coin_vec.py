from numpy import *

N = 10**6
TAILS = 1
HEADS = 2
r = random.randint(1,3,N) 
ntails = sum(where(r == TAILS,1,0))
print 'Number of tails after %g coin flips = %d' % (N, ntails)

'''
python flip_coin_vec.py
Number of tails after 1e+06 coin flips = 500066
'''
