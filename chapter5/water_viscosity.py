from scitools.std import *

A = 2.414 * 10**-5 # Pa s
B = 247.8 # K
C = 140 # K
mu = lambda T: A * 10**(float(B)/(T - C)) # viscosity of water
t = linspace(0, 100, 200) # in Celsius
c2k = lambda C: C + 273.15
y = mu(c2k(t)) # the lambda functions need not be vectorized 
plot(t,y)
ylabel('viscosity (Pa s)')
xlabel('temperature (C)')
raw_input('Press Enter to quit: ')

