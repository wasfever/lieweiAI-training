# -*- coding: utf-8 -*-
'''
@Time    : 2020/5/29 19:07
@Author  : s.xiao
@FileName: test_determinant.py
@Software: PyCharm
分别使用numpy和torch实现矩阵行列式计算
'''

import numpy as np
import torch

# 使用numpy进行行列式计算
a = np.array([[1, 2], [3, 4]])
print(a.shape)
det_a = np.linalg.det(a)
print("numpy计算行列式值为： ", det_a)
print("-----------\n")
# 使用torch实现行列式计算
b = torch.tensor([[1., 2.], [3., 4.]])  # 注意数据类型为浮点型
det_b = b.det()
print("torch计算行列式值为： ", det_b)
