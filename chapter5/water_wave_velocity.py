from scitools.std import *
def c(lambda_):
	'''
	Computes the wave speed of water surface waves 
	depending on the length lambda of the waves
	lambda_ must be in meters
	'''
	g = 9.81 # m/s**2
	s = 7.9*10**-2 # N/m, air-water surface tension
	rho = 1*10**6 # kg/m**3, density of water
	h = 50 # m, the water depth, which we have fixed
	from scitools.std import pi, tanh, sqrt
	return sqrt(g*lambda_/(2*pi)*(1 + s*4*pi**2/(rho*g*lambda_**2)) \
		* tanh(2*pi*h/lambda_))

# first we make a plot for small lambda
figure()
lambda_small = linspace(.001, .1, 100)
plot(lambda_small, c(lambda_small))
xlabel('lambda (m)')
ylabel('wave speed (m/s)')
axis([0.001, .1, 0, max(c(lambda_small))*1.1])

figure()
lambda_large = linspace(1,2000,100)
plot(lambda_large, c(lambda_large))
xlabel('lambda (m)')
ylabel('wave speed (m/s)')
axis([1,2000,0,max(c(lambda_large))*1.1])

raw_input('Press Enter to quit: ')

