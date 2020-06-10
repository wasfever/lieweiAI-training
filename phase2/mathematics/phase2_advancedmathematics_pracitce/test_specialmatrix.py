# -*- coding: utf-8 -*-
'''
@Time    : 2020/5/29 19:27
@Author  : s.xiao
@FileName: test_specialmatrix.py
@Software: PyCharm
使用numpy和torch特殊矩阵的实现
1.对角阵
2.单位阵
3.下三角阵
4.全1（0）阵
'''

import numpy as np
import torch

print("========对角阵=========")
# 1.对角阵
diag_a = np.diag([1, 3, 5, 7])  # 主对角线上值为1,3,5,7，矩阵其余元素值为0
print(diag_a)
print("torch: \n")
diag_b = torch.diag(torch.tensor([1, 3, 5, 7]))
print(diag_b)
print("========单位阵=========")
# 单位阵
unit_a = np.eye(4)  # 默认是4*4的方阵
unit_b = np.eye(3, 4)  # 也可以指定形状
print(unit_a, "\n", unit_b)
print("torch: \n")
unit_c = torch.eye(5)
print(unit_c)
print("\n ========下三角阵=========")
tria_a = np.tri(3, 4)  # 下三角矩阵，元素为1
print(tria_a)
tria_b = torch.tril(torch.ones(3, 3))  # torch.tril构建下三角矩阵需要指定下三角部分元素值为1
print(tria_b)
print("\n ========全0（1）阵=========")
allone_a = np.ones((3, 3))
print(allone_a)
allone_b = torch.ones((3, 3))
print(allone_b)
allzero_a = np.zeros((4, 4))
allzero_b = torch.zeros((5, 5))
print(allzero_a)
print(allzero_b)
