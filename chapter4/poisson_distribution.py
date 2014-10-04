def Poisson(x, t, nu):
	'''
	Calculates the probability that a random variable
	that follows the Poisson distribution has a value x.
	
	The parameter lambda equals the product of t and nu, 
	so t is the time interval and nu is the average number
	of occurrences over the time interval t
	
	The function returns a number between 0 and 1, inclusive.
	'''
	from math import exp, factorial
	p = (nu*t)**x / factorial(x) * exp(-nu*t)
	return p

def test():
	n = 100
	t = 1
	nu = .5
	sum = 0
	for i in range(n):
		sum += Poisson(i,t,nu)
	print '''The sum of probabilities for x = 0,1,...,%d is %f
which should be close to 1''' % (n, sum)	

if __name__ == '__main__':
	test()

'''
python poisson_distribution.py
The sum of probabilities for x = 0,1,...,100 is 1.000000
which should be close to 1
'''
