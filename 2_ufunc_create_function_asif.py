from sympy import var
var('function inputs outputs')

import numpy as np

# Create Your Own ufunc
# How To Create Your Own ufunc

function # - the name of the function.
inputs # - the number of input arguments (arrays).
outputs # - the number of output arrays.

def myadd(x, y):
  
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

# Check if a Function is a ufunc

print(type(np.add))

# Another example

print(type(np.concatenate))

# Another example

if type(np.add) == np.ufunc:
  
  print('add is ufunc')

else:
  
  print('add is not ufunc')




