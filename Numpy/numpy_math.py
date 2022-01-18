""" Numpy allows us greatly to work on mathematical operations 
    majorly element wise operations are used a lot with numpy"""

import numpy as np

a = np.array([1,2,3,4])

#element wise addition 
print(a+2)
#element wise subtraction
print(a-2)
#element wise multiplication
print(a*2)
#element wise division
print(a/2)

b = np.array([5,6,7,8])
#element wise addition 
print(a+b)
#element wise subtraction
print(b-a)
#element wise multiplication
print(a*b)
#element wise division
print(b/a)

""" for more numpy stuff we can look at the docs of numpy 
    https://numpy.org/doc/stable/reference/routines.math.html"""