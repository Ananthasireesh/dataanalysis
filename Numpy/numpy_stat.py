import numpy as np 
# Numpy can help us getting so many statistics from data 
#intialise matrix with random integer values 
a = np.random.randint(7, size=(4,3))
print(a)

#min of numpy array 
print("min of numpy array:", np.min(a, axis=1))

#max of numpy array
print("max of numpy array:", np.max(a))