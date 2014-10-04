def kinematics(x, t, dt = 1E-4):
    '''
    Using the function x, kinematics() returns the position,
    velocity, and acceleration at time t using the appoximation
    v = (x(t+dt)-x(t-dt))/(2*dt)
    a = (x(t+dt)-2x(t)+x(t-dt))/(dt**2)
    '''
    
    v = (x(t+dt)-x(t-dt))/(2.0*dt)
    a = (x(t+dt)-2*x(t)+x(t-dt))/(float(dt**2))
    pos = x(t)

    return pos, v, a

from math import exp
x = lambda t: exp(-(t-4)**2)
pos, v, a = kinematics(x, t = 5, dt = 1E-5)
print '''for the function exp(-(t-4)**2) we have...
x(t) = %f
v(t) = %f 
a(t) = %f''' % (pos, v, a)

'''
python kinematics1.py
for the function exp(-(t-4)**2) we have...
x(t) = 0.367879
v(t) = -0.735759 
a(t) = 0.735759
'''
