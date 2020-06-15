# -*- coding: utf-8 -*-
'''
@Time    : 2020/6/15 22:52
@Author  : s.xiao
@FileName: test02.py
@Software: PyCharm
numpy 基本操作
'''
import numpy as np

print("===使用列表生成数组")
datalist = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
x = np.array(datalist)
print(x.dtype)
print(x.shape)
print(x.ndim)  # 维度
print(x.size)

print("===全0 zeros/全1 ones /empty")
x_zeros = np.zeros((2, 3))  # 默认为float类型，可以通过dtype参数指定类型如：dtype = npint32
y_ones = np.ones((2, 4))
print(x_zeros.dtype)
print(x_zeros, "\n", y_ones)

print("===使用arange生成连续元素")
print(np.arange(6))  # 左闭右开取6个数，默认步长为1，也可指定步长如下
print(np.arange(1, 10, 2))  # 从1开始取到9，步长为2
a = np.arange(20)
print(a)
a = a.reshape(5, 4)  # 改变形状，但size要与原来相同
print(a)

print("===使用astype复制数组，并改变元素类型")
x = np.array([1, 2, 3, 4, 5, 6])
y = x.astype(dtype=float)  # 复制时必须指定元素类型dtype
print(x)
print(y)

print("===ndarray的基本运算")
x = np.array([[1, 5, 3], [2, 3, 4]])
print(x.shape)
y = np.array([[1, 2], [3, 4], [5, 7]])
print(y.shape)
print(x * 2)  # 点乘
print(np.matmul(x, y))  # 矩阵相乘
print(x > 2)  # 布尔运算，结果为False或True

print("===ndarray基本索引")
x = np.array([[1, 2], [3, 5], [7, 8]])
print(x.shape)
print(x[0])
print(x[1, 1])
x = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(x.shape)
print(x[1])
print(x[0, 1])
print(x[1, 1, 1])

print("==生成副本.copy")
print(x[0])
y = x[0].copy()  # 生成副本后，对其操作不影响原变量，否则会改变原来的值
z = x[0]
y[0, 0] = 111
print(x[0])  # 修改副本不会造成影响
z[0, 0] = 111
print(x[0])  # 此时x[0,0]元素已经被修改

print("===ndarray基本切片")  # 注意切片不改变数据维度
x = np.array([1, 2, 3, 4, 5])
print(x[1:4])
print(x[:4])
print(x[::2])  # 按照步长为2切片
y = np.array([[2,3],[3,5],[5,6]])
print(y[:2])
print(y[:2,:1])
print("===ndarray布尔索引")
x = np.array([3, 2, 1, 45, 5, 6])
y = np.array([True, False, False, True, False, True])
print(x[y])
print(x[y == False])

