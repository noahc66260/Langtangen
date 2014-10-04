import numpy

class Polynomial:
    def __init__(self, coefficients):
        from scitools.std import array
        self.coeff = array(coefficients)

    def __call__(self, x):
        """Evaluate the polynomial."""
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s

    def __add__(self, other):
        from scitools.std import copy
        # Start with the longest list and add in the other
        if len(self.coeff) > len(other.coeff):
            result_coeff = copy(self.coeff)  # copy!
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = copy(other.coeff) # copy!
            # Note: copying for arrays is different than that for lists
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)

    def __sub__(self, other):
        from scitools.std import copy
        other_copy = Polynomial(copy(other.coeff))
            # Not sure why but we can't say other.coeff
            # We need to say other.coeff[:]
            # I imagine the first is the reference, the second a copy
        for i in range(len(other_copy.coeff)):
            other_copy.coeff[i] = -other_copy.coeff[i]
        return self + other_copy

    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        M = len(c) - 1
        N = len(d) - 1
        result_coeff = numpy.zeros(M+N+1)
        for i in range(0, M+1):
            for j in range(0, N+1):
                result_coeff[i+j] += c[i]*d[j]
        return Polynomial(result_coeff)

    def differentiate(self):
        """Differentiate this polynomial in-place."""
        for i in range(1, len(self.coeff)):
            self.coeff[i-1] = i*self.coeff[i]
        self.coeff = self.coeff[:-1]

    def derivative(self):
        """Copy this polynomial and return its derivative."""
        dpdx = Polynomial(self.coeff[:])  # make a copy
        dpdx.differentiate()
        return dpdx

    def __str__(self):
        s = ''
        for i in range(0, len(self.coeff)):
            if self.coeff[i] != 0:
                s += ' + %g*x^%d' % (self.coeff[i], i)
        # Fix layout
        s = s.replace('+ -', '- ')
        s = s.replace('x^0', '1')
        s = s.replace(' 1*', ' ')
        s = s.replace('x^1 ', 'x ')
        s = s.replace('x^1', 'x')
        if s[0:3] == ' + ':  # remove initial +
            s = s[3:]
        if s[0:3] == ' - ':  # fix spaces for initial -
            s = '-' + s[3:]
        return s

    def simplestr(self):
        s = ''
        for i in range(0, len(self.coeff)):
            s += ' + %g*x^%d' % (self.coeff[i], i)
        return s


def _test():
    p1 = Polynomial([1, -1])
    p2 = Polynomial([0, 1, 0, 0, -6, -1])
    p3_add = p1 + p2
    print p1, '  +  ', p2, '  =  ', p3_add
    p3_sub = p1 - p2
    print p1, '  -  ', p2, '  =  ', p3_sub 
    p4 = p1*p2
    print p1, '  *  ', p2, '  =  ', p4
    print 'p2(3) =', p2(3)
    p5 = p2.derivative()
    print 'd/dx', p2, '  =  ', p5
    print 'd/dx', p2,
    p2.differentiate()
    print '  =  ', p5
    p4 = p2.derivative()
    print 'd/dx', p2, '  =  ', p4

if __name__ == '__main__':
    _test()

'''
python Polynomial_array1.py
1 - x   +   x - 6*x^4 - x^5   =   1 - 6*x^4 - x^5
1 - x   -   x - 6*x^4 - x^5   =   1 - 2*x + 6*x^4 + x^5
1 - x   *   x - 6*x^4 - x^5   =   x - x^2 - 6*x^4 + 5*x^5 + x^6
p2(3) = -726
d/dx x - 6*x^4 - x^5   =   1 - 24*x^3 - 5*x^4
d/dx x - 6*x^4 - x^5   =   1 - 24*x^3 - 5*x^4
d/dx 1 - 24*x^3 - 5*x^4   =   -72*x^2 - 20*x^3
'''
