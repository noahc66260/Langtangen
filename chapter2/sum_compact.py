import time
M = 10**7
e0 = time.time()
print sum([1.0/k for k in range(1, M+1, 1)])
elapsed_time = time.time() - e0
print 'elapsed time for sum([1.0/k for k in range(1, M+1,1)]) = %f' % \
    (elapsed_time)
print
e0 = time.time()
print sum(1.0/k for k in xrange(1, M+1,1))
elapsed_time = time.time() - e0
print 'elapsed time for sum(1.0/k for k in xrange(1, M+1,1)) = %f' % \
    (elapsed_time)

'''
python sum_compact.py
16.6953113659
elapsed time for sum([1.0/k for k in range(1, M+1,1)]) = 5.918173

16.6953113659
elapsed time for sum(1.0/k for k in xrange(1, M+1,1)) = 3.226310
'''
