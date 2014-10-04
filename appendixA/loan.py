# Let's simulate a 100,000 mortgage over 15 years at 3.5% apr

L = 1e6 # loan amount
N = 12*15 # time of loan
p = 3.5 # apr

from scitools.std import *
x = zeros(N+1) # value of loan
y = zeros(N+1) # amount to be repaid

x0 = L
y0 = 0
x[0] = x0
y[0] = y0
for i in range(1,N):
	y[i] = p/(12*100.) * x[i-1] + float(L)/N
	x[i] = x[i-1] + p/(12*100.) * x[i-1] - y[i]

figure()
plot(range(N+1),x,'o',
	title='Value of Loan after n Months')

figure()
plot(range(N+1),y,'o',
	title='Amount to Repay per Month')
raw_input('Press Enter to quit: ')
