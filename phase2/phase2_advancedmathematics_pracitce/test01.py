# -*- coding: utf-8 -*-
'''
@Time    : 2020/5/19 23:12
@Author  : s.xiao
@FileName: test01.py
@Software: PyCharm
'''

import numpy as np
import matplotlib.pyplot as mlp


# 实现幂函数画图
def power_function():
    x = np.arange(-100, 100)
    # y = x**2
    # y = x**3
    y = x ** (-1)  # 注意x取值不能为0
    mlp.plot(x, y)  # plot表示折线图
    mlp.show()


# 实现常函数
def constant_function():
    x = np.arange(-10, 10)
    y = np.tile([3], x.shape)  # 广播，次数为x的长度
    mlp.plot(x, y)
    mlp.show()


# 指数函数
def exponential_function():
    x = np.arange(-5, 5, 0.1)
    y = 2 ** x
    y1 = 0.5 ** x
    mlp.plot(x, y)
    mlp.plot(x, y1)
    mlp.show()


if __name__ == '__main__':
    # power_function()
    # constant_function()
    exponential_function()
