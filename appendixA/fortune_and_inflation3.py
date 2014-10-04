from scitools.std import *

'''
So we plan to live on a fortune F
Our money is invested in a safe way to get us an apr of p in interest
Every year we plan to consume an amount c[n], where n is in years
We wish to model the development of our fortune x[n]
We wish to spend q percent of the return from our first year
	and account for inflation
'''

p = 6 # apr
q = 50 # percent
F = 2e5 # 200,000 dollars
N = 15 # years
I = 3 # percent inflation
t = 14 # capital gains tax

v = 7
x = zeros(N*v)
x.resize(v,N)
c = zeros(N*v)
c.resize(v,N)

x0 = F
c0 = float(p*300)/10**4 * F

x = transpose(x)
x[0] = x0
x = transpose(x)

c = transpose(c)
c[0] = linspace(0,c0,v)
c = transpose(c)

for k in range(v):
	for n in range(1,N):
		x[k][n] = x[k][n-1] + p/100. * x[k][n-1] - c[k][n-1]
		if n-2 >= 0 and x[k][n-1] >= x[k][n-2]:
			x[k][n] -= t/100.*(x[k][n-1] - x[k][n-2])
		c[k][n] = c[k][n-1] + I/100. * c[k][n-1]

figure()
title('Principal After n Years')
hold('on')
for i in range(v):
	plot(range(N), x[i])
	legend('c[0] = %.2f' % c[i][0])

raw_input('Press Enter to quit: ')

