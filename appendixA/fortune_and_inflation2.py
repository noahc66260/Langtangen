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
t = 28 # tax percent

x_taxes = zeros(N)
x_notaxes = zeros(N)
c = zeros(N)

x0 = F
c0 = float(p*q)/10**4 * F
x_taxes[0] = x0
x_notaxes[0] = x0
c[0] = c0
for n in range(1,N):
	x_taxes[n] = x_taxes[n-1] + p/100. * x_taxes[n-1] - c[n-1]
	x_notaxes[n] = x_notaxes[n-1] + p/100. * x_notaxes[n-1] - c[n-1]
	if n-2 >= 0 and x_taxes[n-1] >= x_taxes[n-2]:
		x_taxes[n] -= t/100.*(x_taxes[n-1] - x_taxes[n-2])
	c[n] = c[n-1] + I/100. * c[n-1]

figure()
plot(range(N), x_taxes,
	range(N), x_notaxes,
	legend=['Taxes', 'No Taxes'],
	title='Principal Value after n Years')

raw_input('Press Enter to quit: ')

