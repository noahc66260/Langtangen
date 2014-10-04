def diff(poly):
	'''
	Calculates and returns the polynomial representation
	of the derivative of poly
	poly is a dictionary object whose entries i
	are integers which represent the nonzero
	coefficients of the ith power of the variable.
	'''
	d = {}
	for exp in poly:
		if exp == 0:
			continue
		d[exp-1] = exp*poly[exp]
	return d

p = {0: -3, 3: 2, 5: -1} 	# -3 + 2*x**3 + -1*x**5
dp = diff(p)			# should be 6*x**2 -5*x**4
print dp

'''
python poly_diff.py
{2: 6, 4: -5}
'''
