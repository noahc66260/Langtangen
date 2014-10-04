from scitools.std import *

def f(x):
	condition = operator.and_(-3<=x, x < -1)
	r = where(condition, -x-2, x)
	condition = operator.and_(-1 <= x, x < 0)
	r = where(condition, x, r)
	condition = operator.and_(0 <= x, x < 1)
	r = where(condition, -x, r)
	condition = operator.and_(1 <= x, x <= 3)
	r = where(condition, x-2, r)
	return r

x = linspace(-3,3,100)
plot(x,f(x), title='Plot of the letter W', axis=[-3.1, 3.1, -1.1, 1.1])
raw_input('Press Enter to quit: ')
