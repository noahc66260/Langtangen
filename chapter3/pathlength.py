def pathlength(x,y):
    '''
    Computes the path length of the points (x0,y0), (x1,y1), ..., (xn,yn)
    x is a list of real numbers
    y is a list of real numbers
    len(x) and len(y) must be equal
    '''

    from math import sqrt
    sum = 0
    n = len(x)
    for i in range(1,n):
        sum += sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2)
    return sum

x = [1,2,1,1]
y = [1,1,2,1]
L = pathlength(x,y)
print 'for x =', x, 'and y =', y, 'our path length is 3.41'
print 'our function gives us pathlength(x,y) = %.2f' % (L)

'''
python pathlength.py
for x = [1, 2, 1, 1] and y = [1, 1, 2, 1] our path length is 3.41
our function gives us pathlength(x,y) = 3.41
'''
