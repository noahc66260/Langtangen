def Lagrange(x, points):
	'''
	Implementation of Lagrange's interpolation formula
	x is the point at which we make the interpolation estimate
	points is a set of n+1 2-tuples such that points[i,0]
	is the x-coordinate of point i and points[i,1] is the 
	y-coordiante of point i
	'''
	from scitools.std import shape
	n = shape(points)[0] - 1 # shape(points) is a 2-tuple
	sum = 0
	for k in range(n+1):
		Lk = 1
		for i in range(n+1):
			if i != k:
				xi = points[i,0]
				xk = points[k,0]
				Lk *= (x - xi)/float(xk - xi)
		yk = points[k,1]
		sum += yk*Lk
	return sum

def _verify(points):
	epsilon = 1E-10
	n = shape(points)[0]
	c = False # our counter, False = no error, True = error
	for k in range(n):
		xk = points[k,0]
		yk = points[k,1]
		diff = abs(Lagrange(xk,points) - yk)
		if diff > epsilon:
			c = True
			print 'Error. Lagrange(xk, points) = %.2f, yk = %.2f' \
				% (xk, yk)
	if c == False:
		print 'abs(Lagrange(xk, points) - yk) < epsilon = %g' % epsilon, 			'for all points.'
	else:
		print 'abs(Lagrange(xk, points) - yk) is not less', 
		print 'than epsilon = %g' % epsilon,
		print 'for all points. The test has failed.'

	

if __name__ == '__main__':
	from scitools.std import *
	x = linspace(0, pi, 5)
	y = sin(x)
	points = array(zip(x,y))
	_verify(points)	
