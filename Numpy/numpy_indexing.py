import numpy as np 
a = np.array(
    [[1,2,3,4,5,6,7],
     [8,9,10,11,12,13,14]]
)
#print array 
print("Array is:", a)
#get shape of the array 
print("Rows and columns in Array A is:", a.shape)

#accessing a specific element from array [r,c]
print("2nd element of 1st row:",a[0,1])
print("6th element of 2st row:",a[1,5])
#we can also use negitive indices as we use in lists 
print("5th element of 2st row:",a[1,-3])

#Get specific row and all columns 
print("first row of the matrix is:",a[0,:])

#get specfic columns 
print("3rd column in array is:", a[:,2])

#get range of elements in a row 
print("3rd to 6th columns in first row in array A is:",a[0,2:6])
# we can also introduce a step size 
print("1st element into 6th element in steps of 2:", a[0,:6:2])

#change a specific element 
#assign 3rd element in 1st row as 20
a[0,2] = 20
print(a)

#assign 2nd column with 20,90
a[:,1] = [20,90]
print(a)

#assign 1st column with [10,20,30,40,50,60,70]
a[0,:] = [10,20,30,40,50,60,70]
print(a)

b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("Array B is:", b)

# get 1st arrays 2nd row 2nd element 
print("First arrays 2nd rows 2nd column is:",b[0,1,1])

#get 2nd arrays 1st row all columns
print("All columns of 2nd matrix, 2nd row is:",b[1,1,:])

#get all the matrices 2nd rows with all columns
print(" All matrices, All columns of 2nd matrix, 2nd row is:",b[:,1,:])