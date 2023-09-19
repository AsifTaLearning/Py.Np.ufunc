import numpy as np

# NumPy ufuncs
# Without ufunc, we can use Python's built-in zip() method

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  
  z.append(i + j)

print(z)

# With ufunc, we can use the add() function

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]

z = np.add(x, y)

print(z)


