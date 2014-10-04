class Line:
	def __init__(self, p1, p2):
		if isinstance(p1, (tuple, list)) and \
		   isinstance(p2, (tuple, list)):
			self.p1 = p1
			self.p2 = p2
			self.slope = None
			self.intercept = None
		elif isinstance(p1, (tuple, list)) and \
		     isinstance(p2, (float, int)):
			self.p1 = p1
			self.p2 = None
			self.slope = p2
			self.intercept = None
		elif isinstance(p1, (float, int)) and \
		     isinstance(p2, (float, int)):
			self.p1 = None
			self.p2 = None
			self.slope = p1
			self.intercept = p2
		else:
			raise TypeError('Arguments are not valid')
	def value(self, x):
		if self.p1 is not None:
			x1, y1 = self.p1[0], self.p1[1]
		if self.slope is None:
			x2, y2 = self.p2[0], self.p2[1]
			self.slope = (y2 - y1)/float(x2 - x1)
		if self.intercept is None:
			self.intercept = y1 - self.slope*x1
		m = self.slope
		b = self.intercept
		return m*x + b

def _test():
	line = Line((0,-1), (2,4))
	print line.value(0.5), line.value(0), line.value(1)

	line = Line((0,-1), 5./2)
	print line.value(0.5), line.value(0), line.value(1)

	line = Line(5./2, -1)
	print line.value(0.5), line.value(0), line.value(1)

if __name__ == '__main__':
	_test()

'''
python Line2.py
0.25 -1.0 1.5
0.25 -1.0 1.5
0.25 -1.0 1.5
'''
