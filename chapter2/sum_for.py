# computes \sum_{k = 1}^M \frac{1}{k}

s = 0; k = 1; M = 100
for k in range(1,M+1):
    s += 1.0/k
print s

'''
python sum_for.py
5.18737751764
'''
