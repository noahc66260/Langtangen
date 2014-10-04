class HelloWorld:
	def __str__(self):
		return 'Hello, World!'

def _test():
	a = HelloWorld()
	print a

if __name__ == '__main__':
	_test()

'''
python HelloWorld.py
Hello, World!
'''
