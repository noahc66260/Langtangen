n = 3
for i in range(-1,n):
    if i != 0:
        print i

for i in range(1,13,2*n):
    for j in range(n):
        print i,j

for i in range(1, n+1):
    for j in range(i):
        if j:
            print i,j

for i in range(1,13,2*n):
    for j in range(0,i,2):
        for k in range(2,j,1):
            b = i > j > k
            if b:
                print i, j, k
