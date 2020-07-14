import numpy as np
import numpy.ma as ma


matrixa = np.zeros((6,6))
x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print(x)
print(x.sum(axis=0))
print(x.sum(axis=1))
mx = ma.masked_array(x, mask=[0,0,0,1,0,2])

y = np.random.rand(4,3,2)
np.set_printoptions(precision=2)
print(y)
print(y.sum(axis=0))
print(y.sum(axis=1))
print(y.sum(axis=2))

q = np.random.rand(5,6,7,8)
np.set_printoptions(precision=9)
print('q', q)

z = np.fromfunction(lambda i, j: i == j, (3, 3), dtype=int)
w = np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
v = np.fromfunction(lambda i, j , k: i*i*i + j*j+ k, (5, 5, 5), dtype=int)
u = np.fromfunction(lambda q, p : q != p, (5,6), dtype=int)
print('z', z)
print('w', w)
print('v', v)
print('u', u)

a = np.random.rand(2,2,2)
np.set_printoptions(precision = 0)
print(a)

b = np.arange(6).reshape(2,3)
for x in np.nditer(a.T):
    print(x, end = '')
