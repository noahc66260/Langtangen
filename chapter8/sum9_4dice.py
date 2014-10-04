import random
import numpy as np

N = 10**5
winnings = 0
for i in range(N):
	winnings -= 1 # pay 1 unit to play
	rolls = np.random.randint(1,7,4)
	if np.sum(rolls) < 9:
		winnings += 10
	
print 'You start playing with 0 units of money'
print 'You end playing after %g rounds with %d units of money' % (N, winnings)

'''
python sum9_4dice.py
You start playing with 0 units of money
You end playing after 100000 rounds with -45420 units of money

# evidently it's a losing game. Don't play.
'''
