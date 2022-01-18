import numpy as np
#create a 5*5 matrix with all 1's out side and 0's inside and 9 at center 
output = np.ones((5,5))
print(output)

replace = np.zeros((3,3))
replace[1,1] = 9
print(replace)
output[1:-1,1:-1] = replace
print(output)

#assigning is not copying in numpy arrays, its like pointing 
""" we can use copy function to do the stuff"""
a = np.array([1,2,3])