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

epsilon = 1E-10
T = 2*pi
t = linspace(epsilon, T-epsilon,500)
n = [1,3,20,200]
figure()
axis = [0, T, -1.2, 1.2]
hold('on')
for i in n:
	plot(t,S(t,i,T))
	legend('n = %d' % i)
plot(t,f(t,T))
legend('f(t)')
raw_input('Press Enter to quit: ')
