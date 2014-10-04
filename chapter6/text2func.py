from scitools.std import * # this might be necessary since our fn sucks

def create_function(s):
	'''
	returns a string function object from a string
	of the form
	s = <expression> is function of <list1> with paramter <list2>
	More details are from Langtangen exercise 6.21 pg 301
	'''
	from scitools.StringFunction import StringFunction

	expression = s.split('is a function of')[0].strip()
	list1 = s.split('is a function of')[1].\
		split('with parameter')[0].strip()
	if 'with parameter' in s:
		list2 = s.split('with parameter')[-1].strip()
	f = eval('StringFunction("%s", ' % expression + \
			'independent_variables=["%s"],%s)' % \
			 (list1, list2))
	return f

def _test():
	s = 'sin(a*x) is a function of x with parameter a=1'
	f = create_function(s)
	from math import pi, sin
	print s
	print 'f(0) = %f' % f(0)
	print 'f(pi/2) = %f' % f(pi/2.)
	print 'f(pi) = %f' % f(pi)

if __name__ == '__main__':
	_test()

'''
python text2func.py
sin(a*x) is a function of x with parameter a=1
f(0) = 0.000000
f(pi/2) = 1.000000
f(pi) = 0.000000
'''
