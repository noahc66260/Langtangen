class Lagrange:
	'''
	Implementation of Lagrange's interpolation formula
	x is the point at which we make the interpolation estimate
	points is a set of n+1 2-tuples such that points[i,0]
	is the x-coordinate of point i and points[i,1] is the 
	y-coordiante of point i
	'''
	def __init__(self, points):
		self.points = points

	def __call__(self, x):
		points = self.points
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
			
	def verify(self):
		points = self.points
		epsilon = 1E-10
		n = shape(points)[0]
		c = False # our counter, False = no error, True = error
		for k in range(n):
			xk = points[k,0]
			yk = points[k,1]
			diff = abs(self.__call__(xk) - yk)
			if diff > epsilon:
				c = True
				print 'Error. Lagrange(xk, points) =',
				print '%.2f, yk = %.2f' % (xk, yk)
		if c == False:
			print 'abs(Lagrange(xk, points) - yk) < epsilon ='
			print '%g' % epsilon, 'for all points.'
		else:
			print 'abs(Lagrange(xk, points) - yk) is not less', 
			print 'than epsilon = %g' % epsilon,
			print 'for all points. The test has failed.'
	
	def graph(self, resolution=1001):
		'''
		graphs the Lagrange polynomial over self.points	
		'''
		#from scitools.std import *
		from scitools.std import zeros, linspace, plot, array
		points = self.points
		xlist = linspace(points[0,0], points[-1,0], resolution)
		ylist = self.__call__(xlist)
		plot(xlist, ylist)

	

if __name__ == '__main__':
	from scitools.std import *
	x = linspace(0, pi, 5)
	y = sin(x)
	points = array(zip(x,y))
	l = Lagrange(points)
	l.verify()
	
	figure()
	hold('on')
	axis([-.1, pi+.1, -.1, 1.1])
	for i in [5,10,20,55,70, 100]:
		x = linspace(0, pi, i)
		y = sin(x)
		points = array(zip(x,y))
		l = Lagrange(points)	
		l.graph()
		xlabel('x')
		ylabel('y')
		legend('n = %d' % i)
	raw_input('Press Enter to quit: ')
