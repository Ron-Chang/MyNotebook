# Basic Numpy 2  

## What is NumPy?
NumPy can process image, signal and liner algebra, etc.

## Why we need it?
Numpy takes less than 0.03 seconds to process 1000 by 1000 matrix multiply, but it will take more than 10 minutes to process with standard list. 
If we are going to process a vector operation, it's better to use numpy to saving the time.


```python
import numpy as np


foo = [i for i in range(1,5+1)]
# foo = [1,2,3,4,5]

# na stand for numpy array
na = np.array(foo)
# type(na) = <class 'numpy.ndarray'>

print(foo)
# [1, 2, 3, 4, 5]
print(na)
# [1 2 3 4 5]

########### List ###########
list_1 = foo + [6]
# [1, 2, 3, 4, 5, 6]
list_1.append(7)
# [1, 2, 3, 4, 5, 6, 7]
dual_list = list_1 + list_1
# It equals dual_list = list_1 * 2
# [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]
"""
# How can we represent vector addition through list method

dual_list = []
for i in list_1:
    dual_list = i + i

# or

dual_list = [i+i for i in list_1]

"""

# pow_list = list_1**2
# TypeError: unsupported operand type(s) for **


########### Array ###########
array_1 = na + [4]
# [1+4, 2+4, 3+4, 4+4, 5+4]
print(list_2)
# [5, 6, 7, 8, 9]

# array_1.append(4)
# Error :'numpy.ndarray' object has no attribute 'append'

Dual_array = array_1 + array_1
# It equals Dual_array = array_1 * 2
# [5+5, 6+6, 7+7, 8+8, 9+9]
# [5*2, 6*2, 7*2, 8*2, 9*2]
print(Dual_array)
# [10, 12, 14, 16, 18]

pow_array = array_1 ** 2
# [ 1,  4,  9, 16, 25]
sqrt_array = np.sqrt(array_1)
# [1, 1.41421356, 1.73205081, 2, 2.23606798]
log_array = np.log(array_1)
# [0, 0.69314718, 1.09861229, 1.38629436, 1.60943791]

# Exponential function
exp_array = np.exp(array_1)
# [2.71828183, 7.3890561, 20.08553692, 54.59815003, 148.4131591]
##############################
```
