from scitools.std import *
v0 = 10 # m/s
g = 9.81 # m/s**2
t = linspace(0,2.0*v0/g,50)
f = lambda t: v0*t - 0.5*g*t**2
y = f(t)

plot(t,y)
xlabel('time (s)')
ylabel('height (m)')
raw_input('Press Enter to quit: ')

