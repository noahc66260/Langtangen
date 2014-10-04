# part 1
N = 10**6
import random
from scitools.std import array
successes = 0
total = 0
for i in range(N):
	roll = random.randint(1,6)
	if roll == 6:
		successes += 1
	total += 1
print 'The probability of rolling a 6 is %f' % (float(successes)/total)

# part 2
successes = 0
total = 0
for i in range(N):
	rolls = [random.randint(1,6) for j in range(4)]
	if rolls == [6,6,6,6]:
		successes += 1
	total += 1
print 'The probability of rolling four sixes in a row is %f' \
	% (float(successes)/total)

# part 3
successes = 0
total = 0
for i in range(N):
	rolls = [random.randint(1,6) for j in range(4)]
	if rolls[:-1] == [6,6,6]:
		if rolls[-1] == 6:
			successes += 1
		total += 1
		
print 'The probability of rolling a 6 if we\'ve rolled three'
print 'sixes already is %f' % (float(successes)/total)

'''
python rolling_dice.py
The probability of rolling a 6 is 0.167023
The probability of rolling four sixes in a row is 0.000778
The probability of rolling a 6 if we've rolled three
sixes already is 0.172466
'''
