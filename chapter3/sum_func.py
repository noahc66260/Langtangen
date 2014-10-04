def s(M):
    '''computes the harmonic series up to, but not including, the Mth term'''
    sum = 0
    for i in range(1,M):
        sum += 1.0/i
    return sum

x = 1.0/1 + 1.0/2
print '1/1 + 1/2 = %.3f \ns(3) = %.3f' % (x,s(3))

'''
python sum_func.py
1/1 + 1/2 = 1.500 
s(3) = 1.500
'''
