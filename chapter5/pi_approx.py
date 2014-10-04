from math import sin, cos, pi

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

print '    N    approximation       error'
for k in range(2,11):
    N = 2**k
    x = [1./2*cos(2.*pi*i/N) for i in range(N+1)]
    y = [1./2*sin(2.*pi*i/N) for i in range(N+1)]
    approx = pathlength(x,y)
    print '%5d %16f %11.2e' % (N, approx, abs(pi - approx))

'''
python pi_approx.py
    N    approximation       error
    4         2.828427    3.13e-01
    8         3.061467    8.01e-02
   16         3.121445    2.01e-02
   32         3.136548    5.04e-03
   64         3.140331    1.26e-03
  128         3.141277    3.15e-04
  256         3.141514    7.89e-05
  512         3.141573    1.97e-05
 1024         3.141588    4.93e-06
'''
