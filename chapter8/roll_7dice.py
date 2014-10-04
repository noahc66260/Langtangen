from numpy import *

N = 10**7
n = 7

rolls = random.randint(1,7,n*N)
rolls.resize(N,n)
rolls = sum(rolls,1)
successes = sum(where(rolls == n*6, 1, 0))
prob = float(successes)/N
print 'Probability of getting seven 6\'s in a row: %g' % (prob)
print 'Compare to (1/6)**7 = %g' % ((1./6)**7)

'''
python roll_7dice.py
Probability of getting seven 6's in a row: 3.4e-06
Compare to (1/6)**7 = 3.57225e-06
'''
