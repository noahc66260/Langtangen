# odd.py prints odd numbers from 1 to n
n = 20
i = 1
list = []
while i <= n:
    list.append(i)
    i = i + 2
for j in range(len(list)):
    print list[j]

'''
python odd_list2.py
1
3
5
7
9
11
13
15
17
19
'''
