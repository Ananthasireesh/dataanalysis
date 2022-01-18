import numpy as np 
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
#convert this matrix to 8 * 1
after = before.reshape((8,1))
print("After reshaping:", after)

#as long as if it has same number of numbers that you reshape you can reshapr it to any kind 

""" vertically stacking arrays"""
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

v3 = np.vstack([v1,v2])
print("vertically stacking the arrays:", v3)

""" Horizantally stacking arrays"""
h1 = np.ones((2,4))
h2 = np.zeros((2,2))
h3 = np.hstack([h1,h2])
print("horizantally stacking the arrays:", h3)


