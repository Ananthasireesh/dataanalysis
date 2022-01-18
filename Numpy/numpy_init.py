import numpy as np
#intialise all zeroes matrix
""" we have a function called np.zeroes to do that"""
a = np.zeros((2,3,3))
print(a)

#intialise all 1's matrix
b = np.ones((2,3), dtype="int16")
print(b)

#intialise a matrix with same number 
c = np.full((2,3,3), 79)
print(c)

# if you want to create a matrix of any shape of other matrix we can pass that like below 
d = np.full_like(a,4)
print(d)

#intialise matrix of random decimal numbers 
e=np.random.rand(4,2)
print(e)

#intialise matrix with random integer values 
f = np.random.randint(7, size=(4,3))
print(f)

#intialize identity matrix 
g = np.identity(5)
print(g)