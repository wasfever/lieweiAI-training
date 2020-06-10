# -*- coding: utf-8 -*-
'''
@Time    : 2020/5/25 19:41
@Author  : s.xiao
@FileName: test_matrixbasiccal.py
@Software: PyCharm
矩阵的基本运算
'''

import torch
import numpy as np

a = torch.tensor([[1, 2], [3, 4], [5, 6]])
b = torch.tensor([[5, 6], [7, 8], [9, 10]])
c = torch.tensor([[1, 2], [3, 4]])
# a、b、c的形状
print("sharp a:", a.shape, " sharp b:", b.shape, "sharp c:", c.shape)
print("----------")
print("矩阵加减：", a + b)
print("--------------------")
print("数加（减）：", 3 + a)
print("--------------------")
print("矩阵点乘：", a * b)
print("--------------------")
print("矩阵数乘:", 5 * a)
print("--------------------")
# print("矩阵叉乘:", b@c)
x = torch.matmul(b, c)
print("矩阵叉乘：",x)  #一般叉乘采用这种形式
print("--------------------")
t = b.t()
print("矩阵的转置：", t)
print(t.shape)
print("--------------------")
d = torch.Tensor([[1, 2], [3, 4]])
inv = d.inverse()
print("矩阵求逆：", inv)
print("--------------------")
d = np.array([[1, 2], [3, 4]])
inv = np.linalg.inv(d)
print("numpy矩阵求逆： ", inv)