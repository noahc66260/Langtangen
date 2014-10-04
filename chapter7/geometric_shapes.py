class Triangle1:
	def __init__(self, width, height, position=(0,0)):
		self.width = width
		self.height = height
		self.position = position # should be a 2-tuple

	def area(self):
		w = self.width
		h = self.height
		return 1./2*w*h

	def circumference(self):
		from math import sqrt
		w = self.width
		h = self.height
		c = w + h + sqrt(w**2 + h**2)
		return c

class Triangle2:
	def __init__(self, v1, v2, v3):
		self.v1 = v1
		self.v2 = v2
		self.v3 = v3

	def area(self):
		from scitools.std import array, sqrt
		from numpy import dot, cross
		v1 = array(self.v1)
		v2 = array(self.v2)
		v3 = array(self.v3)
		v2 = v2 - v1
		v3 = v3 - v1 
		v1 = v1 - v1 # now v1 is at the origin
	
		return abs(cross(v2,v3))/2.0

	def circumference(self):
		from scitools.std import array, sqrt
		from numpy import dot
		v1 = array(self.v1)
		v2 = array(self.v2)
		v3 = array(self.v3)
		v2 = v2 - v1
		v3 = v3 - v1 #now v1 is at the origin
		v1 = v1 - v1
	
		side1 = sqrt(dot(v2,v2))
		side2 = sqrt(dot(v3,v3))
		v1 = v1 - v2
		v3 = v3 - v2
		v2 = v2 - v2 #now v2 is at the origin
	
		side3 = sqrt(dot(v3, v3))
		return side1 + side2 + side3

def _test():
	t1 = Triangle1(width = 4.0, height = 3.0)
	print t1.area() # should be 6.0
	print t1.circumference() # should be 12.0

	t2 = Triangle2(v1 = [5,5], v2 = [9,5], v3 = [5,8])
	t3 = Triangle2(v1 = [5,5], v2 = [5,8], v3 = [9,5])
	print t2.area() # should be 6.0
	print t2.circumference() # should be 12.0
	print t3.area() # should be 6.0
	print t3.circumference() # should be 12.0

if __name__ == '__main__':
	_test()

'''
python geometric_shapes.py
6.0
12.0
6.0
12.0
6.0
12.0
'''
