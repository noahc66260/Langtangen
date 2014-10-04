def binomial(x, n, p):
	'''
	This function calculates the probability of a 
	binomially distributed random variable having the value x.
	
	n is the number of trials
	p is the probability of success for each independent trial
	x is the value of our RV for which we calculate the probability of

	The function returns a number between 0 and 1, inclusive.
	'''
	from math import factorial
	bc = float(factorial(n))/(factorial(x)*factorial(n-x)) # binomial coefficient
	return bc * p**x * (1-p)**(n-x)

def test():
	n = 100
	sum = 0
	p = .5
	for x in range(0,n+1):
		sum += binomial(x,n,p)
	print 'The sum of all probabilities should add to 1'
	print 'We have calculated the sum for n = 100 to be %.2f' % (sum)

if __name__ == '__main__':
	test()

'''
python binomial_distribution.py
The sum of all probabilities should add to 1
We have calculated the sum for n = 100 to be 1.00
'''
