from binomial_distribution import binomial

print '''The probability of getting two heads from five coin flips
is %.2f%%''' % (100*binomial(2,5,.5))
print '''The probability of getting four ones in a row when throwing
a die is %.2f%%''' % (100*binomial(4,4,1./6))
print '''The probability of a skier experiencing a ski break during
five world competitions is %.2f%%''' % ((1-binomial(0,5,1./120))*100)

'''
python binomial_problems.pyThe probability of getting two heads from five coin flips
is 31.25%
The probability of getting four ones in a row when throwing
a die is 0.08%
The probability of a skier experiencing a ski break during
five world competitions is 4.10%
'''
