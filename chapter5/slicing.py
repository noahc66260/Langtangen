# I have changed the list w so that printing is neater. If We were to have
# w = 0, 0.1, 0.2, ..., 3.0, then we would have problems resulting from
# binary representation so that some numbers are represented as
# x.x000000000002 rather than x.x
w = range(0,31)
print 'w[:] =', w[:]
print 'w[:-2] =', w[:-2]
print 'w[::5] =', w[::5]
print 'w[2:-2:6] =', w[2:-2:6]
