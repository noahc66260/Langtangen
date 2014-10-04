# since it is not specified, I set R = 2
class VelocityProfile:
	def __init__(self, beta, mu0, r, R):
		self.beta = beta
		self.mu0 = mu0
		self.r = r
		self.R = R
	
	def __call__(self, n):
		beta = self.beta
		mu0 = self.mu0
		r = self.r
		R = self.R
		v = (beta/(2.*mu0))**(1./n) * \
			n/(n+1.)*(R**(1+1./n) - r**(1+1./n))
		return v

def _test():
	beta = 50
	mu0 = 1
	r = 1
	R = 2
	v = VelocityProfile(beta, mu0, r, R)
	from Central import Central
	c = Central(v, h=1E-5)
	n = 1
	dvdn_approx = c(n)
	def dvdn_exact(beta, mu0, r, R, n):
		from scitools.std import log
		term1 = (beta / (2.*mu0))**(1./n)
		term2 = n/(n+1.)
		term3 = (R**(1+1./n) - r**(1+1./n))
		sum = 0
		sum += -1./n**2 * log(beta/(2.*mu0)) * \
			 term1 * term2 * term3
		sum += 1./(n+1)**2 * term1 * term3
		sum += (-1./n**2) * \
			(R**(1+1./n)*log(R) - r**(1+1./n)*log(r))\
			 * term1 * term2
		return sum

	print 'for n = %.1f' % n
	print 'dv/dn exact:  %10g' % (dvdn_exact(beta, mu0, r, R, n))
	print 'dv/dn approx: %10g' % (dvdn_approx)

if __name__ == '__main__':
	_test()

'''
python VelocityProfile_deriv.py
for n = 1.0
dv/dn exact:    -136.615
dv/dn approx:   -136.615
'''
