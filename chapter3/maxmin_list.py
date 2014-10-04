def max(a):
	''' 
	Returns the largest element in list a
	'''
	if len(a) == 0:
		return None
	max_elem = a[0]
	for i in range(1,len(a)):
		if a[i] > max_elem:
			max_elem = a[i]
	return max_elem

def min(a):
	''' 
	Returns the smallest element in list a
	'''
	if len(a) == 0:
		return None
	min_elem = a[0]
	for i in range(1,len(a)):
		if a[i] < min_elem:
			min_elem = a[i]
	return min_elem

a = [1,3,6,-7,4,32,16,-8]
print 'a =', a
print 'min(a) = ', min(a)
print 'max(a) = ', max(a)

'''
python maxmin_list.py
a = [1, 3, 6, -7, 4, 32, 16, -8]
min(a) =  -8
max(a) =  32
'''
