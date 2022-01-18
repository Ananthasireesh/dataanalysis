import numpy as np
#in linear algebra, we dont do element wise operations where as we do matric multiplications a lot

a = np.ones((2,3))
b = np.full((3,2),3)
""" in matrix multiplication we should have number of rows in first matrix 
    equal to 2nd matrix columns """
#direct multiplication Doesn't work for matrices 
#print("multiplication of two matrices is:", a*b)

#matrix multiplication on matrices
print("multiplication of two matrices is:", np.matmul(a,b))

#find determinent of a matrix 
c = np.identity(2)
print("determinent of identity matrix is:",np.linalg.det(c))

""" for more stuff on linear algebra functions 
 a) Determinent 
 b) Trace 
 c) singular vector decomposition 
 e) Eigen values 
 f) Matrix norm 
 g) Inverse 
 ....etc
we can refer https://numpy.org/doc/stable/reference/routines.linalg.html"""

