# first we make the dictionary
poly_dict = {0: -1./2, 100: 2}

# and now the list
poly_list = [0]*101
poly_list[0] = -1./2
poly_list[100] = 2

x = 1.05
sum1 = 0
for exp in poly_dict:
	sum1 += poly_dict[exp]*x**exp

sum2 = 0
for exp in range(len(poly_list)):
	sum2+= poly_list[exp]*x**exp

print 'for x = 1.05...'
print 'Using a dictionary we get -1/2 + 2*x**100 =', sum1
print 'Using a list we get 1/2 + 2*x*100 =', sum2

'''
python poly_repr.py
for x = 1.05...
Using a dictionary we get -1/2 + 2*x**100 = 262.502515693
Using a list we get 1/2 + 2*x*100 = 262.502515693
'''
