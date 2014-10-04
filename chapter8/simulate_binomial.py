from scitools.std import *

N = 10**5
def simulate_binomial(p,n,x):
	'''
	Returns the probability estimate of simulating
	binomial trials with probability of success p,
	n trials, and our RV x.
	We simulate it N times and return M/N, where
	M is when after n trials, we have exactly x successes

	The function also returns the error
	'''
	M = 0
	for i in range(N):
		successes = 0
		for j in range(n):
			if random.uniform(0,1) < p:
				successes += 1
		if successes == x:
			M += 1

	prob = float(M)/N
	actual = float(factorial(n))/(factorial(x)*factorial(n-x))\
		* p**x * (1-p)**(n-x)
	error = abs(actual - prob)
	return prob, error

# case 1
print 'Probability of getting two heads when flipping a coin five times'
prob, error = simulate_binomial(0.5,5,2)
print 'Estimated probability = %f' % prob
print 'Error = %g' % error

# case 2
print 'Probability of rolling four ones in a row when throwing a die'
prob, error = simulate_binomial(1./6,4,4)
print 'Estimated probability = %f' % prob
print 'Error = %g' % error

# case 3
print 'Probability a skier will break her skis at least once in five competitions'
prob, error = simulate_binomial(119./120,5,5)
prob1 = 1-prob
print 'Estimated probability = %f' % prob1
print 'Error = %g' % error

'''
python simulate_binomial.py
Probability of getting two heads when flipping a coin five times
Estimated probability = 0.313190
Error = 0.00069
Probability of rolling four ones in a row when throwing a die
Estimated probability = 0.000740
Error = 3.16049e-05
Probability a skier will break her skis at least once in five competitions
Estimated probability = 0.039880
Error = 0.00109799
'''
