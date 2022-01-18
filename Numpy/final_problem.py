from turtle import shape
import numpy as np
# declare 5*5 matrix using range
a = np.array(range(1,26),dtype="int16")
a.shape = (5,5)
print(a)

#we can also use reshape function with np.arrange
b = np.arange(1,26).reshape(5,5)
print(b)

""" get [[11 12]
         [16 17]]"""
print(b[2:4,0:2])

""" list indexing- cross of each thing"""
print(b[[0,1,2,3],[1,2,3,4]])

print(b[[0,3,4],3:])



