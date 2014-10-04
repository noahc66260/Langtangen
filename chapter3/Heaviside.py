def Heaviside(x):
	'''
	Computes the Heaviside funtion
	'''
	if x < 0:
		return 0
	else:
		return 1

for i in range(-1,2):
	print 'Heaviside(%d) = %d' % (i, Heaviside(i))

'''
python Heaviside.py
Heaviside(-1) = 0
Heaviside(0) = 1
Heaviside(1) = 1
'''
