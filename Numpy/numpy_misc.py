import numpy as np
#load the data from text file 
#np.genfromtext('data.txt', delimiter=",")
"""Boolean Masking and Advanced indexing"""
a = np.random.randint(49, size=(4,3))
print(a)
print(a > 20)
print(a[a>20])

"""we can also index with a list in numpy, we can get specific elements using list index"""
b = np.array([1,2,3,4,5,6,7,8,9]) 
print("2nd, 4th and 9th element in array are", b[[1,3,8]])

# if you want to check which columns have a specific data we can use this below statement 
# to check if any one of element is greater than 20 in column 
print(np.any(a >20, axis=0))
#to check if all elements in a row is less than 20
print(np.all(a < 20, axis=1))
#to check which elements are less than 20 and greater than 10
print("elements that ae less than 20 and greater than 10:", a[((a<20) & (a>10))])


