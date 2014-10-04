def fact(n):
    prod = 1
    if n != 1 and n != 0:
        while n > 1:
            prod *= n
            n = n-1
    return prod

print 'Our function computes 4! = %d' % (fact(4))
from math import factorial
print 'As a check, 4! = %d' % (factorial(4))

'''
python fact.py
Our function computes 4! = 24
As a check, 4! = 24
'''
