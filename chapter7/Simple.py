class Simple:
	def __init__(self, i):
		self.i = i

	def double(self):
		i = self.i
		self.i = i + i

def _test():
	s1 = Simple(4)
	for i in range(4):
		s1.double()
	print s1.i

	s2 = Simple('Hello')
	s2.double(); s2.double()
	print s2.i
	s2.i = 100
	print s2.i

if __name__ == '__main__':
	_test()


'''
python Simple.py
64
HelloHelloHelloHello
100
'''
