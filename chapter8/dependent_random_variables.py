from scitools.std import *

N = 80
s1 = ''
for i in range(N):
	s1 += str(random.randint(0,2))
print 'Our random independent sequence'
print s1

p = [0.5, 0.8, 0.9]
for j in p:
	last_digit = random.randint(0,2)
	s2 = ''
	for i in range(N):
		if random.uniform(0,1) < j:
			if last_digit == 0:
				new_digit = 1
			elif last_digit == 1:
				new_digit = 0
		else:
			new_digit = last_digit
		
		s2 += str(new_digit)
		last_digit = new_digit

	print 'Dependent sequence, p = %.1f' % j	
	print s2

'''
python dependent_random_variables.py
Our random independent sequence
00110111111110110000001100111111110100110111110011101010111010100110100011001110
Dependent sequence, p = 0.5
11011111100101011110110100110010011110101001011010011010111000001010010011101100
Dependent sequence, p = 0.8
10101011010101100101001010101101001010101001010010101000010110100100101010100101
Dependent sequence, p = 0.9
01010110010110101010101010110101010101010101010101010010110101010111010101101010'''
