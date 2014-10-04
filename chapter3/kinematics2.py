def kinematics(x, y, t, dt = 1E-4):
    '''
    Using the functions x and y  kinematics() returns the position,
    velocity, and acceleration at time t using the appoximation
    vx = (x(t+dt)-x(t-dt))/(2*dt)
    vy = (y(t+dt)-y(t-dt))/(2*dt) 
    ax = (x(t+dt)-2x(t)+x(t-dt))/(dt**2)
    ax = (y(t+dt)-2y(t)+y(t-dt))/(dt**2)

    The function returns three two-tuples
    (x(t),y(t)),(v(x),v(y)),(a(x),a(y))
    '''

    vx = (x(t+dt)-x(t-dt))/(2.0*dt)                     
    vy = (y(t+dt)-y(t-dt))/(2.0*dt)    
    ax = (x(t+dt)-2*x(t)+x(t-dt))/float(dt**2)
    ay = (y(t+dt)-2*y(t)+y(t-dt))/float(dt**2)  
    posx = x(t)
    posy = y(t)

    return (posx,posy), (vx,vy), (ax,ay)

from math import cos, pi, sin
R = 1
w = 2*pi
x = lambda t: R*cos(w*t)
y = lambda t: R*sin(w*t)
(posx, posy), (vx,vy), (ax,ay) = kinematics(x, y, t = 1, dt = 1E-5)
print '''for the functions x = Rcos(wt), y = Rsin(wt) we have...
x(t) = %f
y(t) = %f
v(x(t)) = %f
v(y(t)) = %f 
a(x(t)) = %f
a(y(t)) = %f''' % (posx, posy, vx, vy, ax, ay)

'''
python kinematics2.py
for the functions x = Rcos(wt), y = Rsin(wt) we have...
x(t) = 1.000000
y(t) = -0.000000
v(x(t)) = 0.000000
v(y(t)) = 6.283185 
a(x(t)) = -39.478419
a(y(t)) = 0.000009
'''
