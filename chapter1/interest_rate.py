# calculate interest rate
A = 1000 # euros, our principal
n = 3 # years
p = 5 # percent interest rate

money = A * (1 + p/100.)**n
print """After %d years with an apr of %d, our principal of %d euros 
has grown to %.2f euros.""" % (n, p, A, money)

'''
After 3 years with an apr of 5, our principal of 1000 euros 
has grown to 1157.63 euros.
'''
