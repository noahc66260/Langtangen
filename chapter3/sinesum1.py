from math import sin, pi

def S(t,n,T):
    sum = 0
    for i in range(1,n+1):
        sum += 1./(2*i-1)*sin(2*(2*i-1)*pi*t/T)
    return sum*4/pi

def f(t, T):
    if 0 < t < T/2.0:
        x = 1
    elif t == T/2.0:
        x = 0
    elif T/2.0 < t < T:
        x = -1
    return x

n = [1,3,5,10,30,100]
alpha = [0.01, 0.25, 0.49]

print '    n    alpha    approximation     error'
for i in n:
    for j in alpha:
        approx = S(2*pi*j, i, 2*pi)
        error = abs(f(2*pi*j, 2*pi) - approx)
        print '%5d %8.2f %16f %9.2g' % (i,j,approx,error)
