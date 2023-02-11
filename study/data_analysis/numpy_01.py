import numpy as np
#
a1  = np.array([1, 2, 3, 4, 5])
# print(a1)
# print(type(a1))
# print(a1.shape)
#
a2 = np.array([ [1,2,3],[2,3,4 ], [7,8,9]])
# print(a2)
# print(type(a2))
# print(a2.shape)
#
#
a3 = np.array([ [[1,2,3],[2,3,4 ], [7,8,9]],
                [[1,2,3],[3,4,5],[5,6,7]],
                [[1,2,3],[3,4,5],[5,6,7]]])
# print(a3)
# print(type(a3))
# print(a3.shape)
#
#
# print(np.zeros(10))
# print(np.ones((3, 3)))
# print(np.eye(3))
# print(np.tri(3))
# print(np.empty(10))
# a4 = np.arange(0,30, 2)
# print(a4)
#
# a5 = np.linspace(0, 1 ,5)
# print(a5)
# a6 = np.logspace(0.1, 1, 20)
# print(a6)
#
#
# a7 = np.random.random((3,3))
# print(a7)
#
# a8 = np.random.randint(0,10,(3,3))
# print(a8)
# a9 = np.random.normal(0,1,(3,3))
# print(a9)
# a10 = np.random.randn(3,3)
#
#
# a11 = np.full_like(a3,30)
# print(a11)
#
#
#
#
# # a12 = np.arange(0, 30, 2)
# a12 = np.ones((3,3), dtype=bool)
#
#
#
# print(a12)
# print(type(a12))
# print(a12.shape)
# date = np.array('2020-01-01', dtype=np.datetime64)
#
# date01 = date + np.arange(12)
# print(date01)
# print(type(date01))
# print(date.shape)
# def array_info(array):
#     print(array)
#     print('ndim', array.ndim)
#     print('shape', array.shape)
#     print('dtype', array.dtype)
#     print('size', array.size)
#     print('itemsize', array.itemsize)
#     print('nbytes:', array.nbytes)
#     print('strides', array.strides)
#
# array_info(a1)
# array_info(a2)
# array_info(a3)
#
# print(a2)
# print(a2[0,2])
# print(a2[2,-1])
#
# print(a1)
# print(a1[0:2])
# print(a1[2:])
# print(a1[::-1])
#
# print(a1)
# bi = [False, True, True, False, True]
#
# print(a1[bi])
# bi = [True, False, True, True, False]
# print(a1[bi])
#
# print(a2)
# bi = np.random.randint(0,2, (3,3 ), dtype=bool)
# print(bi)
# print(a2[bi])
#
# print('_______________________________________________')
#
#
#
# print(a1)
# print(a1[0], a1[2])
# ind = [0,2]
# print(a1[ind])
# ind = np.array([[0,1],
#                [2,0]])
# print(a1[ind])
#
# print(a2)
# row = np.array([0,2])
# col = np.array([1,2])
# print(a2[row, col])
# print(a2[row, :])
# print(a2[: ,col ])
#
# print('++++++++++++++++++++++++++++++++++++++++++++')
#
#
# print(a1)
# b1 = np.insert(a1, 0, 10)
# print(b1)
# print(a1)
# c1 =  np.insert(a1, 2, 10)
# print(c1)
#
# print(a2)
# b2 = np.insert(a2, 1, 10, axis= 0)
# print(b2)
# c2 = np.insert(a2, 1, 10, axis= 1)
# print(c2)
#
#
# print(a1)
# a1[0] = 1
# a1[1] = 2
# a1[2] = 3
# print(a1)
#
# print(a1)
# b1 = np.delete(a1,1)
# print(b1)
#
#
# print(a2)
# b2 = np.delete(a2,1, axis=0)
# print(b2)
# c2 = np.delete(a2, 1, axis=1)
#
# print(c2)
# print('___________________________________')
# print(a2)
# print(a2[:2, :2])
#
# a2_sub = a2[:2, :2]
# print('_____________________')
# print(a2_sub)
# a2_sub[:, 1] = 0
#
# print(a2_sub)
# print(a2)
# print('________________________________')
# print(a2)
# a2_sub_copy = a2[:2, :2].copy()
# print(a2_sub_copy)
# a2_sub_copy[:, 1] = 1
# print(a2_sub_copy)
# print(a2)
#
# print(a2.T)
# print('0000000000000000000000000000000000')
# print(a3)
#
# print(a3.T)
# print('_________________')
# n1 = np.arange(1,10)
# print(n1)
# print(n1.reshape(3,3))
#
#
#
# a2 = np.arange(1, 10).reshape(3,3)
# print(a2)
# b2 = np.arange(10,19).reshape(3,3)
# print(b2)
#
#
#
# c2 = np.append(a2, b2, axis=1)
#
# print(c2)
#
# d2 = np.concatenate([a2, b2], axis=0)
#
# print(d2)
#
# d3 = np.concatenate([a2, b2], axis=1)
#
#
# d4 = np.hstack([a2,a2])
# d5 = np.dstack([a2, a2])
# print(d5)
#
# a1 = np.arange(0,10)
# print(a1)
# b1, c1 = np.split(a1, [5])
# print(b1,c1)
# b1, c1, d1, e1, f1 = np.split(a1, [2,4,6,8])
# print(b1, c1, d1, e1, f1)
# a2 = np.arange(1,10).reshape(3, 3)
# print(a2)
# # b2, c2 = np.vsplit(a2, [2])
# # print(b2)
# # print(c2)

#
#
# a3 = np.arange(1,28).reshape(3, 3, 3)
# print(a3)
print('__________________')
#
# b3, c3 = np.dsplit(a3, [2])
# print(b3)# print(c3)
# ____________________________________________________

#
# a1= np.array([1, 2, 3])
# print(a1 +5)
# a2 = np.arange(1, 10).reshape(3, 3)
# print(a1 + a2)
# b2 = np.array([1, 2, 3]).reshape(3, 1)
# print(b2)
# print(a1 + b2)

# __________________________산술연산
# a1 = np.arange(1,10)
# print(a1)
# print(a1 +1)
# print(np.add(a1, 10))
# print(np.subtract(a1, 10))
# print(np.negative(a1))
# print(np.multiply(a1, 2))
#
# #  a1 / 2
# print(np.divide(a1, 2))
# # a1 // 2
# print(np.floor_divide(a1, 2))
# # a1 ** 2
# print(np.power(a1, 2))
# # a1 % 2
# print(np.mod(a1, 2))

# a1 = np.random.randint(-10, 10, size=5)
#
# print(a1)
# print(np.absolute(a1))
#
# print(np.square(a1))
# print(np.sqrt(a1))

# a1 = np.random.randint(1,10, size= 5)
# print(a1)
# print(np.exp(a1))
# print(np.exp2(a1))
# print(np.power(a1, 2))
#
# print(np.log(a1))
#
#
# t = np.linspace(0, np.pi, 3)
# print(t)
# print(np.sin(t))
# print(np.cos(t))
# print(np.tan(t))
#
#
#
# a2 = np.random.randint(1, 10 , size= (3,3))
# print(a2)
#
# print(a2.sum(), np.sum(a2))
#
# print(a2.sum(axis=0), np.sum(a2, axis=0))
#
# print(a2.sum(axis=1), np.sum(a2, axis=1))
#
# print(np.cumsum(a2))
# print(np.cumsum(a2,axis=0))
# print(np.cumsum(a2, axis=1)


a1 = np.arange(1,10)
print(a1)
print(a1 == 5)
print(a1 != 5)
print(a1<5)
a2 = np.arange(1,10).reshape(3,3)
print(a2)
print(np.sum(a2))
print(np.sum(a2 >5))
b1 = [1,2,3,4,5,3,7,8,9]

print(np.all(a2 > 5, axis= 1))

print(np.isinf(a1))
print(np.isclose(a1, b1))
print([(a2 > 5) & (a2 < 8)])







