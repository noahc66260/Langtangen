q = [0]*5
for i in range(5):
    q[i] = 10**(2*i)

q1 = [r**2 for r in [10**i for i in range(5)]]
print 'q1 =', q1
print 'q =', q

'''
python listcomp2for.py
q1 = [1, 100, 10000, 1000000, 100000000]
q = [1, 100, 10000, 1000000, 100000000]
'''
