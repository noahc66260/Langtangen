from scitools.std import *

def S(t,n,T):
    sum = 0
    for i in range(1,n+1):
        sum += 1./(2*i-1)*sin(2*(2*i-1)*pi*t/T)
    return sum*4/pi

def f(t, T):
    import operator
    condition = operator.and_(0 < t, t <= T/2.0)
    x = where(condition,1,t)
    x = where(t == T/2.0, 0, x)
    condition = operator.and_(T/2.0 < t, t < T)
    x = where(condition, -1, x)
    return x

import glob, os
for filename in glob.glob('tmp*.png'):
	os.remove(filename)


epsilon = 1E-10
T = 2*pi
t = linspace(epsilon, T-epsilon,500)
n = array(range(1,300,6))
counter = 0
y = f(t,T) # for plotting our function
for i in n:
	plot(t,S(t,i,T),
		t, y,
		legend=['n = %d' % i, 'f(t,T)'],
		axis=[-.1,T+.1,-1.5,1.5],
		xlabel='x',
		ylabel='y',
		savefig='tmp%04d.png' % counter)
	counter += 1
movie('tmp*.png', encoder='convert', fps=3, output_file='exercise_5.30.gif')
