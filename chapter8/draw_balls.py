import random
import copy
random.seed(1)

hat = ['red' for i in range(5)] \
	+ ['yellow' for i in range(5)] \
	+ ['green' for i in range(3)] \
	+ ['brown' for i in range(7)]

N = 10**3

def option1(pick, n):
	'''
	Returns the money won (0 if not) if option 1 is picked
	for a given selection and value of n
	'''
	from numpy import array, sum
	if sum(array(pick) == 'red') == 3:
		return 60
	else:
		return 0

def option2(pick, n):
	'''
	Returns the money won (0 if not) if option 2 is picked
	for a given selection and value of n
	'''
	from numpy import array, sum, sqrt
	if sum(array(pick) == 'brown') >= 3:
		return 7 + 5*sqrt(n)
	else:
		return 0

def option3(pick, n):
	'''
	Returns the money won (0 if not) if option 3 is picked
	for a given selection and value of n
	'''
	from numpy import array, sum
	pick = array(pick)
	if sum(pick == 'brown') == 1 \
	   and sum(pick == 'yellow') == 1:
		return n**3 - 26
	else:
		return 0

def option4(pick, n):
	'''
	Returns the money won (0 if not) if option 4 is picked
	for a given selection and value of n
	'''
	from numpy import array, sum
	pick = array(pick)
	if sum(pick == 'brown') >= 1 \
	   and sum(pick == 'yellow') >= 1 \
	   and sum(pick == 'red') >= 1 \
	   and sum(pick == 'green') >= 1:
		return 23
	else:
		return 0

option = [option1, option2, option3, option4]
print '%15s %10s %10s %10s %20s ' \
	 % ('Option Number', 'N', 'n', 'P(win)', 'net income per play')
for j in range(len(option)):
	print '%15i' % (j+1)
	for n in range(4,11):
		money = 0
		successes = 0
		for i in range(N):
			money -= 2*n
			random.shuffle(hat)
			pick = hat[:n]
			winnings = option[j](pick, n)
			if abs(winnings) > 10**-10:
				successes += 1
			money += winnings
		pwin = float(successes)/N
		#print 'option %d, successes = %d, N = %g, pwin = %f' \
		#	% (j+1, successes, N, pwin)
		net_income = float(money)/N
		print '%15s %10g %10i %10f %20f' \
			% ('', N, n, pwin, net_income) 

'''
python draw_balls.py
  Option Number          N          n     P(win)  net income per play 
              1
                      1000          4   0.030000            -6.200000
                      1000          5   0.064000            -6.160000
                      1000          6   0.129000            -4.260000
                      1000          7   0.169000            -3.860000
                      1000          8   0.224000            -2.560000
                      1000          9   0.307000             0.420000
                      1000         10   0.359000             1.540000
              2
                      1000          4   0.088000            -6.504000
                      1000          5   0.202000            -6.327571
                      1000          6   0.345000            -5.359630
                      1000          7   0.476000            -4.371112
                      1000          8   0.644000            -2.384465
                      1000          9   0.723000            -2.094000
                      1000         10   0.860000            -0.382206
              3
                      1000          4   0.184000            -1.008000
                      1000          5   0.122000             2.078000
                      1000          6   0.047000            -3.070000
                      1000          7   0.020000            -7.660000
                      1000          8   0.008000           -12.112000
                      1000          9   0.001000           -17.297000
                      1000         10   0.000000           -20.000000
              4
                      1000          4   0.111000            -5.447000
                      1000          5   0.255000            -4.135000
                      1000          6   0.455000            -1.535000
                      1000          7   0.594000            -0.338000
                      1000          8   0.719000             0.537000
                      1000          9   0.794000             0.262000
                      1000         10   0.875000             0.125000
'''	
