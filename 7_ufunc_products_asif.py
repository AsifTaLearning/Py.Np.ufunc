import numpy as np

# Products

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)

print(x)

# Another example

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])

print(x)

# Product Over an Axis

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr = np.prod([arr1, arr2], axis=1)

print(newarr)

# Cummulative Product

arr = np.array([5, 6, 7, 8])

newarr = np.cumprod(arr)

print(newarr)





