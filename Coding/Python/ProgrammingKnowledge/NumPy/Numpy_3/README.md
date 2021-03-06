# Basic Numpy 3  

## 1. Create a default array  

```python
import numpy as np

a = np.zeros((2,3))
print(a)
'''
[[0. 0. 0.]
 [0. 0. 0.]]
'''

b = np.ones((2,3),dtype=np.int16)
'''
[[1 1 1]
 [1 1 1]]
'''

c = np.empty((3,3),dtype=np.int16)
'''
[[     0      0      0]
 [-16384      0      0]
 [     0 -16384      2]]
'''

# np.arange(start, stop, step, dtype)
d = np.arange(1,5)
# [1 2 3 4]
e = np.arange(1,5,0.5)
# [1.  1.5 2.  2.5 3.  3.5 4.  4.5]
```

## 2. Create a even value gap array  

```python
# np.linspace(start, stop, amount)
# provide a even value between the items
f = np.linspace(1,50)
'''default amount = 50
[1.         1.08163265 1.16326531 1.24489796 1.32653061 1.40816327
 1.48979592 1.57142857 1.65306122 1.73469388 1.81632653 1.89795918
 1.97959184 2.06122449 2.14285714 2.2244898  2.30612245 2.3877551
 2.46938776 2.55102041 2.63265306 2.71428571 2.79591837 2.87755102
 2.95918367 3.04081633 3.12244898 3.20408163 3.28571429 3.36734694
 3.44897959 3.53061224 3.6122449  3.69387755 3.7755102  3.85714286
 3.93877551 4.02040816 4.10204082 4.18367347 4.26530612 4.34693878
 4.42857143 4.51020408 4.59183673 4.67346939 4.75510204 4.83673469
 4.91836735 5.        ]
'''
g = np.linspace(1,5,10)
'''
[1.         1.44444444 1.88888889 2.33333333 2.77777778 3.22222222
 3.66666667 4.11111111 4.55555556 5.        ]
'''
h = np.linspace(1,10,10)
'''
[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
'''
```

## 3. Create a random array  

```python
i = np.random.random((2,3))
'''
[[0.40362486 0.51464341 0.74334648]
 [0.79310058 0.76986135 0.11947724]]
'''

```

## 4. Reshape  
- It has to match the array size.  
- It won't change origin array, we have to assign to new variable.  
- `k = j.reshape(3,-1)`, `-1` will figure out the number if it is avalible.  

```python
j = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print(j)
'''
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
'''

print(j.shape)
# (4,3)
# (rows, columns)

k = j.reshape(3,4)
print(k)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''

```

## 3. vstack() v.s hstack()  

```python
l = np.array([[1,2,3],[4,5,6],[7,8,9]])
m = np.array([10,11,12])

n = np.vstack((m,l))
print(n)
'''
[[10 11 12]
 [ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]]
'''
o = np.vstack((l,m))
print(o)
'''
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
'''

p = np.array([[1,2,3],[4,5,6]])
q = np.array([[11,22],[33,44]])

r = np.hstack((p,q))
print(r)
'''
[[ 1  2  3 11 22]
 [ 4  5  6 33 44]]
'''
```

## 4. vsplit() v.s hsplit()  
```python
s = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
t = np.array([[1,2,3,4],[5,6,7,8]])

print(s)
'''
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
'''
u = np.vsplit(s,2)
print(u)
'''
[array([[1, 2, 3],
        [4, 5, 6]]),
 array([[ 7,  8,  9],
        [10, 11, 12]])]
'''
print(u[0])
'''
[[1 2 3]
 [4 5 6]]
'''
print(u[1])
'''
[[ 7  8  9]
 [10 11 12]]
'''

print(t)
'''
[[1 2 3 4]
 [5 6 7 8]]
'''
v = np.hsplit(t,4)
print(v)
'''
[array([[1],
        [5]]),
 array([[2],
        [6]]),
 array([[3],
        [7]]),
 array([[4],
        [8]])]
'''
print(v[0])
'''
[[1]
 [5]]
'''
print(v[1])
'''
[[2]
 [6]]
'''
print(v[2])
'''
[[3]
 [7]]
'''
print(v[3])
'''
[[4]
 [8]]
'''

```
