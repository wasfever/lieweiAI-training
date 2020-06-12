# -*- coding: utf-8 -*-
'''
@Time    : 2020/6/12 23:10
@Author  : s.xiao
@FileName: test01.py
@Software: PyCharm
全连接拟合非线性问题
'''

import torch
from torch import nn
import matplotlib.pyplot as plt

# 数据构造 y = x ³
x = torch.arange(-10.0, 10.0)
y = x.pow(3)
# plt.plot(x,y,".")  一般用于折线图
plt.scatter(x, y)
plt.show()
