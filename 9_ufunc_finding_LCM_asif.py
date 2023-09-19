import numpy as np

# Finding LCM (Lowest Common Multiple)

num1 = 4
num2 = 6

x = np.lcm(num1, num2)

print(x)

# Finding LCM in Arrays

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)

# Another problem

arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x)




