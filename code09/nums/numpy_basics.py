import numpy as np



n1 = np.array([1,2,3,4])
n2 = np.array([5,6,7,8])

n3 = n1 + n2 

nx = np.concatenate([n1, n2])
print(nx)

exit()

arr = np.array([1,2,3,4])

print("mean: ", np.mean(arr))
print("median: ", np.median(arr))
print("max: ", np.max(arr))
print("min: ", np.min(arr))
print("sum: ", np.sum(arr))
print("std: ", np.std(arr))
print("var: ", np.var(arr))
exit()

zeros = np.zeros(6).reshape(2,3)
zeros = np.zeros((2,3))
print(zeros)
ones = np.ones(6)
print(ones)

# with range 
arr = np.linspace(1, 2, 10)

print(arr)

# change arr shape
arr = np.arange(6)
arr_reshape = arr.reshape(2, 3)
print(arr, arr_reshape)

####
v1 = [1, 2, 3]
print("v1", v1)

# multi dim
mat = np.array([[1,2,4], [3,4,3]])
print("mat: ")
print("shape: ", mat.shape)
print("dim: ", mat.ndim)

v1_arr = np.array(v1)
print("v1_arr: ",  v1_arr)