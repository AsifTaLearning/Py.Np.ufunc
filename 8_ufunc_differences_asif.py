import numpy as np

# Differences

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)

print(newarr)

# Another problem

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr, n=2)

print(newarr)





