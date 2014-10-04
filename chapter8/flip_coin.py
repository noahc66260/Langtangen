import sys
N = int(sys.argv[1])

import random
for i in range(N):
	r = random.randint(1,2)
	if r == 1:
		print 'HEADS'
	elif r == 2:
		print 'TAILS'

'''
python flip_coin.py 5
TAILS
HEADS
HEADS
HEADS
HEADS
'''
