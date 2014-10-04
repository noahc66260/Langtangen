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

x = zeros(N)
c = zeros(N)

x0 = F
c0 = float(p*q)/10**4 * F
x[0] = x0
c[0] = c0
for n in range(1,N):
	x[n] = x[n-1] + p/100. * x[n-1] - c[n-1]
	c[n] = c[n-1] + I/100. * c[n-1]

figure()
plot(range(N), x,
	title='Principal Value after n Years')

figure()
plot(range(N), c,
	title='Dollars to spend after n Years, Accounting for Inflation')
raw_input('Press Enter to quit: ')

