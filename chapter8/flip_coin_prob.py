from scitools.std import *

N = 1000
N1 = [10,100,500,1000]

HEADS = 0
TAILS = 1
flips = random.randint(0,2,N)

for n in N1:
	p_heads = float(sum(flips[:n] == HEADS))/n
	print 'Probability of landing heads for first %4d flips: %f' \
		% (n, p_heads)

'''
python flip_coin_prob.py
Probability of landing heads for first   10 flips: 0.300000
Probability of landing heads for first  100 flips: 0.480000
Probability of landing heads for first  500 flips: 0.520000
Probability of landing heads for first 1000 flips: 0.490000
'''
