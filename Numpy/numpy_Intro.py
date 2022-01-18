# import numpy library , give it alias name for it as np
import numpy as np 

#intialise an sigle array
a = np.array([1,2,3])
print("1-D Array:",a)

#intialise a 2d array of floats 
b = np.array([[2.0,3.7,7.2],[5.0,7.0,8.3]])
print("2-D Array:",b)
""" you can create 100s of dimension arrays by nesting lists inside lists"""

#get dimension of numpy arrays 
print("dimension of Array A is:", a.ndim)

#get shape of numpy arrys, returns rows and columns 
print("Dimension of Array B is:", b.shape)

#get type 
print("Data type of Array A is:", a.dtype)

# we can also provide in what datatype should our array get stored, by giving dtype param
c = np.array([1,2,3], dtype="int16")
print("Data type of Array C is:", c.dtype)

# we can get size of item in array by using itemsize 
print("size of array C is:", c.itemsize)

# we can get number of items array by using size
print("size of array C is:", c.size)

#to get todatl size we can multiply size itemsize with tota number of elements 
# we can get number of items array by using size
print("total size of array C is:", c.size * c.itemsize)