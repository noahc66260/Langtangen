# computes \sum_{k = 1}^M \frac{1}{k}

s = 0; k = 1; M = 100
while k <= M:
    s += 1.0/k
    k += 1
print s
