import numpy as np

a = np.array([1,2,3])
b = np.array([[1,2],[3,4],[5,6]])

print(a[0])
# 1

print(b[1][1])
# 4

print(b[1,1])
# 4

c = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print(c.shape)
# (4,3)
# (rows, columns)

print(c)
'''
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
'''
print(c.T)
'''
[[ 1  4  7 10]
 [ 2  5  8 11]
 [ 3  6  9 12]]
'''
# function(T) is swap rows and columns

print(c.ndim)
# 2
# 2 Dimension

print(c.size)
# 12

print(c.dtype)
# int64

d = np.array([[1,2],[3,4]], dtype=np.float64)
print(d.dtype)
# float64

print(c.itemsize)
# 8
# Each number takes 8 bytes in int64

print(d.itemsize)
# 8
# Each number takes 8 bytes in float64

print(c.min())
# 1
print(c.max())
# 12

print(c)
'''
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
'''
print(c.sum())
# 1+2+3+4+5+6+7+8+9+10+11+12
# 78

print(c.sum(axis=0))
# sum all columns
'''
1+4+7+10=22
2+5+8+11=26
3+6+9+12=30
'''
# [22 26 30]
# It equals c.T.sum(axis=1)

print(c.sum(axis=1))
# sum all rows
'''
1+2+3=6
4+5+6=15
7+8+9=24
10+11+12=33
'''
# [ 6 15 24 33]

A = np.array([[1,2],[3,4],[5,6]])
print(b)
'''
array([[1, 2],
       [3, 4],
       [5, 6]])
'''
M = np.matrix([[1,2],[3,4],[5,6]])
print(M)
'''
matrix([[1, 2],
        [3, 4],
        [5, 6]])
'''
