def equal(expr1, expr2, A, B, n=500):
	'''
	Tests whether two expressions are equal.
	expr1 and expr2 are functions of two variables
	To test for equality, we pick a random real number
	between A and B and plug into both expressions
	and check if their difference is very small.
	We measure equality as percentage of the time that
	they are equal for n trials.
	
	The funciton returns a floating number that represents
	the percentage of the time expr1 and expr2 are equal.
	'''
	epsilon = 1E-10
	import random
	fc = 0 # failure count
	for i in range(n):
		a = random.uniform(A,B)
		b = random.uniform(A,B)
		diff = abs(expr1(a,b)-expr2(a,b))
		if diff > epsilon:
			fc += 1
	return (1-float(fc)/n)

def _test():
	x = equal(lambda x,y: x+y, lambda x,y: y+x, -100, 100)
	print 'x + y == y + x %.1f percent of the time' % (x*100)
	x = equal(lambda x,y: x*y, lambda x,y: y*x, -100, 100)
	print 'x * y == y * x %.1f percent of the time' % (x*100)
	

if __name__ == '__main__':
	_test()

'''
python math_identities_failures_cml.py
x + y == y + x 100.0 percent of the time
x * y == y * x 100.0 percent of the time
'''	
