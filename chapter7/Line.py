class Line:
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def value(self, x):
		x1, y1 = self.p1[0], self.p1[1]
		x2, y2 = self.p2[0], self.p2[1]
		m = (y2 - y1)/float(x2 - x1)
		b = y2 - m*x2
		return m*x + b

def _test():
	line = Line((0,-1), (2,4))
	print line.value(0.5), line.value(0), line.value(1)

if __name__ == '__main__':
	_test()

'''
python Line.py
0.25 -1.0 1.5
'''
