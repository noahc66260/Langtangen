# our first snippet, works fine
t1 = {}
t1[0] = -5
t1[1] = 10.5

# our second snippet, doesn't work
# t2 = []
# t2[0] = -5
# t2[1] = 10.5

# Dictionary objects behave differently than lists
# In a dictionary we can create a new node without previously allocating
# space. This is not so in a list. To fix the code we can write

t2 = [0]*2 # now our array has a length of 2
t2[0] = -5
t2[1] = 10.5

